import os

values = ['True','False',"true","false",True,False]

for value in values:
    os.environ['INPUT_IS_PUBLIC'] = values

    resultado = os.environ.get('INPUT_IS_PUBLIC',False)  |     os.environ.get('INPUT_IS_PUBLIC',False) == "True" | os.environ.get('INPUT_IS_PUBLIC',False) == "true"
    print (value,resultado)
