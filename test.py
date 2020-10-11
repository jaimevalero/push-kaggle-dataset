import os
from distutils import strtobool
values = ('True','False',"true","false",True,False)

for value in values:
    print (value)
    os.environ['INPUT_IS_PUBLIC'] = value
    #resultado = os.environ.get('INPUT_IS_PUBLIC',False) == True
    resultado =bool( strtobool(some_string))

    print (value,resultado)

# |     os.environ.get('INPUT_IS_PUBLIC',False) == "True" | os.environ.get('INPUT_IS_PUBLIC',False) == "true"
