# exercicios modulo 1 python  let´s code
import locale
locale.setlocale ( locale.LC_ALL, "pt-BR" )

def desconto():
    """  exeercicio 1
    Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
    programa deve imprimir a mensagem “O novo valor é [valor]
    """
    while True :
        try:
            valor = input(
            "Digite um valor para  ter um desconto de 15%:>> "
            )
            break
        except ValueError:
            print ( 'Entre com valor numérico. Use ponto para valor decimal.' )

    descontos = float(valor)  * 0.15
    print (
        "para o valor:", valor,
        'o desconto é: ', descontos ,
        'O novo valor é:>>', float(valor) - descontos
    )

def   valida():
 # exercicio 2
    """
    Faça um programa que leia a validade das informações:
    a. Idade: entre 0 e 150;
    b. Salário: maior que 0;
    c. Sexo: M, F ou Outro;
    O programa deve imprimir uma mensagem de erro para cada informação inválida.
    """

    # define as variaveis
    idade: int
    salario = float('inf')
    sexo=('M','F', 'O')


    while True:
        try:
            idade = int (
                input ( "digite sua idade: " )
            )
            if idade not in range(0,151):
                print(" digite uma idade entre 0 e 150 anos ")
            else:
                break
        except ValueError:
            print("entre apenas com numeros")

# "salario = float( input( 'digite seu salario: com ponto ex. 1.4 '))
    while True:
        try:
            salario = input (
                "Digite o seu salario(exemplo: R${}): ".format ( locale.format_string ( "%.2f", 1 ) )
            )
            if  salario <= '0,00':
                print("digite um salario valido")
            else:
                break

        except ValueError:
            print(" eu erro ")
# sexo
    while True:
        sex = str.upper ( input ( "DIGITE SEU SEXO (Mm/Ff/Oo):>>" ) )
        if sex not in sexo :
            print ( "valor invalido ")
        else:
            tiposexo= {"M":"Masculino","F":"feminino","O":"outro"}
            print("--------------Resultado-------------")
            print ("\nSua idade: ", idade, "\nseu  salario:",salario, "\nseu sexo:", tiposexo[sex] )
            break


def investiga():
# exercicio 3
    """
    3. Vamos fazer um programa para verificar quem é o assassino de um crime.
    Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde
    a resposta só pode ser sim ou não:
    a. Mora perto da vítima?
    b. Já trabalhou com a vítima?
    c. Telefonou para a vítima?
    d. Esteve no local do crime?
    e. Devia para a vítima?
    Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos
    com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas
    suspeitos, necessitando outras investigações. Valores  iguais ou abaixo de 1 são liberados.
    """
    pont = 0
    quest2 = [
        'Mora perto da vítima?',
        'Já trabalhou com a vítima?',
        'Telefonou para a vítima?',
        'Esteve no local do crime?',
        'Devia para a vítima?'
    ]
    print ( "**Responda apenas  S ou N **\n" )
    pergunta: int
    for pergunta in quest2:
        while True:
            resposta = input ( pergunta )
            ansers = ['SIM', 'S', 'NÃO', 'NAO', 'N']
            if not resposta.upper () in ansers:
                print ( 'responda apenas sim ou nao ' )
            else:
                break
        if resposta.upper () in ansers[0:2]:
            pont += 1

    resultado = [
        'Inocente',
        'Liberado',
        'Suspeito',
        'Cumplice',
        'Cumplice',
        'Assasino'
    ]
    print ( 'Voce foi considerado: ', resultado[pont])

def vezes(mult, qtd: int = 10):
    """
    4. Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
    """
    mtz = ( [x * mult for x in range ( 1, qtd +1)] )
    for i in range(len(mtz) ):
        print(mult , 'x {} = {}'.format(i+1, mtz[i]))


print("***********Exercicio 1 : 'desconto'***********\n")
desconto()
print("\n***********Exercicio 2 : 'Valida'***********\n")
valida()
print("\n***********Exercicio 3 : 'Investiga'***********\n")
investiga()
print("\n***********Exercicio 4 : 'tabuada' argumentos: numero , multiplicador")
multis = int(input("\n>>>Digite o multiplicador:>>"))
qtds = int( input("\n>>>Digite a quantidade de multiplicaçoes:>>"))
vezes(multis,qtds)
