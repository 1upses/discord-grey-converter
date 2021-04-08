#Copyright (c) 2021, 1ups_ Inc.  All rights reserved.
#Copyrights licensed under the GNU General Public License v3.0.
#See the accompanying LICENSE file for terms.

from PIL import Image

filename = str(input("file name (png format): "))
im1 = Image.open(filename)
L,H=im1.size

treshold = int(input("treshold (0-255): "))

im2 = Image.new("RGBA",(L,H))
for y in range(H):
    for x in range(L):
        p = im1.getpixel((x,y))
        gris = int((p[0]+p[1]+p[2])//3)
        if gris > treshold:
            im2.putpixel((x,y),(0,0,0,0))
        else:
            im2.putpixel((x,y),(54,57,62,255))

chaine = "grey-"+filename
im2.save(chaine)
im2.show()
