from PIL import Image, ImageFont, ImageDraw
import time
import pandas as pd

# Certificate properties
text_color = (100, 100, 200)
font_size = 140
coustard_black = ImageFont.truetype(font="fonts/Coustard-Regular.ttf", size=font_size)

df = pd.read_csv('names.csv')
start = time.time()

for i in df.index:
    print(str(i)+ " "+ df['Names'][i])
    im = Image.open("template_certificate.jpg")

    d = ImageDraw.Draw(im)
    name = df['Names'][i]

    w, h = d.textsize(name,font=coustard_black)
    bounding_box = [500, 1200, 3000, 1450]
    x1, y1, x2, y2 = bounding_box
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1

    # d.rectangle([x1, y1, x2, y2],fill=(0,0,0))
    d.text((x,y), name, font=coustard_black, fill=text_color)
    # im.show()
    im.save("certificates/"+name+".png")

done = time.time()
elapsed = done-start
print("elapsed time :"+str(elapsed))