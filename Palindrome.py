def palindrome(num):
    print("original number", num)
    original_num = num
    reverse_num = 0
    while num > 0:
        rem = num%10
        reverse_num = (reverse_num*10) + rem
        num = num//10
    if original_num == reverse_num:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")
palindrome(121)
palindrome(125)
