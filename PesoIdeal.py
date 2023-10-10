def calcular_peso_ideal(altura, sexo):
    if sexo == "homem":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "mulher":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        peso_ideal = None 
    return peso_ideal
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (homem ou mulher): ").lower()
peso_ideal = calcular_peso_ideal(altura, sexo)
if peso_ideal is not None:
    print(f"O peso ideal para uma pessoa de {altura:.2f} metros de altura e sexo {sexo} é {peso_ideal:.2f} kg.")
else:
    print("Sexo não reconhecido. Certifique-se de digitar 'homem' ou 'mulher'.")