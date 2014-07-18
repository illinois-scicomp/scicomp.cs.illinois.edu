from __future__ import division

import scipy.io as sio
import scipy.sparse as sp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import pyamg

A = sio.mmread('matrix.mtx.gz')

ml = pyamg.smoothed_aggregation_solver(A, max_coarse=10)

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#w = ml.levels[0].A.shape[0]
#for k in range(3):
#    B = ml.levels[k].A.tocoo()
#    ax.scatter(B.row/B.row.max()*w, B.col/B.col.max()*w, k, s=10, c='b')
#ax.axis('off')
#plt.show()

c = A.row**2 + A.col**2
plt.figure(figsize=(8,4.5), dpi=240)
plt.scatter(A.row, -A.col, c=c, s=20, lw=1, edgecolor=[0.7,0.7,0.7])
ax = plt.gca()
ax.set_axis_bgcolor('black')
plt.axis('off')
plt.axis('tight')
plt.savefig('matrix.png', dpi=240)
plt.show()
