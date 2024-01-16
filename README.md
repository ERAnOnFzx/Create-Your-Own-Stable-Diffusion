# Create-Your-Own-Stable-Diffusion
## Data
There are 2 sets of data using in this repository, ImageNet1k and fairyTails. <br>
The link of ImageNet1k is https://www.kaggle.com/datasets/vitaliykinakh/stable-imagenet1k/data <br>
fairyTails is a set of 8 pictures which I used to test how to add noise to images, which is restored in ./data/fairyTails. <br>
## Prepare Data
Download ImageNet1k from the link above. Unzip it to the path ./data/ImageNet1k. <br>
Execute the code 'filesRename.py' to rename these files from 0.jpg to 100.jpg in each class. <br>
Execute the code 'ImageResize.py' to resize these images to 256x256 pixels. <br>
Execute the code 'addNoises2Image.py' to add noise to each image to create training data. <br>
## Run
Run the code 'CreateYourOwnStableDiffusion.ipynb' in jupyter notebook or jupyterLab.
## Contact
Email me if there's any advice or questions. <br>
eranonfzx@gmail.com
