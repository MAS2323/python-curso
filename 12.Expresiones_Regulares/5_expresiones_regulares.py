# funcion seach: a diferencia de la funcion match la funcion seach busca en toda la cadena de texto
# si hay algun patron de coincidencia
import re

codigo1 = 'dasfkljasfiho;asfihoashio71dskjnfsl4'
codigo2 = 'Nina Snadra71dssfdjhbdsfjbhfdsaafdsa'
codigo3 = 'Sinforosa Idsfjkb,fdsfsda venga Onewesdfsdfsdfsd'

# tambien admite tres parametros, 1: patron de busqueda, 2: cadena de caracteres, 3: el flat (re.IGNORECASE)
if re.search('71', codigo3):

    print('Hemos encontrado el nombre')

else:
    print('No hemos encontrado el nombre')
