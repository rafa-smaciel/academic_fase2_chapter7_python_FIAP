#Verificar se os batimentos cardiacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso o script deva verificar e exibir uma mensagem informando se os batimentos do usuario encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada, de acordo com o site Tua Saude (HTTPS://WWW.TUASAUDE.COM/FREQUENCIA-CARDIACA/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm.);

#IDADE BPM
#Até 2 anos 120 a 140
#De 8 anos até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos 50 a 60

print("Verificar de Sáude Cardiaca")

idade_usuario = int(input("Informe sua idade: "))
batimentos_por_minuto = int(input("Informe BPM: "))

if idade_usuario < 2:
    if batimentos_por_minuto >= 120 and batimentos_por_minuto <= 140:
        print("Usuário saudavel!")
    else:print("Batimentos anormais")
elif idade_usuario > 8 and idade_usuario <= 17:
    if batimentos_por_minuto >= 80 and batimentos_por_minuto <=100:
        print("Usuario saudavel!")
    else:print("Batimentos anormais")
elif idade_usuario > 17 and idade_usuario <= 60:
    if batimentos_por_minuto >= 70 and batimentos_por_minuto <= 80:
        print("Adulto saudavel!")
    else:print("Batimentos anormais")
elif idade_usuario > 60:
    if batimentos_por_minuto > 50 and batimentos_por_minuto <= 60:
        print("Idoso saudavel!")
    else:print("Batimentos anormais")
else:print("Não foi possivel verificar os batimentos para essa idade")