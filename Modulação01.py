# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.

# Faça um Programa que peça dois números e imprima o maior deles.

def imprimir_maior_numero(): #1
    numero1 = input("Digite o primeiro número: ")

    numero2 = input("Digite o segundo número: ")

    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        if numero1 > numero2:
            print("O número", numero1, "é maior que o número", numero2)
        elif numero1 == numero2:
            print("Os números são iguais")
        else:
            print("O número", numero2, "é maior que o número", numero1)
    except Exception:
        print("Você não digitou um número válido")
        exit()


def verificar_valor_positivo(): #2
    # Faça um Programa que peça um valor e mostre na tela se o valor é positivo 
    # ou negativo.

    valor = int(input("Digite um valor: "))

    if valor > 0:
        print("O valor é positivo")
    elif valor == 0:
        print("O valor é neutro")
    else:
        print("O valor é negativo")
        
def verificar_feminino_maculino(): #3
    #Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

    sexo = input("Digite seu sexo [F, M]: ")
    if sexo == 'F' or sexo == 'f': 
        print("Seu sexo é Feminino")
    elif sexo == 'M' or sexo == 'm': 
        print("Seu sexo é Masculino")
    else: print("Sexo Inválido")
               
def vogal_ou_consoante(): #4
    #Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    letra = input("Digite uma letra: ")
    vogais = ['a', 'e', 'i', 'o', 'u']

    if letra in vogais: print('VOGAL')
    else: print('CONSOANTE')      

def calcular_Aprovado(): #5
#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 7 and media < 10: print("APROVADO")
    elif media < 7: print("REPROVADO")
    else: print("APROVADO com DISTINÇÃO")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 7 and media < 10: print("APROVADO")
    elif media < 7: print("REPROVADO")
    else: print("APROVADO com DISTINÇÃO")      

def Ler_tres_numeros_maior(): #6
     #Faça um Programa que leia três números e mostre o maior deles.

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    valores = [valor1, valor2, valor3]

    print(f'O maior número é {max(valores)}')

def ler_tres_numeros_menor(): #7
     #Faça um Programa que leia três números e mostre o maior e o menor deles.

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    lista = [valor1, valor2, valor3]

    print("Menor valor: ", min(lista), "\nMenor valor: ", max(lista))

def menor_preço(): #8
    #Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

    preco1 = float(input("Digite o primeiro preço: "))
    preco2 = float(input("Digite o segundo preço: "))
    preco3 = float(input("Digite o terceiro preço: "))

    lista = [preco1, preco2, preco3]

    print("O produto que deve ser comprado é o que custa ", min(lista)) 

def numero_decrescente():   #9 
    #Faça um Programa que leia três números e mostre-os em ordem decrescente.

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    lista = [n1, n2, n3]

    lista.sort(key=float, reverse=True)

    print("decrescente: ", lista)    

def turno_dia_noite_tarde(): #10
    #Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


    horario = input("Digite [M, V, N]: ").upper()

    if horario == 'M': print("Bom Dia")
    elif horario == 'V': print("Boa Tarde")
    elif horario == 'N': print("Boa Noite")
    else: print("Valor Inválido")  

def salario_atual_colaborador(): #11
    # Solicita o salário atual do colaborador
    salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

    # Calcula o percentual de aumento com base no salário atual
    if salario_atual <= 280.00:
        percentual_aumento = 20
    elif salario_atual <= 700.00:
        percentual_aumento = 15
    elif salario_atual <= 1500.00:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    # Calcula o valor do aumento
    valor_aumento = (salario_atual * percentual_aumento) / 100

    # Calcula o novo salário após o aumento
    novo_salario = salario_atual + valor_aumento

    # Exibe as informações
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")     

def calculadora_impostos(): #12
    # Solicita o valor da hora e a quantidade de horas trabalhadas ao usuário
    valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

    # Calcula o salário bruto
    salario_bruto = valor_hora * horas_trabalhadas

    # Calcula o desconto do Imposto de Renda
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        desconto_ir = salario_bruto * 0.10
    else:
        desconto_ir = salario_bruto * 0.20

    # Calcula o desconto do INSS
    desconto_inss = salario_bruto * 0.10

    # Calcula o FGTS
    fgts = salario_bruto * 0.11

    # Calcula o total de descontos
    total_descontos = desconto_ir + desconto_inss

    # Calcula o salário líquido
    salario_liquido = salario_bruto - total_descontos

    # Exibe as informações
    print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas})        : R$ {salario_bruto:.2f}")
    print(f"(-) IR ({'5%' if salario_bruto <= 1500 else '10%' if salario_bruto <= 2500 else '20%'})                     : R$ {desconto_ir:.2f}")
    print(f"(-) INSS (10%)                 : R$ {desconto_inss:.2f}")
    print(f"FGTS (11%)                      : R$ {fgts:.2f}")
    print(f"Total de descontos              : R$ {total_descontos:.2f}")
    print(f"Salário Líquido                 : R$ {salario_liquido:.2f}")    

def dia_semana(): #13
      #Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

    dia = int(input("Digite um número de 1 a 7: "))

    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sababo")
    else:
        print("Valor Inválido")

def aprovacao_EUA(): #14

#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


    nota1 = float(input("Digite a nota1"))
    nota2 = float(input("Digite a nota2"))
    media = (nota1 + nota2) / 2

    if media >= 0 and media <= 4:
        print("E")
    elif media > 4 and media <= 6:
        print("D")
    elif media > 6 and media <= 7.5:
        print("C")
    elif media > 7.5 and media <= 9:
        print("B")
    else:
        print("A")

def triangulo(): #15

    #Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    #Dicas:
    #Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    #Triângulo Equilátero: três lados iguais;
    #Triângulo Isósceles: quaisquer dois lados iguais;
    #Triângulo Escaleno: três lados diferentes;


    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))

    if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
        print("É UM TRINGULO")
        if lado1 == lado2 and lado1 == lado3:
            print("Equilatero")
        elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
            print("Isóceles")
        else:
            print("Escaleno")
    else:
        print("Não é um TRINGULO")

def raizez_segundo_Grau(): #16

#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


    import math
    a = float(input("Digite A: "))
    if a == 0:
        print("Valor Invalido")
    else:
        b = float(input("Digite B: "))
        c = float(input("Digite C: "))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
            print("A equação não possui raizes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
    if delta == 0:
            print("1 Raiz real: ", x1)
    else:
            print("2 raizes reais, x1: ", x1, "\nx2: ", x2)       

def verificardata(): #17
 
#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


   
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


    data = input("Digite a data no seguinte modelo: [11/07/2002] :")
    if len(data) != 10:
        print("ERRADO")
    else:
        if data[2] != '/' or data[5] != '/':
            print("ERRADO")
        else:
            numeros_data = data.split('/')
            if int(numeros_data[0]) > 31:
                print("ERRADO")
            elif int(numeros_data[1]) > 12:
                print("ERRADO")
            else:
                print("CERTO")   

def numerointeiromenorque100(): #18
    # Solicita ao usuário um número inteiro menor que 1000
    numero = int(input("Digite um número inteiro menor que 1000: "))

    # Verifica se o número está dentro do intervalo permitido
    if numero < 0 or numero >= 1000:
        print("Número fora do intervalo permitido.")
    else:
        # Calcula as centenas, dezenas e unidades
        centenas = numero // 100
        dezenas = (numero % 100) // 10
        unidades = numero % 10

        # Cria as strings para os termos no plural, se necessário
        str_centenas = f"{centenas} centena{'s' if centenas > 1 else ''}"
        str_dezenas = f"{dezenas} dezena{'s' if dezenas > 1 else ''}"
        str_unidades = f"{unidades} unidade{'s' if unidades > 1 else ''}"

        # Constrói a mensagem final
        mensagem = ""

        if centenas > 0:
            mensagem += str_centenas

        if dezenas > 0:
            if centenas > 0:
                if unidades > 0:
                    mensagem += ", "
                else:
                    mensagem += " e "
            mensagem += str_dezenas

        if unidades > 0:
            if centenas > 0 or dezenas > 0:
                mensagem += " e "
            mensagem += str_unidades

        print(f"{numero} = {mensagem}")                       


def centenasdezenasetc(): #19
   
#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


    import math
    numero = int(input("Digite um número menor ou igual a 1000: "))
    if numero <= 1000:
        centena = numero / 100
        centena2 = math.floor(float(centena))
        resto_centena = centena - centena2
        resto_multiplicado = resto_centena * 100

        dezena = resto_multiplicado / 10
        dezena2 = math.floor(float(dezena))
        unidade = dezena - dezena2
        unidade_certo = unidade * 10

        print("Centena(s): ", centena2)
        print("dezena(s): ", dezena2)
        print("Unidade(s): ", round(unidade_certo))

    else:
        print("VOCÊ DIGITOU UM NÚMERO MAIOR QUE 1000")

def calcularmedia(): #20

#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

# NA LISTA O EXERCÍCIO 5 E O 20 SÃO O MESMO

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 7 and media < 10:
        print("APROVADO")
    elif media < 7:
        print("REPROVADO")
    else:
        print("APROVADO com DISTINÇÃO")       

def troco_atm():


#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


    import math
    saque = int(input("Valor para sacar: "))
    nota100 = saque / 100
    nota100_certo = math.floor(nota100)
    resto_nota_100 = (nota100 - nota100_certo) * 100

    nota50 = resto_nota_100 / 50
    nota50_certo = math.floor(nota50)
    resto_nota_50 = (nota50 - nota50_certo) * 50

    nota10 = resto_nota_50 / 10
    nota10_certo = math.floor(nota10)
    resto_nota_10 = (nota10 - nota10_certo) * 10

    nota5 = resto_nota_10 / 5
    nota5_certo = math.floor(nota5)
    nota1 = (nota5 - nota5_certo) * 5

    print("Notas 100: ", nota100_certo, "\nNotas50: ", nota50_certo, "\nNota 10: ", nota10_certo, "\nNota 1: ", round(nota1))



def parouimpar():

    
    #Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
    

    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número Impar")

def decimal():
   
#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.


    numero = float(input("Digite um número: "))

    if(numero // 1 == numero):
        print("numero inteiro")
    else:
        print("Numero Decimal")



def parouimpar2():

#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.


    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))
    operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")


    def checar():
        if (resultado_operacao // 1 == resultado_operacao):
            print("Inteiro")
            if resultado_operacao % 2 == 0:
                print("Par")
                if resultado_operacao > 0:
                    print("Positivo")
                else:
                    print("Negativo")
            else:
                print("Impar")
        else:
            print("Decimal")


    if operacao == '+':
        resultado_operacao = numero1 + numero2
        print("Resultado: ", resultado_operacao)
        checar()
    elif operacao == '-':
        resultado_operacao = numero1 - numero2
        print("Resultado: ", resultado_operacao)
        checar()
    elif operacao == '/':
        resultado_operacao = numero1 / numero2
        print("Resultado: ", resultado_operacao)
        checar()
    elif operacao == '*':
        resultado_operacao = numero1 * numero2
        print("Resultado: ", resultado_operacao)
        checar()
    else:
        print("Valor Invalido")

def socorro():


#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

    perguntas = [
        "Telefonou para a vítima?: ",
        "Esteve no local do crime?: ",
        "Mora perto da vítima?: ",
        "Devia para a vítima?: ",
        "Já trabalhou com a vítima?: "
    ]
    resposta = 0

    for status in perguntas:
        resposta += (input(status) == "sim")

    if resposta == 5:
        print("Assassino")

    elif resposta >= 3:
        print("Cúmplice")

    elif resposta == 2:
        print("Suspeito")

    else:
        print("Inocente")



def descontoposto():
 

#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


    litros = int(input("Digite a quantidade de litros: "))
    combustivel = input("Digite o tipo do combustivel [G, A]: ")

    preco_alcool1 = (1.90 * 0.03)
    preco_alcool2 = (1.90 * 0.05)
    preco_gasolina1 = (2.50 * 0.04)
    preco_gasolina2 = (2.50 * 0.06)

    print("Litros Vendidos: ", litros)

    if combustivel == 'a' or combustivel == 'A':
        print("Combustivel: alcool")
        if litros <= 20:
            desconto = (1.90 - preco_alcool1) * litros
            print("Preço: ", desconto)
        else:
            desconto = (1.90 - preco_alcool2) * litros
            print("Preço: ", desconto)
    elif combustivel == 'g' or combustivel == 'G':
        print("Combustivel: gasolina")
        if litros <= 20:
            desconto = (2.50 - preco_gasolina1) * litros
            print("Preço: ", desconto)
        else:
            desconto = (2.50 - preco_gasolina2) * litros
            print("Preço: ", desconto)
    else:
        print("Valor Invalido")

def morangosemaca():

    # Solicita a quantidade de morangos e maçãs ao usuário
    quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
    quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

    # Calcula o preço dos morangos de acordo com a quantidade
    if quantidade_morangos <= 5:
        preco_morangos = 2.50
    else:
        preco_morangos = 2.20

    # Calcula o preço das maçãs de acordo com a quantidade
    if quantidade_macas <= 5:
        preco_macas = 1.80
    else:
        preco_macas = 1.50

    # Calcula o valor total da compra
    valor_total = (quantidade_morangos * preco_morangos) + (quantidade_macas * preco_macas)

    # Verifica se o cliente recebe o desconto
    if quantidade_morangos + quantidade_macas > 8 or valor_total > 25.00:
        desconto = valor_total * 0.10
    else:
        desconto = 0

    # Calcula o valor a ser pago pelo cliente
    valor_a_pagar = valor_total - desconto

    # Exibe o valor a ser pago
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")

def descontocarne():

    # Solicita o tipo de carne e a quantidade ao usuário
    tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
    quantidade = float(input("Digite a quantidade em Kg: "))

    # Verifica o preço de acordo com a quantidade
    if quantidade <= 5:
        if tipo_carne == "File Duplo":
            preco_por_kg = 4.90
        elif tipo_carne == "Alcatra":
            preco_por_kg = 5.90
        elif tipo_carne == "Picanha":
            preco_por_kg = 6.90
        else:
            print("Tipo de carne inválido.")
            exit()
    else:
        if tipo_carne == "File Duplo":
            preco_por_kg = 5.80
        elif tipo_carne == "Alcatra":
            preco_por_kg = 6.80
        elif tipo_carne == "Picanha":
            preco_por_kg = 7.80
        else:
            print("Tipo de carne inválido.")
            exit()

    # Calcula o valor da compra
    valor_total = quantidade * preco_por_kg

    # Verifica se a compra será feita no cartão Tabajara
    cartao_tabajara = input("A compra será feita no cartão Tabajara? (S/N): ").strip().lower()
    if cartao_tabajara == "s":
        desconto = valor_total * 0.05
    else:
        desconto = 0

    # Calcula o valor a pagar
    valor_a_pagar = valor_total - desconto

    # Exibe o cupom fiscal
    print("\nCUPOM FISCAL")
    print(f"Tipo de carne: {tipo_carne}")
    print(f"Quantidade: {quantidade} Kg")
    print(f"Preço por Kg: R$ {preco_por_kg:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Tipo de pagamento: {'Cartão Tabajara' if cartao_tabajara == 's' else 'Outro'}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")

# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.
def menu():
    opcao = 1  
    while opcao != 0:
        print('----Seja bem vindo ao meu Super Menu----')
        print('Escolha uma opção abaixo:')
        print('1 - Imprimir maior número')
        print('2 - Verificar se o valor é positivo ou negativo')
        print('3 - verificar si é F ou M')
        print('4 - Consoante ou vogakkkkkk')
        print('5 - Verificar aprovação')
        print('6 - Verificar entre 3 numeros, qual é o maior')
        print('7 - Verificar entre 3 numeros, qual é o menor')
        print('8 - Verificar entre 3 produtos e escolher o mais barato')
        print('9 - Veriricar  3 numeros e colocar eles em ordem decrescente ')
        print('10 - Verificação de turno ')
        print('11 - Calculadora de impostos por salario')
        print('12 - Calculadora de impostos avançada')
        print('13 - Dia da semana, de 1 a 7 ')
        print('14 - Calculadora de nota EUA ')
        print('15 - Ver se o triangulo é equilatero, isóceles ou escaleno')
        print('16 - Calcular raizes de uma equação do segundo grau ')
        print('17 - Verificar se o ano é bissexto ou não')
        print('18 - Verificar numero abaixo de 1000 ')
        print('19 - Contar centenas, dezenas abaixo do numero 1000 ')
        print('20 - Calcular media ')
        print('21 - Calcular troco ')
        print('22 - Verificar se o numero é par ou impar')
        print('23 - Verificar se o numero é inteiro ou decimal')
        print('24 - Calculo operação ')
        print('25 - 190')
        print('26 - Posto desconto')
        print('27 - Morangos e maçãs')
        print('28 - Verificar descontos em carnes ')


        opcao = int(input('Digite uma das opções ou 0 para sair:'))
        if opcao == 1:
            print('---Iniciando a função de imprimir o maior numero')
            imprimir_maior_numero()
            print('Fim da função imprimir o maior numero')

        elif opcao == 2:
            print('iniciando a verificação de valores positivos')
            verificar_valor_positivo()
            print('fim da função de verificação de valores positivos')

        elif opcao ==3:
            print('Iniciando programar F ou M!')
            verificar_feminino_maculino()
            print('Fim da decisção si é osmi ou cuie')

        elif opcao ==4:
            print("--- Inicando a função se a letra é vogal")
            vogal_ou_consoante()
            print('Fim da função')

        elif opcao ==5:
            print('Iniciando a calculadora de aprovação')
            calcular_Aprovado()
            print('fim da função calculadora de aprovação')

        elif opcao == 6:
            print('Inicando programa para ver o maior numero entre 3')
            Ler_tres_numeros_maior()
            print ("Fim da função de ver o maior numero dentro de 3")   

        elif opcao == 7:
            print('Inicando programa para ver o menor numero entre 3')   
            ler_tres_numeros_menor()
            print ('Fim da função de ver o menor numero dentro de 3')  

        elif opcao ==8:
            print('Iniciando programa para verificar o menor preço entre 3 produtos')
            menor_preço()
            print('Fim da função de escolher o produto mais barato') 

        elif opcao ==9:
            print('Iniciando programa que mostra 3 numeros em ordem decrescente')
            numero_decrescente()
            print("Fim da função de mostrar 3 numeros em ordem decrescente")

        elif opcao ==10:
            print('Iniando verificação de turno')
            turno_dia_noite_tarde()
            print(' Fim da função de verificar turno')      

        elif opcao ==11:
            print('Iniciando calculo de impostos')
            salario_atual_colaborador()
            print(' Fim do calculo de impostos')

        elif opcao ==12:
            print('Iniciando calculo de impostos avançado')
            calculadora_impostos()
            print(' Fim do calculo')

        elif opcao ==13:
            print('Inicando para ver o dia da semana')
            dia_semana()
            print ('fim')

        elif opcao ==14:
            print('Inicando calculo de notas EUA')
            aprovacao_EUA()
            print ('fim do calculo!')

        elif opcao ==15:
            print(' iniando programa para verificar o triangulo')
            triangulo()
            print ('fim!')


        elif opcao ==16:
            print('Iniando calculadora das raizes')
            raizez_segundo_Grau()
            print ('Fim do calculo das raizes!')



        elif opcao ==17:
            print ('Iniando verificação de data')
            verificardata()
            print ('Fim!')

        elif opcao ==18:
            print('Iniciando calculo')
            numerointeiromenorque100()
            print('Fim do calculo!')

        elif opcao ==19:
            print('Iniciando verification')
            centenasdezenasetc()
            print('Termino da função')



        elif opcao ==20:
            print('Inicando calculo de media')
            calcularmedia()
            print('Função concluida. Reprovou, ou não?')



        elif opcao ==21:
            print('Iniciando calculo')
            troco_atm()
            print('Fim da função')  



        elif opcao ==22:
            print('Vamos ver se é par ou impar,rsrs')
            parouimpar()
            print('Fim')


        elif opcao ==23:
            print('Inicando a função de inteiro ou decimal')
            decimal()
            print('fim')



        elif opcao ==24:
            print('Iniciando calculo')
            parouimpar2()
            print('Fim do calculo')



        elif opcao ==25:
            print('Iniciando 190')
            socorro()
            print('fim')



        elif opcao == 26:
            print('Vamos ver esses descontos')
            descontoposto()
            print('fim')
            



        elif opcao == 27:
            print('Vamos ver esses morangão i essas maçã do Eden')
            morangosemaca()
            print('fim')



        elif opcao == 28:
            print('vamos as compras')
            descontocarne()
            print('fim')
        
        else:
            print('Opção inválida')

        print('----Fim do menu ----')

# Chamar função de menu
menu()