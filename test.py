import os
import distutils
values = ('True','False',"true","false",True,False)

for value in values:
    print (value)
    os.environ['INPUT_IS_PUBLIC'] = value
    #resultado = os.environ.get('INPUT_IS_PUBLIC',False) == True
    resultado =bool(distutils.util.strtobool(some_string))

    print (value,resultado)

# |     os.environ.get('INPUT_IS_PUBLIC',False) == "True" | os.environ.get('INPUT_IS_PUBLIC',False) == "true"
