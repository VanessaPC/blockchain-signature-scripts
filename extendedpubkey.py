from binascii import unhexlify

# Your vkey (64 bytes = 128 hex chars) 
vkey_hex = "c6597fdb8d0c72485be8ae8def9e582fa12632297a097f8b2a6c198b90f7b68d66ab501d440426354c22b20c0b7a4fc0480ea06361d2fb0a33fd739217e6f472"

# Split key
pub_key_bytes = unhexlify(vkey_hex[:64])
chain_code_bytes = unhexlify(vkey_hex[64:])


print("Public Key  :", pub_key_bytes.hex())
print("Chain Code  :", chain_code_bytes.hex())


ext_pub_key_bytes = pub_key_bytes + chain_code_bytes
print("Extended Pub Key (raw):", ext_pub_key_bytes.hex())
