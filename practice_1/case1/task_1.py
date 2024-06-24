import math

def main():
    while True:
        number = input("Enter positive number: ")
        try:
            number = int(number)
            if number <= 0:
                raise ValueError()

            result = math.factorial(number)

            print(f"Result is: {result}.")

            break
        except ValueError as e:
            print("Number should be greater than 0")

if __name__ == "__main__":
    main()
