


# %% Exercici 1 if
print("introdueix dos nombres enters")
n1 = int(input("Primer nombre: "))
n2 = int(input("Segon nombre: "))

if n1 > n2:
    print("El primer nombre és més gran que el segon")
elif n2 > n1:
    print("El segon nombre és més gran que el primer")
else:
    print("Els dos nombres són iguals")

# %% Exercici 2 if
print("introdueix dos nombres enters")
n1 = int(input("Primer nombre: "))
n2 = int(input("Segon nombre: "))
print("introdueix una operació: +, -, *, /")
operacio = input("Operació: ")

if operacio == "+":
    resultat = n1 + n2
    print("El resultat de la suma és:", resultat)
elif operacio == "-":
    resultat = n1 - n2
    print("El resultat de la resta és:", resultat)
elif operacio == "*":
    resultat = n1 * n2
    print("El resultat de la multiplicació és:", resultat)
elif operacio == "/":
    if n2 == 0:
        print("Error: No es pot dividir entre 0.")
    else:
        resultat = n1 / n2
        print("El resultat de la divisió és:", resultat)
# %% Exercici 14 if
print("La incidencia afecta un servei crític? (si/no)")
servei_critic = input("Resposta: ")
print("Nombre d'usuaris afectats:")
num_usuaris = int(input("Resposta: "))
if num_usuaris < 0:
    print("Error: El nombre d'usuaris afectats no pot ser negatiu.")

print("Hi ha una alternativa de servei disponible? (si/no)")
alternativa_disponible = input("Resposta: ")

if (servei_critic == "sí" and alternativa_disponible == "no") or (num_usuaris >= 50 and alternativa_disponible == "no"):
         print("La incidencia amb prioritat crítica.")
elif num_usuaris > 10 or servei_critic == "sí":
        print("La incidencia amb prioritat alta.")
else:
    print("La incidencia amb prioritat baixa.")



# %% Exercici 1 Booleans

a = 8
b = 5
print(f"{a} < {b}: {a < b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")

# %% # %% Exercici 1 Booleans

a = "Hola"
b = "hola"

print(f"{a} == {b}: {a == b}")


# %% Exercici 5 Booleans

compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
accés_permes = (
    compte_actiu
    and contrasenya_correcta
    and (codi_correcte or dispositiu_de_confiança)
    and not compte_bloquejat
)
print(f"Accés permès: {accés_permes}")
# %% Exercici 6 Llistes
llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Llista original:", llista)
meitat = len(llista) // 2
llista_invertida = llista[:meitat][::-1] + llista[meitat:]
print("Llista invertida:", llista_invertida)

# %% Exercici 1 Llistes methods

llista = [1, 2, 3, 4, 5]
llista.append(6)
llista.insert(2, 10)
llista[0] = 0
print("Llista modificada:", llista)

# %% Exercici 5 Llistes methods
original = [1, 2, 3]
copia_1 = original.copy()
copia_2 = original[:]
referencia = original
referencia[0] = 10
print(original, copia_1, copia_2, referencia)
# %% Exercic bucle while 10
numero_secret = 7
prova = int(input("Prova un nombre entre: "))
while(prova != numero_secret):
    if(prova < numero_secret):
        print("el nombre és més gran")
    else:
        print("el nombre és més petit")
    prova = int(input("Prova un altre nombre: "))
print("Felicitats! Has encertat el nombre secret.")

# %% Exercici for 10
frequencies = [50, 100, 500, 1000]
for freq in frequencies:
     print(f"Freqüència: {freq} Hz")
     print(f"Període: {1/freq} s")
# %% Exercici range 6
numero = int(input("Introdueix un numero:"))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

# %% Exercici range 5
suma = 0
for i in range(1, 101):
    suma = suma + i
print(f"La suma dels nombres de 1 a 100 és: {suma}")

# %% Exercici funcions 1
print("\nExercici 1:")
def saludar_a(nom, salutacio="Hola"):
  print(f"{salutacio} {nom}!")

saludar_a("Marc")
saludar_a("Cristina", "Bon dia")

# %% Exercici funcions 2:

def es_parell(numero):
    print(f"{numero} és parell: {numero % 2 == 0}")

es_parell(4)
es_parell(7)
# %% Exercici funcions 6:
def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")

mostrar_perfil(nom="Anna", edat=19, grau="Enginyeria de Sistemes de Telecomunicació")


# %% Exercici funcions 4:
def sumar_tot(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(10, 20, 30))
print(sumar_tot(100, 200, 300, 400, 500))

# %% Exercici diccionaris 1
estudiant = {
    "nom": "Joan",
    "edat": 20,
    "assignatures": ["Matemàtiques", "Física", "Informàtica"]
}


print("assignatura 2:", estudiant["assignatures"][1])
estudiant["edat"] = 21
print("edat actualitzada:", estudiant["edat"])


estudiant["grau"] = "Enginyeria Informàtica"
del estudiant["edat"]
print("diccionari actualitzat:")
for dada, valor in estudiant.items():
    print(f"{dada}: {valor}")

# %%
