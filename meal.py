def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes



if __name__ == "__main__":
    main()