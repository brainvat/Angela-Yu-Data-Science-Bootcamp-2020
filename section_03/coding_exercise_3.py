tracker = 0

def moveForwards():
    global tracker
    tracker += 1
    print('moved forward by one step.')

def turnRight():
    global tracker
    tracker -= 1
    print('turning right')

def move():

    moveForwards()
    turnRight()
    turnRight()
    turnRight()
    moveForwards()
    turnRight()
    turnRight()
    turnRight()
    moveForwards()
    turnRight()
    moveForwards()
    turnRight()
    moveForwards()
    moveForwards()
    return tracker
