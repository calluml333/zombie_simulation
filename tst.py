import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

np.random.seed(42)

# Displacements from a cell to its eight nearest neighbours
neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))

EMPTY, TREE, FIRE = 0, 1, 2
edge, empty, human, zombie = 0, 1, 2, 3
# Colours for visualization: brown for EMPTY, dark green for TREE and orange
# for FIRE. Note that for the colormap to work, this list and the bounds list
# must be one larger than the number of different values in the array.
colors_list = [(0,0,0), (1,1,1), (0,0,0.5), (1,0,0), 'red']

cmap = colors.ListedColormap(colors_list)

bounds = [0,1,2,3,4]

norm = colors.BoundaryNorm(bounds, cmap.N)

def iterate(X):
    X1 = np.zeros((ny, nx))
    X1[1:ny-1, 1:nx-1]  = np.full((ny-2, nx-2), empty)

    neighbourhood_new = [i for i in neighbourhood]
    np.random.shuffle(neighbourhood_new)

    for ix in range(1,nx-1):
        for iy in range(1,ny-1):
            
            if X[iy,ix] == human:
                X1[iy,ix] = human
                for dx,dy in neighbourhood_new:
                    if X[iy+dy,ix+dx] == edge:
                        X1[iy,ix] = human
                    elif X[iy+dy,ix+dx] == zombie:
                        X1[iy,ix] = zombie
                        break
                    elif X[iy+dy,ix+dx] == empty and np.random.random() <= mh:
                        X1[iy,ix] = empty
                        X1[iy+dy,ix+dx] = human
                        X[iy+dy,ix+dx] = human
                        break

            elif X[iy,ix] == zombie:
                X1[iy,ix] = zombie
                for dx,dy in neighbourhood_new:
                    if X[iy+dy,ix+dx] == edge:
                        X1[iy,ix] = zombie
                    elif X[iy+dy,ix+dx] == human:
                        X1[iy+dy,ix+dx] = zombie
                    elif X[iy+dy,ix+dx] == empty and np.random.random() <= mz:
                        X1[iy,ix] = empty
                        X1[iy+dy,ix+dx] = zombie
                        X[iy+dy,ix+dx] = zombie
                        break

    unique, counts = np.unique(X1, return_counts=True)
    d = dict(zip(unique, counts))  
    
    print("{} Humans || {} Zombies || Total: {}".format(d[2], d[3], (d[2]+d[3])))
    return X1

# The initial number of humans and zombies.
nh, nz = 10, 1

# Probability of new tree growth per empty cell, and of lightning strike.
p, f, = 0.005, 0.005

# Probability that a human and zombie will move position, respectively.
mh, mz = 0.3, 0.05

# Forest size (number of cells in x and y directions).
nx, ny = 5, 5

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

X = initiate_grid(nx, ny, nh, nz)
print(X)

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)#, interpolation='nearest')


# The animation function: called to produce a frame for each generation.
def animate(i):
    im.set_data(animate.X)
    animate.X = iterate(animate.X)
    
# Bind our grid to the identifier X in the animate function's namespace.
animate.X = X

# Interval between frames (ms).
interval = 100

if __name__ == "__main__":
    anim = animation.FuncAnimation(fig, animate, interval=interval)
    plt.show()