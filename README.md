# Create-Your-Own-Stable-Diffusion
## Data 数据集
There are 2 sets of data using in this repository, ImageNet1k and fairyTails. <br>
The link of ImageNet1k is https://www.kaggle.com/datasets/vitaliykinakh/stable-imagenet1k/data <br>
fairyTails is a set of 8 pictures which I used to test how to add noise to images, which is restored in ./data/fairyTails. <br>
这个存储库用到了两组数据，ImageNet1k和fairyTails<br>
ImageNet1k的链接是https://www.kaggle.com/datasets/vitaliykinakh/stable-imagenet1k/data <br>
fairyTails是8张用来展示如何给图片加噪的测试用例，存储在./data/fairyTails中<br>
## Data Preprocessing 数据预处理
Remove the README.md files in ./results/ ./data/ ./data/ImageNet1k/ ./data/fairyTails/ before running the code. <br>
Download ImageNet1k from the link above. Unzip it to the path ./data/ImageNet1k. <br>
Execute the code 'filesRename.py' to rename these files from 0.jpg to 100.jpg in each class. <br>
Execute the code 'ImageResize.py' to resize these images to 256x256 pixels. <br>
Execute the code 'addNoises2Image.py' to add noise to each image to create training data. <br>
在运行代码前请先删掉./results/ ./data/ ./data/ImageNet1k/ ./data/fairyTails/中的README.md文件<br>
从上面的链接下载ImageNet1k数据集，并将其解压到./data/ImageNet1k文件夹中<br>
依次执行 'filesRename.py' 'ImageResize.py' 'addNoises2Image.py' 三个代码对数据进行预处理
## Run 运行
Run the code 'CreateYourOwnStableDiffusion.ipynb' in jupyter notebook or jupyterLab. <br>
在jupyter notebook或者jupyterLab中运行'CreateYourOwnStableDiffusion.ipynb'
## Contact 联系方式
Email me if there's any advice or questions. <br>
eranonfzx@gmail.com <br>
如果有任何建议或问题欢迎邮件联系 <br>
邮箱地址为: eranonfzx@gmail.com <br>
