#EXERCICIOS

#2.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(sobrenome, nome)


 
# 3.
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2022 - ano_nascimento
print(nome, "tem (ou terá)", idade, "anos")



#4.
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



#5.
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
resultado = x ** y
print(resultado)



#6.
raio = float(input("Digite o raio do círculo: "))
pi = 3.141592
area = pi * raio ** 2
perimetro = 2 * pi * raio
print("Área:", area)
print("Perímetro:", perimetro)



#7.
numero = int(input("Digite um número de 0 a 99: "))
dezena = numero // 10
unidade = numero % 10
print("Dígito das dezenas:", dezena)
print("Dígito das unidades:", unidade)



#8.
camisas = int(input("Digite o número de camisas: "))
calcas = int(input("Digite o número de calças: "))
sapatos = int(input("Digite o número de pares de sapato: "))
combinacoes = camisas * calcas * sapatos
print("Número de combinações possíveis:", combinacoes)



#9.
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


#10.
distancia = float(input("Digite a distância percorrida em metros: "))
tempo = float(input("Digite o tempo em segundos: "))

velocidade_ms = distancia / tempo
velocidade_km_h = (distancia / 1000) / (tempo / 3600)

print(f"Velocidade média em m/s: {velocidade_ms:.2f} m/s")
print(f"Velocidade média em km/h: {velocidade_km_h:.2f} km/h")

Código em Python:

#11.
salario_anterior = float(input("Digite o salário anterior: "))
salario_atual = float(input("Digite o salário atual: "))

percentual_aumento = (salario_atual - salario_anterior) / salario_anterior * 100

print(f"Percentual de aumento: {percentual_aumento:.2f}%")

Código em Python:

#12.
rm = int(input("Digite o RM do aluno: "))

soma_digitos = 0
while rm > 0:
    soma_digitos += rm % 10
    rm //= 10

print(f"A soma dos dígitos do RM é: {soma_digitos}")


#13.
nac = float(input("Digite a nota da NAC: "))
am = float(input("Digite a nota do AM: "))
ps = float(input("Digite a nota da PS: "))

media = (2 * nac + 3 * am + 5 * ps) / 10

print(f"Média da disciplina: {media:.2f}")



#14.
valor_total = float(input("Digite o valor total do IPTU: "))
valor_parcela = float(input("Digite o valor de cada parcela: "))

valor_desconto = valor_total * 0.1
valor_total_desconto = valor_total - valor_desconto
numero_parcelas = int(valor_total_desconto / valor_parcela)

print(f"Valor do desconto para pagamento à vista: R$ {valor_desconto:.2f}")
print(f"Total com desconto: R$ {valor_total_desconto:.2f}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
print(f"Número de parcelas: {numero_parcelas}")
