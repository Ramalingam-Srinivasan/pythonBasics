#letter = ''
# while not letter.isalpha():
#     letter = input("enter an alpha")
#
# print("you have entereed : "+letter)

#for i in range(1,100):
 #   print(i)

 #break example
#print("print the number to put in list\n")
#my_list = []

#while True:
 #   inp = input()
  #  if (inp== 'z'):
   #     break
    #my_list.append(int(inp))
#print(my_list)


#continue example

str = "a,b,r,a,m"
str2 = ''

for i in str:
    if i==',':
        #continue
        pass
    else:
        str2 = str2 + i
print(str2)
