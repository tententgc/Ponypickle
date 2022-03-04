import cv2 
import numpy as np
import matplotlib.pyplot as plt 

image = cv2.imread('img/test3.png')
plt.imshow(image,cmap='gray',vmin=0,vmax=255) 
plt.show()

width, height = image.shape
index, radius = 5,1.5
row, column   = index // width, index % width  

r = int(radius)

x = np.arange(max(column -  r, 0), min(column + r + 1, width)) 
y = np.arange(max(row - r, 0), min(row + r + 1, height))

print(x)
print(y) 

X, Y = np.meshgrid(x, y) 

plt.plot(X, Y,marker='.',color= 'k',linestyle = 'none')
plt.show()

R = np.sort(((X - column) ** 2 + (Y - row) ** 2)) 
print(R)

mask = R < radius
print(mask) 

print("X mask")
print(X[mask]) 

print("Y mask") 
print(Y[mask]) 

print((Y[mask]* width + X[mask])) 
print(R[mask])