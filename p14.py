from test import bsert
from utils import fromhex
from p13 import xors, score

def gen():
  with open('p14.txt', 'rb') as f:
    for line in f:
      for x in xors(fromhex(line.strip())):
        yield str(x).strip()

bsert | sorted(gen(), key=score)[-1] == 'Now that the party is jumping'