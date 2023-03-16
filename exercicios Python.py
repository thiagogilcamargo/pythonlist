#EXERCICIOS


#1. Instale o Python 3.0 no seu computador.

#2.Escreva um algoritmo em Python que recebe seu nome e sobrenome, depois de ler as informações mostra na tela o sobrenome e depois o nome.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(sobrenome, nome)


 
# 3.Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu
# algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim
# de 2022. Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu
# programa deverá imprimir:

#Fulano de tal tem (ou terá) 34 anos.

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2022 - ano_nascimento
print(nome, "tem (ou terá)", idade, "anos")



#4.. Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
# dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = a + b
multiplicacao = a * b
divisao_inteira = a // b
resto_divisao_inteira = a % b
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
print("Divisão inteira:", divisao_inteira)
print("Resto da divisão inteira:", resto_divisao_inteira)



#5.Escreva um algoritmo que recebe um número x e y e imprime x elevado a y. Lembre-se que ∗∗ representa a potência entre dois números em Python.

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
resultado = x ** y
print(resultado)



#6.Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π.

raio = float(input("Digite o raio do círculo: "))
pi = 3.141592
area = pi * raio ** 2
perimetro = 2 * pi * raio
print("Área:", area)
print("Perímetro:", perimetro)



#7.Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
#dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
#divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

numero = int(input("Digite um número de 0 a 99: "))
dezena = numero // 10
unidade = numero % 10
print("Dígito das dezenas:", dezena)
print("Dígito das unidades:", unidade)



#8.Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
# um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
# deverá ler o número de camisas, o número de calças e o número de pares de sapato.

camisas = int(input("Digite o número de camisas: "))
calcas = int(input("Digite o número de calças: "))
sapatos = int(input("Digite o número de pares de sapato: "))
combinacoes = camisas * calcas * sapatos
print("Número de combinações possíveis:", combinacoes)



#9.Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
# e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
# de um desconto, fosse um aumento. O que muda no seu algoritmo?

preco = float(input("Digite o preço do produto: "))
percentual = float(input("Digite o percentual de desconto (positivo) ou aumento (negativo): "))

valor_desconto = preco * (percentual/100)
novo_preco = preco - valor_desconto

print("Valor do desconto: R$", valor_desconto)
print("Novo preço do produto: R$", novo_preco)
Para calcular um aumento, basta mudar a linha que calcula o valor do desconto para:


valor_aumento = preco * (percentual/100)
novo_preco = preco + valor_aumento
E mudar o texto que exibe o resultado para "Valor do aumento" e "Novo preço do produto".


#10.Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
# Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
# seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.

distancia = float(input("Digite a distância percorrida em metros: "))
tempo = float(input("Digite o tempo em segundos: "))

velocidade_ms = distancia / tempo
velocidade_km_h = (distancia / 1000) / (tempo / 3600)

print(f"Velocidade média em m/s: {velocidade_ms:.2f} m/s")
print(f"Velocidade média em km/h: {velocidade_km_h:.2f} km/h")


#11.Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual
# de aumento. Você deverá escrever um algoritmo que recebe 2 números reais representando
# os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
# João obteve.

salario_anterior = float(input("Digite o salário anterior: "))
salario_atual = float(input("Digite o salário atual: "))

percentual_aumento = (salario_atual - salario_anterior) / salario_anterior * 100

print(f"Percentual de aumento: {percentual_aumento:.2f}%")



#12.O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
#recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
#o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5.
#Dica: realize várias divisões e restos de divisões por 10.

rm = int(input("Digite o RM do aluno: "))

soma_digitos = 0
while rm > 0:
    soma_digitos += rm % 10
    rm //= 10

print(f"A soma dos dígitos do RM é: {soma_digitos}")


#13.Uma disciplina da faculdade possui 3 tipos de avaliações: NAC, AM e PS. A média da
# disciplina é calculada de forma ponderada, onde a NAC tem peso 2, o AM peso 3 e a PS
# peso 5. Escreva um algoritmo que calcula a média da disciplina, seu algoritmo deverá receber
# as três notas (NAC, AM e PS) e deverá imprimir o valor da média.

# MEDIA = (2 ∗ NAC + 3 ∗ AM + 5 ∗ P S)/10

nac = float(input("Digite a nota da NAC: "))
am = float(input("Digite a nota do AM: "))
ps = float(input("Digite a nota da PS: "))

media = (2 * nac + 3 * am + 5 * ps) / 10

print(f"Média da disciplina: {media:.2f}")



#14.As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
#à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
#informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
#desconto em percentual dado pela prefeitura para pagamento à vista.

valor_total = float(input("Digite o valor total do IPTU: "))
valor_parcela = float(input("Digite o valor de cada parcela: "))

valor_desconto = valor_total * 0.1
valor_total_desconto = valor_total - valor_desconto
numero_parcelas = int(valor_total_desconto / valor_parcela)

print(f"Valor do desconto para pagamento à vista: R$ {valor_desconto:.2f}")
print(f"Total com desconto: R$ {valor_total_desconto:.2f}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
print(f"Número de parcelas: {numero_parcelas}")
