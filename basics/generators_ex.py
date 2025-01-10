


# printing squre root of a number list

def sqr_root(num):
    sq =[]
    for i in range(1,num+1):
     sq.append(i*i)
    return sq

print(sqr_root(10))

#using same logic using generators , whch is very useful when handling large amount of data

def sqr_root_gen(num):
    for i in range(1,num+1):
        yield i*i

sq = sqr_root_gen(10)
for i in sq:
    print(i)

