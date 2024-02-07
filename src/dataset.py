import torch
from torchvision import datasets, transforms

train_dir = 'C:/Users/user/Desktop/LiverCirrhosisClassificationWebApp/liver_disease.v2-release.multiclass/train'
valid_dir = 'C:/Users/user/Desktop/LiverCirrhosisClassificationWebApp/liver_disease.v2-release.multiclass/valid'
BATCH_SIZE = 32
data_transform = transforms.Compose([
        #transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Resize((224, 224)),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
train_dataset = datasets.ImageFolder(root=train_dir,
                                           transform=data_transform)
train_dataset_loader = torch.utils.data.DataLoader(train_dataset,
                                             batch_size=BATCH_SIZE, shuffle=True,
                                             num_workers=4)

valid_dataset = datasets.ImageFolder(root=valid_dir,
                                           transform=data_transform)
valid_dataset_loader = torch.utils.data.DataLoader(valid_dataset,
                                             batch_size=BATCH_SIZE, shuffle=False,
                                             num_workers=4)