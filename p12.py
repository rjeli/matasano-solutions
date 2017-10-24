from test import bsert
from utils import tohex, fromhex, xor

b1 = fromhex('1c0111001f010100061a024b53535009181c')
b2 = fromhex('686974207468652062756c6c277320657965')
bsert | tohex(xor(b1, b2)) == '746865206b696420646f6e277420706c6179'
