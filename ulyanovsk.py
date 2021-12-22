from PIL import Image

text = open('LE07_L2SP_171022_20020725_20200916_02_T2_MTL.txt', 'r')

corners = ["CORNER_UL_LAT_PRODUCT", "CORNER_UL_LON_PRODUCT", "CORNER_UR_LAT_PRODUCT", "CORNER_UR_LON_PRODUCT","CORNER_LL_LAT_PRODUCT",
           "CORNER_LL_LON_PRODUCT", "CORNER_LR_LAT_PRODUCT", "CORNER_LR_LON_PRODUCT"]
coordinates = []
lines = text.readlines()

for line in lines:
    line = line.strip()
    if line[0:21] in corners:
        coordinates.append(float(line[24:]))
print(coordinates)

delta_y = abs(coordinates[0]-coordinates[4])
delta_x = abs(coordinates[1]-coordinates[3])
print(delta_x, delta_y)

x = 8341
y = 7731
density_x=delta_x/x
density_y=delta_y/y
print(density_x, density_y)

ul_lat = 54.3282
ul_lon = 48.3866

ul_dif_lat = coordinates[0] - ul_lat
ul_dif_lon = coordinates[1] - ul_lon
print(ul_dif_lat, ul_dif_lon)

pixel_lat = ul_dif_lat / density_y
pixel_lon = ul_dif_lon / density_x
print(pixel_lat, pixel_lon)
cst = 800
point_ul_x = 4734 - cst
point_ul_y = 4588 - cst
point_lr_x = 4734 + cst
point_lr_y = 4588 + cst

image = Image.open('LE07_L2SP_171022_20020725_20200916_02_T2_SR_B4.TIF')
cropped = image.crop((point_ul_x, point_ul_y, point_lr_x, point_lr_y))
cropped.save('C:\\Users\\his16\\Pictures\\Saved Pictures\\cropped.TIF')
image = Image.open('LE07_L2SP_171022_20020725_20200916_02_T2_SR_B3.TIF')
cropped = image.crop((point_ul_x, point_ul_y, point_lr_x, point_lr_y))
cropped.save('C:\\Users\\his16\\Pictures\\Saved Pictures\\cropped1.TIF')



