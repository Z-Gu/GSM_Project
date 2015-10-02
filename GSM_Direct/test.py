#!/usr/bin/python

#Demonstrates the encoding and decoding

from seg_temp import *
from decoder import decode

b = s_t(a)
print b
c = decode(b)
print c[0] == a
