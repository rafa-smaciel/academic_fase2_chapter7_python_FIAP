#Hora de dicidir! Os caloboradores da sua equipe foram sorteados para ganharem um console de úlyima geração cada um por conta do bom desempenho que tiveram nos últimos projetos. por uma questão de logistica, porém, a empresa pede que todos os 5 membros da equipe recebam o mesmo aparelho.
#Crie um algoritimo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.
#As opções são: PLAYSTATION, XBOX E NINTENDO.

print("Eleição para o console")

voto1 = input("Selecione uma opção: PLAYSTATION, XBOX ou NINTENDO")
voto2 = input("Selecione uma opção: PLAYSTATION, XBOX ou NINTENDO")
voto3 = input("Selecione uma opção: PLAYSTATION, XBOX ou NINTENDO")
voto4 = input("Selecione uma opção: PLAYSTATION, XBOX ou NINTENDO")
voto5 = input("Selecione uma opção: PLAYSTATION, XBOX ou NINTENDO")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:print("o colaborador 1 digitou dados incorretos")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:print("o colaborador 2 digitou dados incorretos")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:print("o colaborador 3 digitou dados incorretos")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:print("o colaborador 4 digitou dados incorretos")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:print("o colaborador 5 digitou dados incorretos")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido é o playstation")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o Xbox")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o nintendo")
else:print("Houve empate, favor entrar em contado com a organização")
