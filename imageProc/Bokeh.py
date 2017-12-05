import numpy as np
import scipy as sp
from matplotlib import pylab as plt
import cv2
import imageio
import matplotlib.animation as animation
from matplotlib import colors

from skimage import measure

filename = 'stabilized.avi'
vid = imageio.get_reader(filename,  'ffmpeg')
vid_length = len(vid)
nums = range(vid_length)
print len(vid)

def video_median(vid,rang):
    frame_list = []
    for num in rang:
        frame = vid.get_data(num)
        frame = colors.rgb_to_hsv(frame)
        frame_list.append(frame)

    return np.median(frame_list,axis=0)




def running(frame):
    pass


def dist(s,d):
    diff = s-d
    return np.sqrt((diff[:,:,0])**2+(diff[:,:,1])**2)



back_med = video_median(vid,range(20))

row = 400
col = 1160

g_kernel = cv2.getGaussianKernel(5, 20)

for n in range(30):
    frame = vid.get_data(n)
    frame_hsv = colors.rgb_to_hsv(frame)
    d = dist(frame_hsv, back_med)
    bw = np.zeros(d.shape)
    bw[d > 0.1] = 1
    all_labels = measure.label(bw)
    rafi  = np.zeros(d.shape)
    rafi_label = all_labels[row,col]
    if rafi_label > 0:
        rafi[all_labels == rafi_label] = 1

# Daniel added those line for morphology
    se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    rafi = cv2.morphologyEx(rafi, cv2.MORPH_CLOSE, se)
    plt.imshow(rafi)
    plt.show()
    # end
    frame_no_rafi = np.zeros(frame.shape)
    frame_with_rafi = np.zeros(frame.shape)

    for i in range(3):

        frame_no_rafi[:,:,i] = frame[:,:,i] * (1-rafi)
        frame_with_rafi[:, :, i] = frame[:, :, i] * rafi

    frame_no_rafi = cv2.blur(frame_no_rafi, (20, 20))
    frame_complete = frame_no_rafi + frame_with_rafi

    plt.imshow(frame_complete.astype('uint8'))
    plt.show()
