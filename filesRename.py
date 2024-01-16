from tqdm import tqdm
import multiprocessing
import os

def rename_files(path):
    files = os.listdir(path)
    for i in range(len(files)):
        new_name = str(1000 + i)[1:] + '.jpg'
        os.rename(path+files[i],path+new_name)

if __name__ == "__main__":
    father = './data/ImageNet1k/'
    son = os.listdir(father)
    for i in range(len(son)):
        son[i] = father + son[i] + "/"
    
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    res = list(tqdm(pool.imap(rename_files, son), total=len(son)))