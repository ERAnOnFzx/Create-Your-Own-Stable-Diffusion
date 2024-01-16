import numpy as np
import multiprocessing
from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import matplotlib.image as img

noiseFiles = os.listdir("./data/fairyTails/")

def process_noise_image(imgpath):
    imgpath = "./data/fairyTails/" + imgpath
    image = img.imread(imgpath)
    level = imgpath.split("/")[-1][1:-4]
    level = 100 - int(level)
    level_ = np.zeros(256, dtype=int)
    i = 0
    while level != 0:
        level_[i] = (level % 2) * 255
        level = level // 2
        i += 1
    level_ = np.concatenate((level_, level_, level_))
    level_ = np.reshape(level_, (256,1,3))
    op = np.concatenate((image, level_), axis=1)
    plt.axis('off')
    fig = plt.gcf()
    fig.set_size_inches(2.56/1,2.57/1) #dpi=100, output = 256*257 pixels
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1,bottom=0,right=1,left=0,hspace=0,wspace=0)
    plt.margins(0,0)
    plt.imshow(op)
    plt.savefig(imgpath,dpi=100,pad_inches=0)
    plt.close()

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    res = list(tqdm(pool.imap(process_noise_image, noiseFiles), total=len(noiseFiles)))
