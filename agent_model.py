import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
import logging

np.random.seed(42)


# logging  
LOG = os.getcwd() + "/tmp/ccd.log"                                                     
logging.basicConfig(filename=LOG, filemode="w", level=logging.DEBUG)  

# console handler  
console = logging.StreamHandler()  
console.setLevel(logging.ERROR)  
logging.getLogger("").addHandler(console)

def log_message(message):
    logger = logging.getLogger(__name__)
    logger.debug(message)

#=========================================================#
'''--------------------- Functions ---------------------'''
#=========================================================
 
 
def iterate(X):
    X1 = np.zeros((ny, nx))
    X1[1:ny-1, 1:nx-1]  = np.full((ny-2, nx-2), empty)

    neighbourhood_new = [i for i in neighbourhood]
    np.random.shuffle(neighbourhood_new)

    for ix in range(1,nx-1):
        for iy in range(1,ny-1):
            # log_message("\n --- \n{}".format((iy,ix)))
            if X[iy,ix] == human:
                # log_message("Human at {}".format((iy,ix)))
                X1[iy,ix] = human
                for dx,dy in neighbourhood_new:
                    # log_message("{}: X[{},{}] || {}".format((dy,dx),iy+dy,ix+dx,X[iy+dy,ix+dx]))
                    if X[iy+dy,ix+dx] == edge:
                        # log_message("Edge at {}".format((iy+dy,ix+dx)))
                        X1[iy,ix] = human
                    elif X[iy+dy,ix+dx] == zombie and np.random.random() <= p_b:
                        # log_message("Zombie at {}".format((iy+dy,ix+dx)))
                        X1[iy,ix] = zombie
                        X[iy,ix] = zombie
                        break
                    elif X[iy+dy,ix+dx] == zombie and np.random.random() <= p_k:
                        # log_message("Zombie at {}".format((iy+dy,ix+dx)))
                        X[iy+dy,ix+dx] = empty
                        X1[iy+dy,ix+dx] = empty
                    elif X[iy+dy,ix+dx] == empty and np.random.random() <= mh:
                        # log_message("Human is moving")
                        X1[iy,ix] = empty
                        X[iy,ix] = empty
                        X1[iy+dy,ix+dx] = human
                        X[iy+dy,ix+dx] = human
                        # log_message("Human moved to ({},{})".format(iy+dy,ix+dx))
                        break

            elif X[iy,ix] == zombie:
                # log_message("\n --- \nZombie at {}".format((iy,ix)))
                X1[iy,ix] = zombie
                for dx,dy in neighbourhood_new:
                    # log_message("{}: X[{},{}] || {}".format((dy,dx),iy+dy,ix+dx,X[iy+dy,ix+dx]))
                    if X[iy+dy,ix+dx] == edge:
                        # log_message("Edge at {}".format((iy+dy,ix+dx)))
                        X1[iy,ix] = zombie
                    elif X[iy+dy,ix+dx] == human and np.random.random() <= p_b:
                        # log_message("Human at {}".format((iy+dy,ix+dx)))
                        X1[iy+dy,ix+dx] = zombie
                        X[iy+dy,ix+dx] = zombie
                    elif X[iy+dy,ix+dx] == human and np.random.random() <= p_k:
                        # log_message("Human at {}".format((iy+dy,ix+dx)))
                        X1[iy,ix] = empty
                        X[iy,ix] = empty
                    elif X[iy+dy,ix+dx] == empty and np.random.random() <= mz:
                        # log_message("Zombie is moving")
                        X1[iy,ix] = empty
                        X[iy,ix] = empty
                        X1[iy+dy,ix+dx] = zombie
                        X[iy+dy,ix+dx] = zombie
                        # log_message("Zombie moved to ({},{})".format(iy+dy,ix+dx))
                        break
    # log_message("\n -------------- \nX1:")
    # log_message(X1)
    # log_message("\n -------------- \n")

    adjust_counts(X1)
    return X1


def adjust_counts(grid):
    global nz
    global nh

    unique, counts = np.unique(grid, return_counts=True)
    d = dict(zip(unique, counts))    
    try:
        nh = d[2]
    except KeyError:
        nh = 0
    try:
        nz = d[3]
    except KeyError:
        nz = 0



def initiate_grid(nx, ny, n_humans, n_zombies):
    X  = np.zeros((ny,nx))
    Y  = np.full((ny-2)*(nx-2), empty)
    
    used_indices = []
    
    i = 0
    while i < n_humans:
        index = np.random.randint(0, (ny-2)*(nx-2))
        if index not in used_indices:
            Y[index] = human
            used_indices.append(index)
            i += 1
    j = 0
    while j < n_zombies:
        index = np.random.randint(0, (ny-2)*(nx-2))
        if index not in used_indices:
            Y[index] = zombie
            used_indices.append(index)
            j += 1            
        
    Y = np.resize(Y,((ny-2),(ny-2)))
    X[1:ny-1, 1:nx-1] = Y
    
    print(X)

    return X


def animate(i):
    # log_message(animate.X)

    ax.set_title("{} Humans || {} Zombies || Total: {}".format(nh, nz, nh+nz))
    im.set_data(animate.X)
    animate.X = iterate(animate.X) 
    

#=========================================================#
'''--------------------- Paramters ---------------------'''
#=========================================================#


# Displacements from a cell to its eight nearest neighbours
neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))

edge, empty, human, zombie = 0, 1, 2, 3

# Colours for visualization: brown for EMPTY, dark green for TREE and orange
# for FIRE. Note that for the colormap to work, this list and the bounds list
# must be one larger than the number of different values in the array.
colors_list = [(0,0,0), (1,1,1), (0,0,0.5), (1,0,0), 'red']
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3,4]
norm = colors.BoundaryNorm(bounds, cmap.N)

# The initial number of humans and zombies.
nh, nz = 200, 1

# Probability of new tree growth per empty cell, and of lightning strike.
p, f, = 0.005, 0.005

# Probability a human will kill a zombie, and that a zombie will bite a human
p_k, p_b = 0.5, 0.3

# Probability that a human and zombie will move position, respectively.
mh, mz = 0.3, 0.05

# Forest size (number of cells in x and y directions).
nx, ny = 50, 50

# Interval between frames (ms).
interval = 100

if __name__ == "__main__":
    # log_message('\n\n\n-------------------- New Run ---------------------')
    print('Initiating Grid')
    X = initiate_grid(nx, ny, nh, nz)
    print('Grid Initiated')

    print('Creating Figrue')
    fig = plt.figure(figsize=(25/3, 6.25))
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    im = ax.imshow(X, cmap=cmap, norm=norm)#, interpolation='nearest')
    print('Figrue Created')

    print(' Bind our grid to the identifier X in the animate functions namespace')   
    # Bind our grid to the identifier X in the animate function's namespace.
    animate.X = X
    print('Grid Binded')

    print('Animating')
    anim = animation.FuncAnimation(fig, animate, interval=interval)
    plt.show()
