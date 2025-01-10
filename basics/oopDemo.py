from abstractDemo import bike,car,vehicle



if (__name__ == '__main__'):
    print ("you are runnin this directly")

def set_color(obj,color):
    obj.color=color

bike1 = bike()
car1 = car()

set_color(bike1,"blue")
set_color(car1,"red")

print(car1.color)
print (bike1.color)