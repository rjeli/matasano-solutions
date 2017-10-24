from utils import fromb64
from Crypto.Cipher import AES

with open('p17.txt', 'rb') as f:
  b = fromb64(f.read().strip())

key = 'YELLOW SUBMARINE'
aes = AES.new(key, AES.MODE_ECB)

print aes.decrypt(b)