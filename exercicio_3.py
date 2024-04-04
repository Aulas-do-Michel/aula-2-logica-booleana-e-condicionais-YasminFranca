"""
#### Exercício 3 - Identificar se a variante está no gene BRCA1 - Versão 2.

Receba 3 inputs do usuário:
1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
2) A posição dessa variante. Será um número inteiro.
3) O genoma de referência dessa variante. Considere só 2 opções possíveis, "hg19" e "hg38".

Responda:
"Sim" se ela estiver no BRCA1.
"Não" se ela não estiver.

Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e:
1) Se a posição estiver no intevalo de 41196312 a 41277500, caso o genoma de referência seja o "hg19".
2) Se a posição estiver no intevalo de 43044295 a 43125483, caso o genoma de referência seja o "hg38".

Obs: Tirei a Location daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:41196312-41277500

Exemplos:

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Digite o genoma de referência: hg38

Resposta:
Não

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Digite o genoma de referência: hg19

Resposta:
Sim

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 43044299
Digite o genoma de referência: hg38

Resposta:
Sim

----------------------------------

Digite o cromossomo: chr2
Digite a posição: 43044299
Digite o genoma de referência: hg38

Resposta:
Não

"""

#Objetivo: "Identificar se a variante está no gene BRCA1".

#Primeiro passo
#Receber um input do cromossomo de uma variante.

cromossomo = input("Digite o cromossomo: ")

#Segundo passo
#Receber um input da posição da variante. NÚMERO INTEIRO.

posicao = int(input("Digite uma posição: "))

#Terceiro passo
#O genoma de referência dessa variante
#ATENÇÃO: só 2 opções possíveis, "hg19" e "hg38".

genomareferencia = input("Digite o Genoma de referência: ")

#Dessa forma:
#A variante estará no gene BRCA1 se estiver no cromossomo 17 (chr17).

geneBRCA1 = cromossomo == "chr17"

#E se a posição estiver no INTERVALO de 41196312 a 41277500 para hg19.

posicaohg19 = (posicao >=41196312) and (posicao <=41277500)

#E se a posição estiver no INTERVALO de 43044295 a 43125483 para hg38.

posicaohg38 = (posicao >=43044295) and (posicao <=43125483)


#Quarto passo:
#"Sim" se estiver no gene BRCA1.
#"Não" se ela não estiver no gene BRCA1.

if geneBRCA1 and posicaohg19 and genomareferencia == "hg19":
    print("Sim")
elif geneBRCA1 and posicaohg38 and genomareferencia == "hg38":
    print("Sim")
else:
    print("Não")
