from PIL import Image
from PIL import ImageDraw

newImg = Image.new("RGBA", (300, 300),"#f0f00f")
drawObj = ImageDraw.Draw(newImg)
for x in range(100, 200, 2):
    for y in range(100, 200, 2):
        drawObj.point([x,y], fill="Red")


drawObj.line([(5 , 5), (296, 5), (296, 296), (5, 296),(5, 5)], fill="Black")
drawObj.line([(12, 12), (293, 12), (293, 293), (12, 293),(12, 12)], fill="Purple")
drawObj.line([(17, 17), (290, 17), (290, 290), (17, 290),(17, 17)], fill="Blue")


for a in range(150, 300, 10):
    drawObj.line([(a, 0), (300, a-150)], fill= "White")
for b in range(0, 150, 10):
    drawObj.line([(0, b), (150-b, 0)], fill= "White")
for c in range(150, 300, 10):
    drawObj.line([(0, c), (c-150, 300)], fill= "White")
for d in range(0, 150, 10):
    drawObj.line([(d, 0), (d-150, 300)], fill= "White")



newImg.save("drawImg.png")