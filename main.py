import inputfromesp


# under development


DELAY = 500 # in ms
SIZE = 1000 # size of canvas for real time path tracing
INITIAL =(SIZE//2, SIZE//2)  # initial x,y of bot

path = [] # list of (x,y) of bot positions; to be traced by robot

def get_current_pos(INITIAL):
    # communicate with nodemcu to get current location
    x,y = None, None
    return x,y


if __name__  == '__main__':
    path.append(get_current_pos(INITIAL))
