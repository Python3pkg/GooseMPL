
import matplotlib.pyplot as plt
import numpy as np

x,y = np.meshgrid(np.linspace(0,1,100),np.linspace(0,1,100))
d   = np.sqrt(x**2+y**2)

# ==============================================================================
# default
# ==============================================================================

fig,ax = plt.subplots()

cax = ax.imshow(d)

cbar = fig.colorbar(cax,aspect=10)
cbar.set_ticks([0,np.sqrt(2.)])
cbar.set_ticklabels(['0',r'$\sqrt{2}$'])  # vertically oriented colorbar

ax.xaxis.set_ticks(list(range(0,101,20)))
ax.yaxis.set_ticks(list(range(0,101,20)))

plt.xlim([0,100])
plt.ylim([0,100])

plt.xlabel(r'x')
plt.ylabel(r'y')

plt.savefig('image.svg')

# ==============================================================================
# goose
# ==============================================================================

plt.style.use('goose')

fig,ax = plt.subplots()

cax = ax.imshow(d)

cbar = fig.colorbar(cax,aspect=10)
cbar.set_ticks([0,np.sqrt(2.)])
cbar.set_ticklabels(['0',r'$\sqrt{2}$'])  # vertically oriented colorbar

ax.xaxis.set_ticks(list(range(0,101,20)))
ax.yaxis.set_ticks(list(range(0,101,20)))

plt.xlim([0,100])
plt.ylim([0,100])

plt.xlabel(r'x')
plt.ylabel(r'y')

plt.savefig('image_goose.svg')

# ==============================================================================
# goose-latex
# ==============================================================================

plt.style.use(['goose','goose-latex'])

fig,ax = plt.subplots()

cax = ax.imshow(d)

cbar = fig.colorbar(cax,aspect=10)
cbar.set_ticks([0,np.sqrt(2.)])
cbar.set_ticklabels(['0',r'$\sqrt{2}$'])  # vertically oriented colorbar

ax.xaxis.set_ticks(list(range(0,101,20)))
ax.yaxis.set_ticks(list(range(0,101,20)))

plt.xlim([0,100])
plt.ylim([0,100])

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.savefig('image_goose-latex.svg')
