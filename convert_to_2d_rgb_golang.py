#!/usr/bin/env python3

"""
imports a png and prints to screen  a 2d array of it's RGB values.
output is formatted to be pasted into golang code as a 2d array. 
"""

from xml.dom import NAMESPACE_ERR
from PIL import Image
import sys

import numpy as np
np.set_printoptions(threshold=np.inf)

import pprint
pp = pprint.PrettyPrinter(width=240, compact=True)


image = Image.open('input.png')

im_r, im_g, im_b, im_a = image.split()
im_r = np.array(im_r, dtype=int).transpose()
im_g = np.array(im_g, dtype=int).transpose()
im_b = np.array(im_b, dtype=int).transpose()


print(f"Rvals = [][]uint8{{")
for  _, row in enumerate(im_r.astype(int)):
    print(f"{list(row)},".replace('[', '{').replace(']', '}'))
print(f"}}")

print(f"Gvals = [][]uint8{{")
for  _, row in enumerate(im_g.astype(int)):
    print(f"{list(row)},".replace('[', '{').replace(']', '}'))
print(f"}}")

print(f"Bvals = [][]uint8{{")
for  _, row in enumerate(im_b.astype(int)):
    print(f"{list(row)},".replace('[', '{').replace(']', '}'))
print(f"}}")
