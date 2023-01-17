num = int(input())
print("Given number", num)
while num > 0:
    digit = num%10
    num = num // 10
    print(digit, end=" ")
