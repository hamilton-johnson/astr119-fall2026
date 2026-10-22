import numpy as np
b = np.array([[1,2,3], 
              [4,5,6]])
print(b.shape) # rows and columns
print(b[1,2])
print(b[0])
print(b[0,0])
print(b[:,1])
print(b[0:2,1:3])

from matplotlib.pyplot import imread, imsave
im =imread('clean_io_small.png')
print(im.shape)
im2 = im.copy()
print(im2.shape)
im2[20:40, 20:40, :] = 1
imsave('painted.png', im2)
