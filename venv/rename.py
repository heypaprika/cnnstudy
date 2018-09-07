import os
import cv2


imsize = 600
sidx = 2000

imglist = os.listdir('./')

for impath in imglist:
    if '.JPG' in impath:
        img = cv2.imread(impath)
        im = cv2.resize(img, (imsize, imsize))
        savename = '{}.png'.format(int(sidx))
        cv2.imwrite(savename, im)


        sidx += 1
    else:
        pass

cv2.waitKey(-1)



#print(imglist)