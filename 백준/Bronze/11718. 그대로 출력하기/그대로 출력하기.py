for _ in range(100):
    try:

        str1 = input()
        print(str1)
    except EOFError:
        break