# perfect number any number divisor 
# 28 = 1,2,4,7,14  sum(all) = 28 
def perfect_number(n):
    l = []
    for i in range(1,n):
        if n % i  == 0:
             l.append(i)
    
    summ = sum(l)
    if summ == n:
        return True
    return False
print(perfect_number(28)) 


# time = o(n)
# space = o(n)

