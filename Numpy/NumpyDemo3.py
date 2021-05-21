import numpy as np
from PIL import Image
from numpy import asarray
from matplotlib import pyplot

image = Image.open("kobe.png")
w, h = image.size
image_New = image.resize((w, h * 2))
data = asarray(image)
print("data array size:", data.shape)
print(data[1: 10, 1: 10 , 1])
image2 = Image.fromarray(data[:, :, 1])
data2 = data[0: 10, 0: 10, 1] // 8 * 8

imagex1 = Image.new("RGB", (256, 256), color=(255,0,0))

datax1 = np.array(imagex1)
datax1.setflags(write=1)
for i in range(256):
    datax1[:, i, 0] = i

data3 = data
image3 = Image.fromarray(data2)
imagex2 = Image.fromarray(datax1)
#print(data2[0:10,0:10])
#print(image2.mode)
 #print(image2.size)
#image2.save("outP1.jpg")
image3.save("outP2.jpg")
#pyplot.imshow(image2)
image_New.save("outP3.jpg")
pyplot.imshow(imagex2)
pyplot.imshow(image_New)
pyplot.show()