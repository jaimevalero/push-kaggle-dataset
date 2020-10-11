import os
import sys

from distutils.util import strtobool



values = ('True','False',"true","false",True,False)

for j,value in enumerate(values):
    #rint (value)
    #resultado = os.environ.get('INPUT_IS_PUBLIC',False) == True
    resultado = strtobool(str(value))

    print (j,value,resultado)

# |     os.environ.get('INPUT_IS_PUBLIC',False) == "True" | os.environ.get('INPUT_IS_PUBLIC',False) == "true"
