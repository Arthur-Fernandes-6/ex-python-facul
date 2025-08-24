#Q1
#  nota1 = float(input("digite a nota1: "))
# nota2 = float(input("digite a nota2: "))
# nota3 = float(input("digite a nota3: "))

# media = (nota1 + nota2 + nota3)/3

# if media > 6:
#     print("aprovado")

# elif media == 6:
#     print("FINAL")

# else:
#     print("reprovado")
#////////////////////////////////////

#Q2
# numero = int (input ("digite um numero"))

# if numero > 0:
#     print ("é positivo")

# elif numero < 0:
#    print ("é negativo")

# else:
#     print("é zero") 
#//////////////////////      

# valor1 = int(input("digite o primeiro valor: "))
# valor2 = int(input("digite o segundo valor: "))
# operacao = input("digite a operaço que deseja realizar: ")

# if(operacao == "+"):
#    res = valor1 + valor2
#    print(res)

# elif(operacao == "-"):
#    res = valor1 - valor2
#    print(res)

# elif(operacao == "/"):
#    res = valor1/valor2
#    print(res)
#////////////////////////////

#Q3
# usuario = input("digite um usuario: ")
# senha = input ("digite uma senha: ")

# if (usuario == "admin" and senha == "admin"):
#       print("bem vindo")
#///////////////////////////////////////

#Q4
#idade = int(input("digite sua idade: "))

#if idade >= 18:
    #print("voto obrigatorio")

#elif idade >= 16:
    #print("voto opcional")

#else:
    #print("não pode votar")


#///////////////////////////////////////////////










#questao2 lista 2
#N = int(input("Digite a quantidade de valores: "))

#numeros = []

#for i in range(N):
    #valor = int(input("Digite um valor: "))

    #if valor >= 0 and valor <= 1000:
        #numeros.append(valor)

    #else:
        #print("Valor invalido")

#menor = min(numeros)
#maior = max(numeros)
#soma = sum(numeros)

#print(f"o menor numero é {menor}")
#print(f"o maior numero é {maior}")
#print(f"a soma dos numeros é {soma}")

#///////////////////////////////////////////////////////////

#Q3

#nome = input("Digite seu nome: ")

#if len(nome) < 3:
    #print("Nome invalido")
    #nome = input("Digite um nome válido: ")


#idade = int(input("Digite sua idade: "))

#if idade < 0 or idade > 150:
     #print("Valor invalido")
     #idade = input("Digite sua idade: ")



#salario = float(input("Digite seu salario: "))

#if salario < 0:
    #print("Salario invalido")
    #salario = float(input("Digite seu salario: "))


#sexo = input("Digite seu sexo (digite F ou M): ").upper()

#if sexo != 'F' and sexo != 'M':
    #print("Valor invalido")
    #sexo = input("Digite seu sexo: ")


#estadoCivil = input("Digite seu estado civil (digite S(solteiro) ou C(casado) ou V(viuvo) ou D(divorciado)): ").upper()

#if estadoCivil != 'S' and estadoCivil != 'C' and estadoCivil != "V" and estadoCivil != "D":
   #print("Valor invalido")
    #estadoCivil = input("Digite seu estado civil: ")



#print("DADOS DO USUARIO")

#print(f"NOME: {nome}")
#print(f"IDADE: {idade} anos")
#print(f"SALARIO: R${salario}")
#print(f"SEXO: {sexo}")
#print(f"ESTADO CIVIL: {estadoCivil}")

#//////////////////////////////////////////////////////////


#q5

#numeros = int(input("digite um numero: "))

#divisores = 0

#for i in range(1,numeros+1):
    #if numeros % i == 0:
       #divisores += 1

#if divisores == 2:
    #print(f"{numeros} é primo")

#else:
    #print(f"{numeros} não é primo")