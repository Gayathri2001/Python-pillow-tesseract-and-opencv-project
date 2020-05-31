#you are going to change the colors of the image, creating variations based on a single photo. There are many complex ways to change a photograph using variations, such as changing a black and white image to either "cool" variants, which have light purple and blues in them, or "warm" variants, which have touches of yellow and may look sepia toned. In this assignment, you'll be just changing the image one color channel at a time
#For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. So the top row of changes would create three alternative pixels, varying the first channel (red). one at (20, 100, 50), one at (100, 100, 50), and one at (180, 100, 50). The next row would vary the second channel (blue), and would create pixels of color values (200, 10, 50), (200, 50, 50) and (200, 90, 50).

import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont, ImageDraw
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
# build a list of 9 images which have different color
images=[]
lables=[]
for i in range(3):
    for j in (0.1,0.5,0.9):
        source = image.split()
        mid = source[i].point(lambda x:x*j)
        source[i].paste(mid)
        im = Image.merge(image.mode, source)
        lables.append('channel {} intensity {}'.format(i,j))
        images.append(im)
font = ImageFont.truetype("readonly/fanwood-webfont.ttf",75)
# create a contact sheet from different color
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3+3*85))
x=0
y=0
draw = ImageDraw.Draw(contact_sheet)
for i,img in enumerate(images):
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    draw.text((x,y+first_image.height+5), lables[i], font=font)
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height+85
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
