from PIL import Image
from pylab import *

# im = array(Image.open("lena.jpg"))
#
# imshow(im)
#
# y = [100,100,400,400]
#
# x = [200,500,200,500]
#
# plot(x,y,'r*')
#
# plot(x[:2],y[:2])
#
# axis('off')
# title("plotting: lena.jpg")
#
# show()

# im = array(Image.open("lena.jpg").convert("L"))
#
# figure()
#
# gray()
#
# contour(im,origin='image')
# axis('equal')
# axis('off')
#
# figure()
# hist(im.flatten(),128)
# show()

# im = array(Image.open("lena.jpg"))
# imhist,bins = histogram(im.flatten(),256,normed=True)
# cdf = imhist.cumsum()
# cdf = 255*cdf/cdf[-1]
# im2 = interp(im.flatten(),bins[:-1],cdf)
# im2 = im2.reshape(im.shape)
# imshow(im2)
# show()