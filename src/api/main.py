#Import Necessary Evil.
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
#import scipy.io
import os
import torch
import torch.nn as nn
import torch.optim as optim

#identify verisons
print(f'Numpy Version: {np.__version__}')
print(f'Pandas Version: {pd.__version__}')
print(f'Seaborn Version: {sns.__version__}')
print(f'Torch Version: {torch.__version__}')

#Fetch Dataset
train_dir = 'C:\Users\user\Desktop\LiverCirrhosisClassificationWebApp\liver disease.v2-release.multiclass\train'
test_dir = 'C:\Users\user\Desktop\LiverCirrhosisClassificationWebApp\liver disease.v2-release.multiclass\test'

#Display images from the train dataset 
# Get the list of image files in the directory
image_files = [f for f in os.listdir(train_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Randomly select 'num_images' images
selected_images = random.sample(image_files, min(6, len(image_files)))

# Display each selected image
for image_file in selected_images:
    image_path = os.path.join(train_dir, image_file)
    img = Image.open(image_path)
# Display image using Matplotlib
    plt.imshow(img)
    plt.title(image_file)
    plt.axis('off')  # Turn off axis labels
    plt.show()

data_transform = transforms.Compose([
        transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
train_dataset = datasets.ImageFolder(root=train_dir,
                                           transform=data_transform)
dataset_loader = torch.utils.data.DataLoader(train_dataset,
                                             batch_size=4, shuffle=True,
                                             num_workers=4)