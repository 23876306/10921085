from PIL import Image
from PIL import ImageFilter

img1 = Image.open("puppy.jpg")
img2 = img1.fillter(ImageFilter.BLUR)   #模糊
img2.save("outP1.jpg")
img3 = img1.filter(ImageFilter.CONTOUR) #輪廓
img3.save("outP2.jpg")
img4 = img1.filter(ImageFilter.DETAIL)  #細節增強
img4.save("outP3.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE) #物件邊緣增強
img5.save("outP4.jpg")
img6 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE) #物件邊緣更增強
img6.save("outP5.jpg")
img5 = img1.filter(ImageFilter.EMBOSS) #浮雕
img5.save("outP6.jpg")