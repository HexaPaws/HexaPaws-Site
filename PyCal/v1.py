history = []

def get_number():
    while True:
        x = input(">>>> ")
        try:
            return float(x)
        except ValueError:
            print("Not a number! Try again.")


while True:
    print("Type in the first number")
    x = get_number()

    print("Type in the second number")
    y = get_number()

    print("Now type in any one of these five: + - * / **")
    z = input(">>>> ")

    result = None  # 💡 important!

    match z:
        case "+":
            result = x + y
        case "-":
            result = x - y
        case "*":
            result = x * y
        case "/":
            if y == 0:
                print("Nya! You can't divide by zero! >:3")
            else:
                result = x / y
        case "**":
            if x == 0 and y == 0:
                print("Cannot take zero to the power of zero!")
            else:
                result = x ** y
        case _:
            print("Invalid operation!")

    # ✅ only run if calculation worked
    if result is not None:
        print(f"The answer is {result}")

        entry = f"Nya! {x} {z} {y} = {result} :3"
        history.append(entry)

        show = input("Show history? (y/n): ")
        if show == "y":
            print("\n--- History ---")
            for item in history:
                print(item)
            print("---------------\n")

    again = input("Again? (y/n): ")
    if again != "y":
        break