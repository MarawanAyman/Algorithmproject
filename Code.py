def R(X, Y):
    if X == 1:
        return Y
    if X % 2 == 0:
        return R(X // 2, Y * 2)
    return Y + R(X // 2, Y * 2)
num1 = 50
num2 = 65
product = R(num1, num2)
print(product)
