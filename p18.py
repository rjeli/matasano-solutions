from utils import fromhex

bs = []
with open('p18.txt', 'rb') as f:
  for line in f:
    bs.append(fromhex(line))

for b in bs:
  blocks = b[::16]
  d = {}
  for i, b in enumerate(blocks):
    if b in d:
      print 'dupe blocks', d[b], i
    else:
      d[b] = i
