"""
#### Exercício 2 - Conversor de moeda

Você é uma casa de câmbio, recebe dinheiro em reais e transforma na moeda da viagem do usuário.

Você tem em caixa dólares, pesos argentinos e ienes.

Pergunte para o usuário para onde ele vai viajar:

Se ele falar "Estados Unidos", "Argentina" ou "Japão", faça o seguinte processo:
    Pergunte quantos reais ele vai converter. Receba o valor em float.
    Converta o valor para a moeda do país.
    Responda com o valor da moeda e em seguida o tipo da moeda (USD, ARS, ou JPY).

Se ele falar qualquer outra coisa, responda "Não temos essa moeda em caixa.".

Utilize as seguintes conversões:
5 reais = 1 USD
1 real = 180 ARS
1 real = 30 JPY

Obs:
Nos testes, vou tentar ignorar caso haja apenas uma diferença no número de casas decimais nas respostas.
Porém, se você quiser garantir que você imprima com exatamente 2 casas decimais você pode usar a seguinte sintaxe: f"{sua_variavel:.2f}".

Exemplo:
valor_em_dolares = 23.333333
print(f"{valor_em_dolares:.2f} USD")
>>> 23.33 USD

Mais informações sobre formatação de strings: https://realpython.com/python-f-strings/#interpolating-values-and-objects-in-f-strings

-------------------------------------------
Exemplos:

Qual país você vai viajar? Estados Unidos
Quantos reais você quer converter? 100

Resposta:
20.00 USD

-------------------------------------------
Qual país você vai viajar? Argentina
Quantos reais você quer converter? 100

Resposta:
18000.00 ARS

-------------------------------------------
Qual país você vai viajar? China

Resposta:
Não temos essa moeda em caixa.
"""

pais = input("Qual país você vai viajar? ")
USA = (pais == "Estados Unidos")
ARG = (pais == "Argentina")
JPN = (pais == "Japão") 
if USA:
    convertervalor = float(input("Quantos reais você quer converter? "))
    valordolares = float(convertervalor / 5)
    print(f"{valordolares:.2f} USD")
elif ARG:
    convertervalor = float(input("Quantos reais você quer converter? "))
    valorpesos = float(convertervalor * 180)
    print(f"{valorpesos:.2f} ARS")
elif JPN:
    convertervalor = float(input("Quantos reais você quer converter? "))
    valorienes = float(convertervalor * 30)
    print(f"{valorienes:.2f} JPY")
else:
    print("Não temos essa moeda em caixa.")
