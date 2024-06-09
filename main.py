import random
import re

range_user = []
num = 0
correct_guess = False
valid_range = False
secret_num: int = 0
range_pattern = r'^[0-9]+-[0-9]+$'

while valid_range == False:
    in_user = input("> Insira um interválo de números. ex: 1-10, 1-3.. \n> ")
    if not re.match(range_pattern, in_user):
        print("É necessário inserir um intervalo válido para continuar")
    else:
        range_user = in_user.strip().split('-')
        if range_user[0] == range_user[1]:
            print(f"O intervalo precisa ser maior do que 1, seu intervalo foi {in_user}")
            print(f"É necessário inserir um válido intervalo para continuar")
        else:
            num = random.randint(int(range_user[0]), int(range_user[1]))
            valid_range = True  


while correct_guess == False:
    choosed = input(f"> Advinhe o número entre {range_user[0]}-{range_user[1]}\n> ")
    if not re.match(r'^[0-9]+$', choosed):
        print("Insira apenas um número válido")
    elif not num in range(int(range_user[0]), int(range_user[1])):
        print("Insira apenas números dentro do intervalo escolhido")
    else:
        print(num)
        if int(choosed) == num:
            print("Parabens, você acertou o número!!")
            correct_guess = True
        else:
            if int(choosed) > num:
                print("Ops, o seu número escolhido é mais alto, Tente novamente")
            else:
                print("Ops, o seu número escolhido é mais baixo, Tente novamente")
            
    