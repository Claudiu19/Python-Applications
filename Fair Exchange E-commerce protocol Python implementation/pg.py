import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256

private_key = RSA.import_key(open("private_pg.pem").read())
merchant_key = RSA.importKey(open("public_merchant.pem", "rb").read())
print("Loaded keys")
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8082))
    s.listen()
    conn, addr = s.accept()

    # Start Message 4
    print('Receiving Message 4')
    data = conn.recv(4096)

    x = data.split(b'\\\\abcdeh')
    enc_session_key = x[0]
    nonce = x[1]
    tag = x[2]
    ciphertext = x[3]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    package = cipher_aes.decrypt_and_verify(ciphertext, tag)
    data2 = package.split(b'\\\\\\abh')

    data3 = data2[0].split(b'\\\\\\abcdeg')
    enc_session_key = data3[0]
    nonce = data3[1]
    tag = data3[2]
    ciphertext = data3[3]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    client_package = cipher_aes.decrypt_and_verify(ciphertext, tag)
    # End Message 4

    # Start Message 5
    data = client_package.split(b"\\\\\\gh")
    Resp = b"Accepted"
    to_sign = Resp + b'\\\\\\hg' + data[3] + b'\\\\\\hg' + data[4] + b'\\\\\\hg' + data[6]
    h = SHA256.new(to_sign)
    signer = PKCS1_v1_5.new(private_key)
    signed= signer.sign(h)
    message = Resp + b'\\\\\\gh' + data[3] + b'\\\\\\gh' + signed

    session_key = get_random_bytes(16)

    cypher_rsa = PKCS1_OAEP.new(merchant_key)
    enc_session_key = cypher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)
    message1 = enc_session_key + b'\\\\\\abcdel' + cipher_aes.nonce + b'\\\\\\abcdel' + tag + b'\\\\\\abcdel' + ciphertext
    print('Sending Message 5')
    conn.sendall(message1)
    #End Message 5


