def greeting():
    greet = input("Greetings ").lower().strip()
    if "hello" in greet:
        print("$0")
    elif greet[0] == "h" and "hello" not in greet:
        print("$20")
    else:
        print("$100")

greeting()