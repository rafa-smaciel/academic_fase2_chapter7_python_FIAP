#2 - Viajar é bom demais! Uma agência de viagens está propondo uma estratégia pra alavancar as vendas após os impactos da pandemia do coronavirus.
#A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência.
#Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no vôo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e clacule os descontos de acordo com a tabela abaixo:

#Categoria descontos
#Econômica 2 viajantes 3%
#          3 viajantes 4%
#          4 viajentes ou mais 5%
#Executiva 2 viajentes 5%
#          3 viajentes 7%
#          4 viajantes ou mais 8%
#Primeira classe   2 viajantes 10%
#                  3 viajantes 15%
#                  4 viajantes ou mais 20%

#O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DO DESCONTO, o VALOR LÍQUIDO DA VIAJEM (valor bruto menos os descontos) e o VALOR MEDIO POR VIAJANTE.

print("VIAJAR É BOM DEMAIS!")
categoria = int(input("Digite sua categoria: 1- Econômica, 2- Executiva ou 3- Primeira Classe: " ))
qtd_viajantes = int(input("Informe a quantidade de viajantes: "))
valor_bruto_viajem = float(input("Informe o valor bruto da viajem: "))


if categoria == 1 and qtd_viajantes == 2:
    valor_desconto = valor_bruto_viajem * 0.03
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}")
elif categoria == 1 and qtd_viajantes == 3:
    valor_desconto = valor_bruto_viajem * 0.04
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}")
elif categoria == 1 and qtd_viajantes >= 4:
    valor_desconto = valor_bruto_viajem * 0.05
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}")  
elif categoria == 2 and qtd_viajantes == 2:
    valor_desconto = valor_bruto_viajem * 0.05
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}") 
elif categoria == 2 and qtd_viajantes == 3:
    valor_desconto = valor_bruto_viajem * 0.07
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}") 
elif categoria == 2 and qtd_viajantes >= 4:
    valor_desconto = valor_bruto_viajem * 0.08
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}") 
elif categoria == 3 and qtd_viajantes == 2:
    valor_desconto = valor_bruto_viajem * 0.10
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}") 
elif categoria == 3 and qtd_viajantes == 3:
    valor_desconto = valor_bruto_viajem * 0.15
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}") 
elif categoria == 3 and qtd_viajantes >= 4:
    valor_desconto = valor_bruto_viajem * 0.20
    valor_liquido_viajem = valor_bruto_viajem - valor_desconto
    valor_medio_viajante =  valor_liquido_viajem / qtd_viajantes
    print(f"O valor bruto da viajem é de R$: {valor_bruto_viajem}")
    print(f"O valor do desconto sera de R$: {valor_desconto}")
    print(f"O valor liquido da viajem é de R$: {valor_liquido_viajem}")
    print(f"O valor médio por viajante sera de R$: {valor_medio_viajante}") 
else:print("Não possui descontos!")