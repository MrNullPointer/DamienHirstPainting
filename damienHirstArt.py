import colorgram

rgbColors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    rgbColors.append((r,g,b))

print(rgbColors)