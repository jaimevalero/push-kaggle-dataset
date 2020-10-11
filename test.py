import os
import sys

from distutils.util import strtobool



values = ('True','False',"true","false",True,False)

for j,value in enumerate(values):
    print (value)
    os.environ['INPUT_IS_PUBLIC'] = value
    #resultado = os.environ.get('INPUT_IS_PUBLIC',False) == True
    resultado =bool( strtobool(str(value)))

    print (j,value,resultado)

# |     os.environ.get('INPUT_IS_PUBLIC',False) == "True" | os.environ.get('INPUT_IS_PUBLIC',False) == "true"
