#passing list

def print_list(names):
    for i in range(0,len(names)):
        names[i]=names[i].title()
        print(names[i])

names = ["ram","priya","tinku","jaya"]
print_list(names)

print(names)