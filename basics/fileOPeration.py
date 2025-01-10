
txt = '\npython is easy to learn .\n i will become a great man'
# with open('myFile.txt','w') as f open  file in write mode
# with open('myFile.txt','a') as f open file in append mode
try:
    with open('myFile.txt','a') as f:
     print(f.write(txt))
except FileNotFoundError as e:
    print(e)
finally:
    print(f.closed)