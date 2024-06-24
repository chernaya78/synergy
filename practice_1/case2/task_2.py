import random

MAX_ATTEMPTS = 10

def main():
    secret = random.randint(1, 100)
    attempts = 0

    print(" /\\_/\\")
    print("( o.o )")
    print(" > ^ <")

    print("Welcome to this awesome game!")
    print("Try to guess my random secret number (tip - it's from 1 to 100) ;)")

    while attempts < MAX_ATTEMPTS:
        try:
            number = int(input("Enter number: "))
            if number < 1 or number > 100:
                raise Exception("Number should be from 1 to 100")

            attempts += 1

            if number < secret:
                print("Your number is too small")
            elif number > secret:
                print("Your number is too big")
            else:
                print("Congratulations! You have guessed my secret number! Awesome!")

                break

            if attempts == MAX_ATTEMPTS:
                raise Exception(f"You have reached attempts limit. My secret number was {secret}.")
        except ValueError:
            print("Please enter valid number")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
