a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

def check_triangle(a, b, c):
    sides = sorted([a, b, c])

    if sides[0]** 2 + sides[1] ** 2 == sides[2] **2:
        return True
    else:
        return False


if check_triangle(a, b, c):
        print("The triangle is right-angles.")

else:
        print("The triangle is not right-angled.")

