from Cryptodome.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private_client.pem", "wb")
file_out.write(private_key)
public_key = key.publickey().export_key()
file_out = open("public_client.pem", "wb")
file_out.write(public_key)

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private_merchant.pem", "wb")
file_out.write(private_key)
public_key = key.publickey().export_key()
file_out = open("public_merchant.pem", "wb")
file_out.write(public_key)

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private_pg.pem", "wb")
file_out.write(private_key)
public_key = key.publickey().export_key()
file_out = open("public_pg.pem", "wb")
file_out.write(public_key)