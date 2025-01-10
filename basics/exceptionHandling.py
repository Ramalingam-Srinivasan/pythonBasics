


try:
    nume = int(input("enter numerator:"))
    deno = int(input("enter denomenator:"))
    result = nume/deno
except ZeroDivisionError as e:
    print(e)
    print('you cannot divide by zero')
except ValueError as e:
   print(e)
   print("enter digits only....")
except Exception as e:
    print(e)
else:
    print(int(result))
finally:
    print('this block always runs')

print('bye...')

#assignemtn problems
# 1. write a function to list the first N prime numners
# 2. write a function to sort a list of values  . without using sort method
# 3. write a function a multiply two matrices