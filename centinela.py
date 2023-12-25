"""
Este código tiene como objetivo contar la cantidad de dígitos que tiene un número entero ingresado por el usuario.

La función contar_digitos toma un número entero como argumento y utiliza un bucle while para contar los dígitos del número.

Comienza inicializando un contador en cero y una bandera terminar como False.
Luego, entra en un bucle while que se ejecutará hasta que terminar sea True.
Dentro del bucle, comprueba si el número es igual a cero. Si lo es, asigna True a terminar, lo que detiene el bucle.
Si el número no es cero, incrementa el contador en uno y divide el número entre 10 usando la operación //=, lo que descarta
el último dígito del número en cada iteración.
Cuando el número llega a cero, se establece la bandera terminar en True y el bucle termina.
Por último, la función devuelve el valor del contador, que representa la cantidad de dígitos en el número ingresado.
En el programa principal, se solicita al usuario que ingrese un número entero, luego se llama a la función contar_digitos 
pasando el número ingresado como argumento y se imprime la cantidad de dígitos que tiene ese número en la pantalla.
"""

def contar_digitos(numero:int)->int:
    contador = 0
    terminar = False
    
    while terminar == False:
        if numero == 0:
            terminar = True
            
        else:
            contador += 1
            numero //= 10
            
    return contador

num = int(input("Ingrese un numero entero: "))
digitos = contar_digitos(num)
print("La cantidad de digitos del numero es",digitos)


                
