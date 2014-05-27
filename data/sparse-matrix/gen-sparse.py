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
plt.figure(figsize=(20, 10))
plt.scatter(A.row, -A.col, c=c, s=20, lw=0)
plt.axis('off')
plt.axis('tight')
plt.savefig('matrix.png', bbox_inches='tight')
plt.show()
