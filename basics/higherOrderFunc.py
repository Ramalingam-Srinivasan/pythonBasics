#thigher order function\
#takes function as param or return a function
def happy():
    print('am happy nom.............')

def feeling():
    print('feeling happy nw')


hp = happy

#print(hp())


def emotions(func):
    func()
    return feeling

feel = emotions(hp)

feel()