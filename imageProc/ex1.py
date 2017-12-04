import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def K_greatest(dirty_img,norm_noise,K):
    U, S, V = np.linalg.svd(norm_noise, full_matrices=True)
    invS=1/S[:K]
    invS=np.append(invS,np.zeros(min(dirty_img.shape)-K))
    invSmat=np.zeros(dirty_img.shape)
    invSmat = np.diag(invS)
    invSNoise = np.dot(V.transpose(), np.dot(invSmat, U.transpose()))
    cleaned_img = np.dot(invSNoise, dirty_img)
    return cleaned_img



def RMS(im1,im2):
    return np.sum((im2-im1)**2)

def return_RMS(img,dirty_img,norm_noise):
    RMSList=[]
    for K in range(1,min(img.shape)+1):
        k_cln_img=K_greatest(dirty_img,norm_noise,K)
        RMSList.append(RMS(img,k_cln_img))
    return RMSList

img=cv2.imread('old-globe.jpg',cv2.IMREAD_GRAYSCALE)
x=range(1,501)
y=np.sin(x)


noise=np.random.random((500,500))
row_sums=noise.sum(axis=1)
norm_noise=noise/row_sums[:, np.newaxis]

dirty_img=np.dot(norm_noise,img)
cln_img=K_greatest(dirty_img,norm_noise,500)
#print RMS(img,cln_img)

RMSList=return_RMS(img,dirty_img,norm_noise)

plt.plot(x,RMSList)
plt.show()
invNoise=np.linalg.pinv(norm_noise)

#
#cleaned_img=K_greatest(dirty_img,norm_noise,499)




#cleaned_img=np.dot(invNoise,dirty_img)
#print dirty_img.max(),  dirty_img.min()
#print dirty_img
#show_img(cleaned_img.astype('uint8'))

#print