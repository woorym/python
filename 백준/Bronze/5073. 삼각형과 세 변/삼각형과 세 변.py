a, b, c = 1, 1, 1
while True:
        a, b, c = map(int, input().split())

        if a == 0 and b == 0 and c == 0:
            break

        if a >= b + c or b >= a + c or c >= a + b:
            print("Invalid")

        elif a == b and b == c and a == c:
            print("Equilateral")

        elif a == b or b == c or a == c:
            print("Isosceles")

        elif a != b and b != c and a != c:
            print("Scalene")
        