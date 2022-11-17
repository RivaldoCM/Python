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


    options = int(input("Escolha uma das opções:  "))

    if options == 1:
        retangulo()
    elif options == 2:
        isosceles()
    elif options == 3:
        escaleno()
    else:
        print("Digite uma opção correta animal. ")
        time.sleep(2)
        menu()
    pass


def square():
    side = int(input("Digite o numero de lados:  "))
    size = int(input("Digite o tamanho do lado:  "))
    ang = 360/side

    for i in range(side):
        pen.forward(size)
        pen.left(ang)


def isosceles():
    size_igual = int(input("Digite o valor para dois lados de mesmo tamanho: "))
    base_ang = int(input("Digite o valor para dois angulos iguais: "))

    #CONVERTENDO PARA O ANGULO CORRETO.
    convert_ang = 180 - base_ang

    pen.left(convert_ang)
    pen.forward(size_igual)
    pen.left(base_ang*2)
    pen.forward(size_igual)
    pen.home()


def retangulo():
    size1 = int(input("Digite o tamanho do lado oposto a hipotenusa: "))
    base_size = int(input("Digite o valor para a base do triangulo: "))

    pen.right(90)
    pen.forward(size1)
    pen.left(90)
    pen.forward(base_size)
    pen.home()


def escaleno():
    pen.speed(1)

    pen.forward(100)
    pen.left(163)
    pen.forward(200)
    pen.left(143)
    pen.home()
    pen.hideturtle()


menu()
screen.exitonclick()
