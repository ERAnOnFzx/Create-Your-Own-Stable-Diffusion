from PIL import Image
import os
import multiprocessing
from tqdm import tqdm

def compress_image(image_path):
    
    image = Image.open(image_path)

    target_width = 256
    target_height = 256

    image = image.resize((target_width, target_height))
    image.save(image_path)

if __name__ == "__main__":
    father = './data/ImageNet1k'
    son = os.listdir(father)
    sons = []
    for i in range(len(son)):
        temp = os.listdir(father+son[i])
        for j in temp:
            sons.append(father+son[i]+"/"+j)
    
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    res = list(tqdm(pool.imap(compress_image, sons), total=len(sons)))