# Lenguaje interpretado, no compila el codigo a binario
# Menos eficiente ya que al tener que interpretar el codigo es menos rapido
# Facil de programar, muchas librerias (librerias son: funcionalidades dessarolladas por otras personas en el mundo que han compartido de manera open source para su uso), ahorra tiempo de programacion

# Sintaxis Python:

# en la programacion de lenguajes de bajo nivel (C, C++, Java, PHP) se terminan las instrucciones con ; en python NO
print("Hello world") # Esto es una instruccion

# Python entiende el orden del codigo por el sangrado, es decir, por el numero de tabulaciones antes de la instruccion

if True:
    print("Esta instruccion esta tabulada 1 vez ya que se encuentra dento de un condicional")

if False:
    pass
print("Esta instruccion no esta tabulada, se ejecutara independientemente de si el condicional (if) era o no era True")

# Python usa para las operaciones definidas de condicion, bucle, etc los : en vez de los claudators tradicionales {}

#Ejemplo en C:

# if(True) {
#   println("Hello there");
# }

# En Python:
if(True):
    print("Hello there")


#--------------------------------------------------------------------------------------------#

# Declarando variables y definiendolas
# Declarar = crear una variable vacia, Definir = darle un valor a una variable

# Quiero declarar una variable que se llame miVariable

#miVariable  # Si te pones encima con el raton ves que esta subrayada en amarillo y dice que no esta definida.

# Definimos la variable como un numero

miVariable = 3
print(miVariable)
# En python las variables pueden ser de cualquier tipo de datos (integer, float, double, string)

# Definimos la variable como string
# p.d: string = conjunto de caracteres

miVariable = "Ahora soy un string"

print(miVariable)