
a = 0
for b in range(0,10,2):
 a += b +1
print(type([1,15,"h","30"]))

print("foo" * 3)
print(2 ** 3)

def cal(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return cal(n-1)+cal(n-2)
result = cal(5)
print(result)


list1 = [1,2,3]
list2 = [4,5,6]
res = list1 + list2
print(res)


def even(start, n):
    # Start from the next even number if 'start' is odd
    if start % 2 != 0:
        start += 1

    # Use list comprehension to generate the list of even numbers
    return [i for i in range(start, n + 1, 2)]


# Example usage
result = even(5, 13)
print(result)  # Output: [6, 8, 10, 12]