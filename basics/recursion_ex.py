

#printing factoraila of number
def fact(num):
    if num==0:
        return 1
    return num * fact(num-1)

print(fact(5))


#fibinocii series in recursion


def fibo(num):
    if num<=1:
        return num
    return (fibo(num-1)+fibo(num-2))

nterms=5
for i in range(nterms): 
    print(fibo(i))
