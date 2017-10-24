from utils import tohex, fromhex

bs = []
with open('p18.txt', 'rb') as f:
  for line in f:
    bs.append(fromhex(line))

def uniq(b):
  return len(set(b[::16]))

print tohex(sorted(bs, key=uniq)[0])
