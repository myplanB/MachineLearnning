from PIL import Image
import os

pil_im = Image.open("lena.jpg")
# pil_im.show()
#
# for infile in filelist:
#     outfile = os.path.splitext(infile)[0]+".jpg"
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print "can not convert "+infile

#
# pil_im.thumbnail((128,128))
# pil_im.show()

# box = (100,100,400,400)
# region = pil_im.crop(box)
# region.show()
#
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region,box)
# pil_im.show()

# out = pil_im.resize((128,128))
# out.show()

out = pil_im.rotate(90)
out.show()