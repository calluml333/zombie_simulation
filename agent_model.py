import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
import logging


#=========================================================#
'''--------------------- Some setup --------------------'''
#=========================================================#

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
#=========================================================#
 
 
def iterate(X):
    global X_names
    global zi
    X1 = np.zeros((ny, nx))
    X1[1:ny-1, 1:nx-1]  = np.full((ny-2, nx-2), empty)

    neighbourhood_new = [i for i in neighbourhood]
    np.random.shuffle(neighbourhood_new)
    names = []

    for ix in range(1,nx-1):
        for iy in range(1,ny-1):
            if X[iy,ix] == human:
                X1[iy,ix] = human
                if X_names[iy,ix] not in names:
                    for dx,dy in neighbourhood_new:
                        if X[iy+dy,ix+dx] == zombie and np.random.random() <= p_b:
                            X1[iy,ix] = zombie
                            X[iy,ix] = zombie
                            X_names[iy,ix] = generate_name("z", zi)
                            zi += 1
                            names.append(X_names[iy,ix])
                            break
                        elif X[iy+dy,ix+dx] == zombie and np.random.random() <= p_k:
                            X[iy+dy,ix+dx] = empty
                            X1[iy+dy,ix+dx] = empty
                            X_names[iy+dy,ix+dx] = generate_name('e')
                        elif X[iy+dy,ix+dx] == empty and np.random.random() <= mh:
                            X1[iy+dy,ix+dx] = human
                            X[iy+dy,ix+dx] = human
                            X_names[iy+dy,ix+dx] = X_names[iy,ix]
                            X1[iy,ix] = empty
                            X[iy,ix] = empty
                            X_names[iy,ix] = generate_name('e')
                            names.append(X_names[iy+dy,ix+dx])
                            break            
            elif X[iy,ix] == zombie:
                X1[iy,ix] = zombie
                if X_names[iy,ix] not in names:
                    for dx,dy in neighbourhood_new:
                        if X[iy+dy,ix+dx] == human and np.random.random() <= p_b:
                            X1[iy+dy,ix+dx] = zombie
                            X[iy+dy,ix+dx] = zombie
                            X_names[iy+dy,ix+dx] = generate_name("z", zi)
                            zi += 1
                            names.append(X_names[iy+dy,ix+dx])
                        elif X[iy+dy,ix+dx] == human and np.random.random() <= p_k:
                            X1[iy,ix] = empty
                            X[iy,ix] = empty
                            X_names[iy,ix] = generate_name('e')
                        elif X[iy+dy,ix+dx] == empty and np.random.random() <= mz:
                            X1[iy+dy,ix+dx] = zombie
                            X[iy+dy,ix+dx] = zombie
                            X_names[iy+dy,ix+dx] = X_names[iy,ix]
                            X1[iy,ix] = empty
                            X[iy,ix] = empty
                            X_names[iy,ix] = generate_name('e')
                            names.append(X_names[iy+dy,ix+dx])
                            break

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
    global hi
    global zi
    X  = np.zeros((ny,nx))
    Y  = np.full(((ny-2),(nx-2)), empty)
    X_names = np.full([ny,nx], generate_name('e'))

    used_indices = []
    i = 0
    while i < n_humans:
        iy = np.random.randint(0, (ny-2))
        ix = np.random.randint(0, (nx-2))
        if (iy,ix) not in used_indices:
            Y[iy,ix] = human
            used_indices.append((iy,ix))
            X_names[iy+1,ix+1] = generate_name("h", hi)
            hi += 1
            i += 1
            # print("New human name (", X_names[iy+1,ix+1], ") assigned at ", (iy,ix))   
    j = 0
    while j < n_zombies:
        iy = np.random.randint(0, (ny-2))
        ix = np.random.randint(0, (nx-2))
        if (iy,ix) not in used_indices:
            Y[iy,ix] = zombie
            used_indices.append((iy,ix))
            X_names[iy+1,ix+1] = generate_name("z", zi)
            zi += 1
            j += 1       
            # print("New zombie name (", X_names[iy+1,ix+1], ") assigned at ", (iy,ix))   
        
    X[1:ny-1, 1:nx-1] = Y   
    return X, X_names


def generate_name(agent_type, number=None):
    if agent_type == 'e':
        return 'eeeeeee'
    if number < 10:
     return agent_type + "_0000" + str(number)
    elif 10 < number < 100:
     return agent_type + "_000" + str(number)
    elif 100 < number < 1000:
     return agent_type + "_00" + str(number)
    elif 1000 < number < 10000:
     return agent_type + "_0" + str(number)
    elif 10000 < number < 100000:
     return agent_type + "_" + str(number)


def animate(i):
    ax.set_title("{} Humans || {} Zombies || Total: {}".format(nh, nz, nh+nz))
    im.set_data(animate.X)
    animate.X = iterate(animate.X) 
    

#=========================================================#
'''--------------------- Paramters ---------------------'''
#=========================================================#


# Displacements from a cell to its eight nearest neighbours
neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))

edge, empty, human, zombie = 0, 1, 2, 3

# Colours for visualization: black for edge, white for empty, blue for human
# and red for zombie.
colors_list = [(0,0,0), (1,1,1), (0,0,0.5), (1,0,0), 'red']
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3,4]
norm = colors.BoundaryNorm(bounds, cmap.N)

# The initial number of humans and zombies.
nh, nz = 500, 5

# Probability a human will kill a zombie, and that a zombie will bite a human
p_k, p_b = 0.5, 0.8

# Probability that a human and zombie will move position, respectively.
mh, mz = 0.3, 0.05

# Forest size (number of cells in x and y directions).
nx, ny = 100, 100

# Initialise ints to be used in the names for each of the agent types
hi, zi = 0, 0

# Interval between frames (ms).
interval = 100


if __name__ == "__main__":
    X, X_names = initiate_grid(nx, ny, nh, nz)
    fig = plt.figure(figsize=(25/3, 6.25))
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    im = ax.imshow(X, cmap=cmap, norm=norm)#, interpolation='nearest')

    # Bind grid to the identifier X in the animate function's namespace.
    animate.X = X

    anim = animation.FuncAnimation(fig, animate, interval=interval)
    plt.show()