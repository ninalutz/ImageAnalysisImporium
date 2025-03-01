# import the necessary packages
from sklearn.cluster import MiniBatchKMeans 
import numpy as np
import argparse
import cv2
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from PIL import Image  
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import itertools
import matplotlib.colors as mcolors 
import colorsys

filename = ""
filename += "trump.jpg" #add your image name here
num_clusters = 5

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

rgbList = []

# load the image, grab its dimensions (width and height),
image = Image.open(filename)
w = image.width
h = image.height

print(w)
print(h)

# grab each pixel, convert to hsv, and add to a list.

def pixels_rgb_list(in_list, h, w) :
    for y in range(0, h):
        for x in range(0, w):
            # print(image.getpixel((x, y)))
            pixelRBG = (r, g, b) = image.getpixel((x, y))
            in_list.append(pixelRBG)

pixels_rgb_list(rgbList, h, w)

hsvList = []

for x in rgbList:
  pixelHSV = rgb_to_hsv(x[0], x[1], x[2])
  hsvList.append(pixelHSV)


clt = MiniBatchKMeans(num_clusters)
clt.fit(hsvList)
clusterCenters = list(clt.cluster_centers_)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
cols = []
# plotting the points
pts = []
for i in range(0, len(hsvList)):
  if i % 100 == 0:
    pts.append(hsvList[i])
    cols.append(rgbList[i])

for p_i in range(len(pts)):
    #todo -- HSV to RGB
    p = pts[p_i]
    c = cols[p_i]
    ax.scatter(p[0], p[1], p[2], zdir='z', c=(c[0]/255, c[1]/255, c[2]/255), s=3)

for col in clusterCenters:
  print(col)
  r, g, b = colorsys.hsv_to_rgb(col[0]/360, col[1]/100, col[2]/100)
  ax.scatter(col[0], col[1], col[2], zdir='z', c=(r, g, b),edgecolors= "lawngreen", s=150)

ax.legend()
ax.set_xlim3d(0, 360) #H = 0-360
ax.set_ylim3d(0, 100) # S = 1-100
ax.set_zlim3d(0, 100) # V = 1-100

plt.show()
plt.savefig('plot-15.png')
