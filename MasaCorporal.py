peso, altura = map(float,input(" Ingrese su peso y su estatura ").split())

imc = peso/(altura **2)

if imc < 18.5:
    print(f"IMC de {round(imc,2)}: Peso inferior a lo normal")

if  imc > 18.5 and imc < 24.9:
    print(f"IMC de {round(imc,2)}: Peso normal") 

if  imc > 25.0 and imc < 29.9:
    print(f"IMC de {round(imc,2)}: Peso superior al normal")

elif imc > 30.0:
    print (f"IMC de {round(imc,2)}:  Estas en sobrepeso")   