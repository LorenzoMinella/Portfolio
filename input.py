username = input("Como te llamas? ")
numero = int(input("Dame un numero: "))
numero2 = int(input("Dame otro numero: "))


def sumar(var1,var2):
    return var1+var2

cacadevaca = sumar(numero, numero2)

print("Hola " + username + ". Tu resultado es: " + str(cacadevaca))