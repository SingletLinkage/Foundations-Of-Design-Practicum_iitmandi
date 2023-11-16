import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
path = 'positions.csv'
def animate(i):
    plt.cla()
    
    data = pd.read_csv(path)
    x = data['x']
    y = data['y']
    plt.plot(x,y)

def get_x_y_from_pos(pos):
    # pos : list of (x,y)
    x = [i[0] for i in pos]
    y = [i[1] for i in pos]
    return x,y

def start_plotting(DELAY=1000, path='positions.csv'):
    ani = FuncAnimation(plt.gcf(), animate, interval=DELAY, save_count=100)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    start_plotting()