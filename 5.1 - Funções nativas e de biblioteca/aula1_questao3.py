import random 

x = random.randint(1, 10)

while True:
    y = int(input("Adivinhe um número entre 1 e 10: "))
    
    if y < x:
        print("Muito baixo! Tente novamente.")
    elif y > x:
        print("Muito alto! Tente novamente.")
    elif y == x:
        print(f"Parabéns, você acertou!, o numero é {x}")
        break

        
    