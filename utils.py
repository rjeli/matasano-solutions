import binascii

def tohex(b):
  return binascii.hexlify(b)

def fromhex(s):
  return bytearray(binascii.unhexlify(s.strip()))

def tob64(b):
  return binascii.b2a_base64(b).rstrip()

def fromb64(s):
  return binascii.a2b_base64(s)

def xor(b1, b2):
  b1, b2 = bytearray(b1), bytearray(b2)
  return bytearray([x ^ y for x, y in zip(b1, b2)])
