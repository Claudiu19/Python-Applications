import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256


key = RSA.importKey(open("public_merchant.pem", "rb").read())
client_public_key_text = open("public_client.pem", "rb").read()
client_private_key = RSA.importKey(open("private_client.pem", "rb").read())
pg_public_key = RSA.importKey(open("public_pg.pem", "rb").read())

# Start Message 1
data = client_public_key_text
session_key = get_random_bytes(16)

cypher_rsa = PKCS1_OAEP.new(key)
enc_session_key = cypher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
message = enc_session_key + b'abcde' + cipher_aes.nonce + b'abcde' + tag + b'abcde' + ciphertext

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8081))
print("Sending Message 1")
s.sendall(message)
# End Message 1

# Start Message 2
print('Receiving Message 2')
data = s.recv(1024)
x = data.split(b'abcde')
enc_session_key1 = x[0]
nonce1 = x[1]
tag1 = x[2]
ciphertext1 = x[3]

cipher_rsa1 = PKCS1_OAEP.new(client_private_key)
session_key1 = cipher_rsa1.decrypt(enc_session_key1)

cipher_aes1 = AES.new(session_key1, AES.MODE_EAX, nonce1)
message2 = cipher_aes1.decrypt_and_verify(ciphertext1, tag1)
ids = message2.split(b'abcde')

h = SHA256.new(ids[0])
valid = False
try:
     PKCS1_v1_5.new(key).verify(h, ids[1])
     valid = True
except (ValueError, TypeError):
     valid = False
print("Valid: ", valid)
# End Message 2

# Start Message 3
session_key1 = get_random_bytes(16)
cypher_rsa1 = PKCS1_OAEP.new(pg_public_key)
enc_session_key1 = cypher_rsa1.encrypt(session_key1)
cipher_aes1 = AES.new(session_key1, AES.MODE_EAX)

CardN = b'1234-5678-9012'
CardExp = b'9/19'
CCode = b'456'
Amount = b'1200$'
NC = cipher_aes1.nonce
M = b"To be found"
OrderDesc = b"Some items"

PI_text = CardN + b'\\\\\\gh' + CardExp + b'\\\\\\gh' + CCode + b'\\\\\\gh' + ids[0] + b'\\\\\\gh' + Amount + b'\\\\\\gh' + client_public_key_text + b'\\\\\\gh' + NC + b'\\\\\\gh' + M
PO_non_enc_text = OrderDesc + b'\\\\\\gh' + ids[0] + b'\\\\\\gh' + Amount
h = SHA256.new(PO_non_enc_text)
signer = PKCS1_v1_5.new(client_private_key)
PO = PO_non_enc_text + b'\\\\\\rt' + signer.sign(h)
h = SHA256.new(PI_text)
PM = PI_text + b'\\\\\\rt' + signer.sign(h)


ciphertext1, tag1 = cipher_aes1.encrypt_and_digest(PM)
message = enc_session_key1 + b'\\\\\\abcdeg' + cipher_aes1.nonce + b'\\\\\\abcdeg' + tag1 + b'\\\\\\abcdeg' + ciphertext1

message_sent = PO + b'\\\\\\abl' + message
session_key = get_random_bytes(16)
cypher_rsa = PKCS1_OAEP.new(key)
enc_session_key = cypher_rsa.encrypt(session_key)
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message_sent)
message = enc_session_key + b'\\\\\\abcdef' + cipher_aes.nonce + b'\\\\\\abcdef' + tag + b'\\\\\\abcdef' + ciphertext
print('Sending Message 3')
s.sendall(message)
# End Message 3

# Start Message 6
print('Receiving Message 6')
data = s.recv(5120)
x = data.split(b'\\\\abcdeh')
enc_session_key1 = x[0]
nonce1 = x[1]
tag1 = x[2]
ciphertext1 = x[3]

cipher_rsa1 = PKCS1_OAEP.new(client_private_key)
session_key1 = cipher_rsa1.decrypt(enc_session_key1)

cipher_aes1 = AES.new(session_key1, AES.MODE_EAX, nonce1)
message2 = cipher_aes1.decrypt_and_verify(ciphertext1, tag1)
data2 = message2.split(b'\\\\\\gh')
print("Response: " + str(data2[0]))
print("Sid: " + str(data2[1]))

# End Message 6

