from PIL import Image
import numpy as np

image_RED = Image.open('C:\\Users\\his16\\Pictures\\Saved Pictures\\cropped1.TIF')
image_NIR = Image.open('C:\\Users\\his16\\Pictures\\Saved Pictures\\cropped.TIF')
#print(image_RED.getpixel((30, 30)))

RED = np.array(image_RED)
NIR = np.array(image_NIR)
NDVI = (NIR - RED)/(NIR + RED)
print(NDVI)
image_NDVI = Image.new("RGB", image_RED.size, color = (255, 255, 255))
# i- номер строки,j- номер столбца
cnt = 0
for i in NDVI:
    for j in range(len(i)):
        if i[j] >= 0.9:
            image_NDVI.putpixel((j,cnt), (4,18,14))
        elif i[j] >= 0.8:
            image_NDVI.putpixel((j,cnt), (4,38,4))
        elif i[j] >= 0.7:
            image_NDVI.putpixel((j,cnt), (4,54,4))
        elif i[j] >= 0.6:
            image_NDVI.putpixel((j,cnt), (4,66,4))
        elif i[j] >= 0.5:
            image_NDVI.putpixel((j,cnt), (4,94,4))
        elif i[j] >= 0.4:
            image_NDVI.putpixel((j,cnt), (28,114,4))
        elif i[j] >= 0.3:
            image_NDVI.putpixel((j,cnt), (100,162,4))
        elif i[j] >= 0.2:
            image_NDVI.putpixel((j,cnt), (142,182,20))
        elif i[j] >= 0.166:
            image_NDVI.putpixel((j,cnt), (132,138,52))
        elif i[j] >= 0.1:
            image_NDVI.putpixel((j,cnt), (164,130,76))
        elif i[j] >= 0.66:
            image_NDVI.putpixel((j, cnt), (180,150,108))
        elif i[j] >= 0:
            image_NDVI.putpixel((j, cnt), (252,254,252))
        elif i[j] >= -1:
            image_NDVI.putpixel((j, cnt), (4,18,60))
    cnt += 1
image_NDVI.show()