def fl_same(numlist):
    print("Given list:", numlist)
    first_num=numlist[0]
    last_num=numlist[-1]
    if first_num == last_num:
        return True
    else:
        return False
numbers_x=[10,20,30,40,10]
print("result is", fl_same(numbers_x))
numbers_y=[75,65,35,75,30]
print("result is", fl_same(numbers_y))
