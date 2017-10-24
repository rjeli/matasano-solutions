import glob
import unittest

class _Bsert(object):
  def __or__(self, other):
    return _Wrapped(other)

bsert = _Bsert()

class _Wrapped(unittest.TestCase):
  def __init__(self, obj):
    super(_Wrapped, self).__init__('__init__')
    self.wrapped = obj
  def __eq__(self, other):
    self.assertEqual(self.wrapped, other)

if __name__ == '__main__':
  for fn in glob.glob('p*.py'):
    __import__(fn[:-3])