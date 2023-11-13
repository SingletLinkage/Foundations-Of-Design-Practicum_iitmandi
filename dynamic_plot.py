import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
import pandas as pd

# plt.style.use('fivethirtyeight')

# x = [363, 364, 380, 381, 386, 387, 391, 392, 393, 395, 484, 485, 488, 490, 495, 496, 513, 514, 515, 516, 516, 515, 515, 514, 514, 513, 513, 514, 514, 515, 515, 516, 516, 515, 515, 514, 514, 515, 515, 516, 516, 515, 515, 516, 516, 517, 517, 519, 519, 520, 520, 521, 521, 522, 522, 523, 523, 522, 516, 515, 509, 508, 504, 502, 497, 496, 491, 490, 451, 450, 443, 440, 430, 429, 424, 423, 396, 394, 389, 389, 388, 382, 381, 380, 377, 376, 373, 373, 374, 374, 373, 373, 372, 372, 373, 373, 374, 374, 373, 373, 372, 372, 370, 370, 368, 368, 367, 367, 366, 366, 365, 365, 364, 364, 362, 362, 361, 361, 360, 360, 359, 359, 358, 359, 359]
# y = [94, 95, 95, 96, 96, 97, 97, 98, 98, 100, 100, 99, 99, 97, 97, 96, 96, 97, 97, 98, 122, 123, 127, 128, 133, 134, 137, 138, 139, 140, 143, 144, 169, 170, 176, 177, 199, 200, 225, 226, 258, 259, 311, 312, 324, 325, 331, 333, 338, 339, 402, 403, 407, 408, 451, 452, 465, 466, 466, 467, 467, 468, 468, 470, 470, 471, 471, 472, 472, 471, 471, 468, 468, 467, 467, 468, 468, 470, 470, 471, 472, 472, 471, 471, 468, 468, 465, 459, 458, 454, 453, 429, 428, 349, 348, 337, 336, 310, 309, 304, 303, 302, 300, 297, 295, 212, 211, 207, 206, 183, 182, 179, 178, 177, 175, 172, 171, 166, 165, 101, 100, 99, 98, 97, 96]
# x.append(x[0])
# y.append(y[0])
# here x and y are dummy data. in the actual scenario, these data values will be collected from the robot.

def animate(i, index, path):
    # idx = next(index)
    plt.cla()
    # plt.plot(x[:idx],y[:idx])

    data = pd.read_csv(path)
    x = data['x']
    y = data['y']
    plt.plot(x,y)

    # plt.xlim((200, 700))
    # plt.ylim((0, 500))

def get_x_y_from_pos(pos):
    # pos : list of (x,y)
    x = [i[0] for i in pos]
    y = [i[1] for i in pos]
    return x,y

def start_plotting(DELAY=1000, path='positions.csv'):
    index = count()
    ani = FuncAnimation(plt.gcf(), animate, fargs=(index, path), interval=DELAY, save_count=100)
    plt.tight_layout()
    plt.savefig('pic.png')
    plt.show()
    
    
if __name__ == "__main__":
    start_plotting()
    
