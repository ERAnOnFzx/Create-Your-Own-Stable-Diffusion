import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
import multiprocessing
from tqdm import tqdm
import os
import random

def create_noise_image(imgpath):
    img = image.imread(imgpath)
    noises = np.random.normal(size=(256,256,3))
    img = np.array(img/255.0)
    noise_power = 1
    noise_rate = random.sample(range(100),10)
    for i in range(10):
        x = noise_rate[i]
        noise = noise_power-x*0.01
        signal = 1.0 - noise
        noise_rates = noise ** 0.5
        signal_rates = signal ** 0.5
        noisy_images = signal_rates * img + noise_rates * noises
        minv = np.min(noisy_images)
        maxv = np.max(noisy_images)
        noisy_images = (noisy_images - minv) / (maxv - minv)

        level = 100 - x
        level_ = np.zeros(256, dtype=int)
        k = 0
        while level != 0:
            level_[i] = (level % 2)
            level = level // 2
            k += 1
        level_ = np.array([level_, level_, level_]).T
        level_ = np.reshape(level_,(256,1,3))
        op = np.concatenate((noisy_images, level_), axis=1)

        plt.axis('off')
        fig = plt.gcf()
        fig.set_size_inches(2.56/1,2.57/1) #dpi=100, output = 256*256 pixels
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1,bottom=0,right=1,left=0,hspace=0,wspace=0)
        plt.margins(0,0)
        plt.imshow(op)
        plt.savefig(imgpath[:-4]+str(i)+".jpg",dpi=100,pad_inches=0)
        plt.close()##!!!!!!!!IMPORTANT!!!!!!!!!!

if __name__ == "__main__":
    father = './data/ImageNet1k/'
    son = os.listdir(father)
    sons = []
    for i in range(len(son)):
        temp = os.listdir(father+son[i])
        for j in temp:
            sons.append(father+son[i]+"/"+j)
    
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    res = list(tqdm(pool.imap(create_noise_image, sons), total=len(sons)))