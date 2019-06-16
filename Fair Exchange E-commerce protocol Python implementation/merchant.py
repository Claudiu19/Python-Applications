import socket
import uuid
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256

private_key = RSA.import_key(open("private_merchant.pem").read())
pg_key = RSA.importKey(open("public_pg.pem", "rb").read())
while True:
# Start Message 1
    client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_s.bind(('localhost', 8081))
    client_s.listen()
    conn_client, addr_client = client_s.accept()
    print('Receiving Message 1')
    data = conn_client.recv(1024)

    x = data.split(b'abcde')
    enc_session_key = x[0]
    nonce = x[1]
    tag = x[2]
    ciphertext = x[3]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    client_public_key_text = cipher_aes.decrypt_and_verify(ciphertext, tag)
    client_public_key = RSA.import_key(client_public_key_text)
    # End Message 1


    # Start Message 2
    Sid = uuid.uuid1().bytes
    h = SHA256.new(Sid)
    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(h)
    data = Sid + b'abcde' + sig

    session_key = get_random_bytes(16)

    cypher_rsa = PKCS1_OAEP.new(client_public_key)
    enc_session_key = cypher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    message = enc_session_key + b'abcde' + cipher_aes.nonce + b'abcde' + tag + b'abcde' + ciphertext
    print('Sending Message 2')
    conn_client.sendall(message)
    # End Message 2

    # Start Message 3
    print('Receiving Message 3')
    data = conn_client.recv(3072)
    x = data.split(b'\\\\\\abcdef')
    enc_session_key = x[0]
    nonce = x[1]
    tag = x[2]
    ciphertext = x[3]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data1 = cipher_aes.decrypt_and_verify(ciphertext, tag)
    data = data1.split(b'\\\\\\abl')
    PO_text = data[0].split(b'\\\\\\rt')
    h = SHA256.new(PO_text[0])
    valid = False
    try:
        PKCS1_v1_5.new(private_key).verify(h, PO_text[1])
        valid = True
    except (ValueError, TypeError):
        valid = False
    print("Valid: ", valid)
    PO = PO_text[0].split(b'\\\\\\gh')
    # End Message 3

    # Start Message 4
    message = data[1]
    to_sign = Sid + b'\\\\\\gh' + client_public_key_text + b'\\\\\\gh' + PO[2]
    signed = signer.sign(SHA256.new(to_sign))
    message += b'\\\\\\abh' + signed
    session_key = get_random_bytes(16)

    cypher_rsa = PKCS1_OAEP.new(pg_key)
    enc_session_key = cypher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)
    message1 = enc_session_key + b'\\\\abcdeh' + cipher_aes.nonce + b'\\\\abcdeh' + tag + b'\\\\abcdeh' + ciphertext

    pg_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pg_s.connect(('localhost', 8082))
    print('Sending Message 4')
    pg_s.sendall(message1)
    # End Message 4


    # Start Message 5
    print('Receiving Message 5')
    data = pg_s.recv(5120)
    y = data.split(b'\\\\\\abcdel')
    enc_session_key = y[0]
    nonce = y[1]
    tag = y[2]
    ciphertext = y[3]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    send_to_client = cipher_aes.decrypt_and_verify(ciphertext, tag)
    # End Message 5

    # Start Message 6
    session_key = get_random_bytes(16)

    cypher_rsa = PKCS1_OAEP.new(client_public_key)
    enc_session_key = cypher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(send_to_client)
    message1 = enc_session_key + b'\\\\abcdeh' + cipher_aes.nonce + b'\\\\abcdeh' + tag + b'\\\\abcdeh' + ciphertext
    print('Sending Message 6')
    conn_client.sendall(message1)

    # End Message 6
