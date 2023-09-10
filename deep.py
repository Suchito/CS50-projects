def deep():
    question = input("What is the Answer to Great Question of Life, the Universe, and Everything? ").lower().strip()
    if question == "42" or question == "forty-two" or question == "forty two":
        print("Yes")
    else:
        print("No")

deep()