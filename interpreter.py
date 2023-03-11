# python interpreter
expr = input("Ecxpresion: ").split()

'''
x is an integer
y is +, -, *, or /
z is an integer
'''
x = int(expr[0])
y = (expr[1])
z = int(expr[2])
#values for y
if y == "/":
        result = x/z
elif y == "*":
    result = x*z
elif y =="+":
    result = x+z
elif y == "-":
    result = x-z
# prit sum
print(f"sum {float(result):.2f}")

