from random import randint

print("==========================")
print ("WILLKOMMEN.")
print ("RATEN SIE DIE ANZAHL DER M & Ms")
print ("Sie haben 7 Chancen, die richtige Nummer zu finden. Zahlen von 1 bis 130. Viel Glück!")
print ("===========================")

def game():
    answer = randint(1, 130)

    while True:
        for n in range(7):
            user_guess = int(input("Ratet mal die Nummer?\n"))
            if user_guess == answer:
                print("WTF😱 Alter, du hast gewonnen!")
                break
            elif user_guess > answer:
                print("Deine Vermutung ist höher!")
            else:
                print("Deine Vermutung ist kleiner!")
        else:
            print(f"Du hast verloren! Das ist sehr schade. Die Antwort war {answer}.")

        again = str(input("Willst du nochmal spielen? y oder n: "))
        if again == "y":
            game()
        else:
            break

game()
