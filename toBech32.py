#!/usr/bin/env python3
import bech32

def bech32_encode(hex_key: str): 
  key_bytes = bytes.fromhex(hex_key)
  five_bit = bech32.convertbits(key_bytes, 8, 5, True)
  bech = bech32.bech32_encode("ed25519_sk", five_bit)
  return bech

hex_key = "e84f3ee5298cb1fca85f00769925210e8ea2f562b9a6e338ea0d6c56ac91fa01a400b4580702fbeefbf9f970cc9d07bdcf276ab98f92719e7e258811d0e2a3c466ab501d440426354c22b20c0b7a4fc0480ea06361d2fb0a33fd739217e6f472"  # <-- replace this with your skey
print(bech32_encode(hex_key))