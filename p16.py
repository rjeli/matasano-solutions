import numpy as np
import itertools
from test import bsert
from utils import fromb64, xor
from p13 import score, xors

def hamming_dist(b1, b2):
  b1, b2 = np.unpackbits(bytearray(b1)), np.unpackbits(bytearray(b2))
  return np.count_nonzero(b1 != b2)

bsert | hamming_dist('this is a test', 'wokka wokka!!!') == 37

with open('p16.txt', 'rb') as f:
  b = fromb64(f.read())

dists = []
for KEYSIZE in xrange(2, 40):
  dist1 = hamming_dist(b[:KEYSIZE], b[KEYSIZE:2*KEYSIZE])
  dist2 = hamming_dist(b[KEYSIZE*2:KEYSIZE*3], b[KEYSIZE*3:KEYSIZE*4])
  dists.append((float(dist1+dist2)/2/KEYSIZE, KEYSIZE))

keysize_guesses = sorted(dists, key=lambda x: x[0])[:10]

for _, KEYSIZE in keysize_guesses:
  print 'trying keysize', KEYSIZE
  blocks = []
  for i in xrange(KEYSIZE):
    blocks.append(b[i::KEYSIZE])
  keys = []
  for block in blocks:
    plain, k = sorted([(str(x), k) for x, k in xors(block)], key=lambda x: score(x[0]))[-1]
    keys.append(k)
  bsert | len(keys) == KEYSIZE
  cycled = itertools.islice(itertools.cycle(keys), len(b))
  print 'key:', ''.join(chr(c) for c in keys)
  print xor(b, cycled)
