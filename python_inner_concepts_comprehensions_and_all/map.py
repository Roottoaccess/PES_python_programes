def main():
    yell("This","is","CS50")


def yell(*words): # Veriable number of words
    # uppercase = []
    # for word in words:
    #     uppercase.append(word.upper())

    # This 3 line of code is reduce with the help of the map function !!
    # uppercase = map(str.upper, words)

    # Using the list comprehension
    uppercase = [word.upper() for word in words]

    print(*uppercase) # Unpacked !

if __name__ == "__main__":
    main()