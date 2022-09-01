import sys    
import cmath as c
import math as m

if __name__ == "__main__":  

    op = sys.argv[1]
    t = sys.argv[2]
    x = sys.argv[3]
    y = sys.argv[4] if len(sys.argv) >= 5 else 0

    # La variable 'op' indica la operación (de las 8 posibles).
    # La variable 't' indica el tipo de variable (número entero, decimal o complejo).
    # La variable 'x' corresponde al primer operando.
    # La variable 'y' corresponde al segundo operando.
    # Su valor se especificará a la hora de ejecutar el programa.

    op = int(op)         # Transformo las variables 'op' y 't' en números entero.
    t = int(t)

    if t == 1: 
        x = int(x)       # Si t=1, transforma las variables 'x' e 'y' en números enteros.
        y = int(y)

    elif t == 2: 
        x = float(x)     # Si t=2, transformo las variables 'x' e 'y' en números decimales.
        y = float(y)

    elif t == 3: 
        x = complex(x)   # Si t=3, transformo las variables 'x' e 'y' en números complejos.
        y = complex(y) 

    else:
        print ("ERROR")  # Para otro valor de 't', se imprime ERROR por pantalla (tipo de dato no existe).
        exit (-1)        # Establezco una salida del programa mediante el método exit.

    if op == 1:          # Si op=1 el programa realiza la suma de 'x' e 'y'.
        s = x + y        # Defino la variable 's' como la suma de 'x' más 'y'.

    elif op == 2:        # Si op=2, el programa realiza la resta de 'x' e 'y'.
        s = x - y        # Defino la variable 's' como la resta de 'x' menos 'y'.

    elif op == 3:        # Si op=3, el programa realiza el producto de 'x' e 'y'.
        s = x * y        # Defino la variable 's' como el producto de 'x' por 'y'.

    elif op == 4:        # Si op=4, el programa realiza el cociente de 'x' entre 'y'.
        s = x / y        # Defino la variable 's' como el cociente de 'x' entre 'y'.

    elif op == 5:              # Si op=5, el programa calcula el valor absoluto de 'x'.
        if  t == 3:         
            print ("ERROR")    # Si trabajo con complejos, imprime ERROR por pantalla (operación no permitida).
            exit (-2)          # Establezco una salida del programa mediante el método exit.
        elif x < 0:         
            s = -1 * x         # Si 'x' es menor que 0, la variable 's' será el producto de -1 por 'x'.
        else: 
            s = x              # Si 'x' es mayor que 0, la variable 's' será igual a la variable 'x'.
       

    elif op == 6:              # Si op=6, el programa calcula el módulo de 'x' entre 'y'.
        if t == 3:          
            print ("ERROR")    # Si trabajo con complejos, imprime ERROR por pantalla (operación no permitida).
            exit (-2)          # Establezco una salida del programa mediante el método exit.
        else: 
            s = x % y          # Defino la variable 's' como el módulo de 'x' entre 'y'.

    elif op == 7:              # Si op=7, el programa calcula la potencia 'x' elevado a 'y'.
        if t == 3:          
            print ("ERROR")    # Si trabajo con complejos, imprime ERROR por pantalla (operación no permitida).
            exit (-2)          # Establezco una salida del programa mediante el método exit.
        else: 
            s = m.pow (x,y) # Defino la variable 's' como 'x' elevado a 'y'.

    elif op == 8:                      # Si op=8, el programa calcula la raíz cuadrada de 'x'.
        if t == 1:
            r1 = m.sqrt(x)          # Defino las dos raíces, positiva y negativa.
            r2 = -1 * r1                     
            print (int(r1),int(r2))    # Transformo las dos raíces a números enteros. Imprimo las dos raíces.
            exit (0)                   # Establezco una salida del programa mediante el método exit (sin errores).
        elif t == 2:    
            r1 = m.sqrt(x)          # Defino las dos raíces, positiva y negativa.
            r2 = -1 * r1       
            print (r1, r2)             # Imprimo las dos raíces
            exit (0)                   # Establezco una salida del programa mediante el método exit (sin errores).
        elif t == 3:
            r1 = c.sqrt(x) # Defino las dos raíces, positiva y negativa.
            r2 = -1 * r1 
            print (r1, r2)     # Imprimo las dos raíces.
            exit (0)           # Establezco una salida del programa mediante el método exit (sin errores).
        
    else: 
        print ("ERROR")    # Imprime ERROR por pantalla (operación no existe).
        exit (-3)          # Establezco otra salida del programa mediante el método exit.

    if t == 1:  
        s=int(s)           # Si se ha operado con enteros, transformo 's' en número entero y la imprimopor pantalla.
    
    print (s)              # Si se ha operado con números decimales o complejos, imprimo 's'.
    exit (0)               # Establezco una salida del programa mediante el método exit  (sin errores).

