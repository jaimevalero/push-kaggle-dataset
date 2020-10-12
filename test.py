import os
import sys

from distutils.util import strtobool



values = ('True','False',"true","false",True,False)

for j,value in enumerate(values):
    resultado = strtobool(str(value))
    print (j,value,resultado)
