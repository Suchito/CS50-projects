def main():
    sentence = input("Input a Sentence: ")
    sentence = convert(sentence)
    print(sentence)


def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence


main()