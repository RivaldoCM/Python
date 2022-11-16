import turtle
import time

screen = turtle.Screen()
pen = turtle.Turtle()


def menu():
    print('''
            MENU:

            [1] - Desenhar um quadrado
            [2] - Desenhar triangulos
            [2] - Desenhar outras formas
            [3] - Sair
        ''')
    op = [1, 2, 3, 4]

    options = int(input("Escolha uma das opções:  "))

    if options == op[0]:
        print("funciona")
    elif options == op[1]:
        print("funcionando")
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


menu()
screen.exitonclick()
