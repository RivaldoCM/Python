import turtle
import time

screen = turtle.Screen()
pen = turtle.Turtle()


def menu():
    print('''
            MENU:

            [1] - Desenhar um quadrado
            [2] - Desenhar triangulos
            [3] - Desenhar outras formas
            [4] - Sair
        ''')
    op = [1, 2, 3, 4]

    options = int(input("Escolha uma das opções:  "))

    if options == op[0]:
        teste()
    elif options == op[1]:
        triangles()
    elif options == op[2]:
        square()
    elif options != op:
        print("Digite uma opção correta animal. ")
        time.sleep(2)
        menu()


def square():
    print("fazendo")
    side = int(input("Digite o numero de lados:  "))
    size = int(input("Digite o tamanho do lado:  "))
    ang = 360/side

    for i in range(side):
        pen.forward(size)
        pen.left(ang)


def triangles():
    size_igual = int(input("Digite o valor para dois lados de mesmo tamanho: "))
    base_ang = int(input("Digite o valor para dois angulos iguais: "))

    teste = 180 - base_ang

    pen.left(teste)
    pen.forward(size_igual)
    pen.left(base_ang*2)
    pen.forward(size_igual)
    pen.home()
    print(teste)


def teste():
    pen.forward(50)
    pen.left(85)
    pen.forward(50)



menu()
screen.exitonclick()