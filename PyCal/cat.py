from rich import print
history = []

def get_number():
    while True:
        x = input(">>>> ")
        try:
            return float(x)
        except ValueError:
            print("Not a number! Try again.")


while True:
    print("Type in the first number[cyan]:3[/cyan]!")
    x = get_number()

    print("Type in the second number![cyan] :3[/cyan]!")
    y = get_number()

    print("Now type in any one of these five: [magenta] + - * / ** [/magenta]")
    z = input("[green] >>>> [/green]")

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
                print("[cyan] Nya! [/cyan] [red]You can't divide by zero![/red] [cyan]>:3 [/cyan]")
            else:
                result = x / y
        case "**":
            if x == 0 and y == 0:
                print("[cyan] Nya! [/cyan] [red]Cannot take zero to the power of zero! [/red] >:3")
            else:
                result = x ** y
        case _:
            print("Invalid operation!")

    # ✅ only run if calculation worked
    if result is not None:
        print(f"The answer is {result}")

        entry = f"[cyan]Nya! [/cyan] {x} {z} {y} = {result} :3"
        history.append(entry)

        show = input("[green]Show history? (y/n): [/green]")
        if show == "y":
            print("\n--- History ---")
            for item in history:
                print(item)
            print("---------------\n")

    again = input("[green] Again? (y/n): [/green]")
    if again != "y":
        break