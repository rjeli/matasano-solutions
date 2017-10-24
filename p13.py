from test import bsert
from utils import fromhex, xor
from collections import defaultdict

common = set([' ', 'e', 't', 'a', 'o', 'i', 'n', 's'])
def score(s):
  ret = 0
  ret += sum(ord('A') <= ord(c) <= ord('z') for c in s)
  ret += sum(1 for c in s if c in common)
  return ret

def xors(b):
  return ((xor(b, [c]*len(b)), c) for c in xrange(0, 255))

b = fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
best = sorted([str(x) for x, k in xors(b)], key=score)[-1]
bsert | best == 'Cooking MC\'s like a pound of bacon'