class Error(Exception):
    pass


class CongruenciaIncorrecta(Error):
    pass


class Cero(Error):
    pass


clase = 5


while True:
    try:
        numero = int(input("Adivine con qué congruencia mod n se está trabajando, ingrese un número: "))
        suma = numero+numero
        if numero != 5 and numero != 0:
            raise CongruenciaIncorrecta
        elif numero == 0:
            raise Cero
        break

    except CongruenciaIncorrecta:
        print("La congruencia es incorrecta, intente de nuevo.")
        print(f"Aquí una pista:  {numero} + {numero}=", suma % clase)
        print()

    except Cero:
        print("El número ingresado debe ser distinto de cero.")
        print()

print("Felicidades, adivinó la congruencia.")
