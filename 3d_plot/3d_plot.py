from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

data_file = np.genfromtxt('test2D_data2.txt', delimiter='|')

x = data_file[:,0];
y = data_file[:,1];
z = data_file[:,2];


#x = np.linspace(0, 100, 1)
#y = np.linspace(0, 100, 1)
#z = np.linspace(-2, 2, 1)


fig = plt.figure()


ax = plt.axes(projection='3d')
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_wireframe(x,y,z, rstride=2, cstride=2)
#ax.plot_wireframe(X,Y,Z, linewidth=0.5);

ax.scatter(x,y,z, c = z)

plt.show()
