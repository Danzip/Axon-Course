import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image_dft_np(img):
    f=np.fft.fft2(img)
    fshift=np.fft.fftshift(f)
    #magn=20*np.log(np.abs(fshift))
    return fshift

def image_idft_np(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def magn_and_phase(fshift):
    return cv2.cartToPolar(np.real(fshift),np.imag(fshift))

def dft_from_magn_phase(magn,phase):
    x, y = cv2.polarToCart(magn,phase)
    return x,y

img=cv2.imread('old-globe.jpg',cv2.IMREAD_GRAYSCALE)/255.0
img2=cv2.imread('index.jpeg',cv2.IMREAD_GRAYSCALE)/255.0
fshift=image_dft_np(img)
#print (fshift.shape)
img_back=image_idft_np(fshift)
show_img(img_back)

magn,phase=magn_and_phase(fshift)
x,y=dft_from_magn_phase(magn,phase)
x2,y2=dft_from_magn_phase()
new_image=np.abs(image_idft_np(x+1j*y))
#show_img(new_image)
new_image/np.max(new_image)
#print new_image.min(),new_image.max()
#plt.imshow(new_image,cmap='gray')
#plt.show()
show_img(new_image)
# (dshift,dmagn)=image_dft_cv2(img)
# img_back=image_idft_cv2(dshift)
# print(img_back.min(), img_back.max())
# show_img(img_back)



# cv2.show()
cv2.waitKey(0)
