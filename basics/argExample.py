#variable length argument example - uing this concept we can add any number f arguments in  the method arguments list

#  here args will create a tuple of arguments ...
#  if single elements then *args will create tuple
def total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(total(10,20,30,40))


# if we have key value pair then use **args called kwargs called
# as keyvalue variable argument length

def dic_arg(**args):
    for key,val in args.items():
        print(val)

dic_arg(name='ram',doorno=6,age=31,sex='male')

