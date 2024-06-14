palabra = input(str('Ingrese una palabra: '))

# buscamos como presentar la palabra ingresada y mostrarla

palabra_nueva = palabra[:]
palabra_invertida = palabra_nueva[::-1] 
centro_invertido = palabra_invertida[1:4]

print(palabra_nueva)
print (palabra_invertida)
print(centro_invertido)


