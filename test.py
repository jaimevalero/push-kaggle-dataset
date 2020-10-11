import os

values = ('True','False',"true","false",True,False)

for value in values:
    print (value)

    os.environ['INPUT_IS_PUBLIC'] = values
    resultado = os.environ.get('INPUT_IS_PUBLIC',False)
    print (value,resultado)

# |     os.environ.get('INPUT_IS_PUBLIC',False) == "True" | os.environ.get('INPUT_IS_PUBLIC',False) == "true"
