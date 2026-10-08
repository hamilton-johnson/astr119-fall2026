a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def quadratic(a,b,c):
    if a == 0:
        print("nope")
    else:
        result_pos = ((-b + (b**2 - 4*a*c)**0.5)/(2*a))
        result_neg = ((-b - (b**2 - 4*a*c)**0.5)/(2*a))
        return result_pos, result_neg
        

result1, result2 = quadratic(a,b,c)
print("x1: ", result1)
print("x2: ", result2)