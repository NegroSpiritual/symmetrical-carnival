import torch
import torch.nn as nn
import torch.optim as optim
from tqdm.auto import tqdm

from dataset import train_dataset_loader, valid_dataset_loader
from model import SimpleClassifier
#TODO: use argparser to make it a command line thing
lr = 1e-4
EPOCHS = 30
device = ('cuda' if torch.cuda.is_available() else 'cpu')

model = SimpleClassifier().to(device)
print(model)
print(f'Computation on: {device}')

optimizer = optim.Adam(model.parameters(), lr=lr)
criterion = nn.CrossEntropyLoss()

def train(model, datasetloader, optimizer, criterion):
    model.train()
    print('Training...')
    train_running_loss = 0.0
    train_running_correct = 0
    counter = 0
    for i, data in tqdm(enumerate(datasetloader), total=len(datasetloader)):
        image, labels = data
        image = image.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()
        outputs = model(image)
        loss = criterion(outputs, labels)
        train_running_loss += loss.item()
        _, pred = torch.max(outputs.data, 1)
        train_running_correct += (pred==labels).sum().item()
        loss.backward() #Backprop
        optimizer.step()
        counter +=1
    epoch_loss = train_running_loss/counter
    epoch_acc = 100. *(train_running_correct / len(datasetloader.dataset))
    return epoch_loss, epoch_acc

def validate(model, datasetloader, criterion):
    model.eval()
    print('Validating...')
    val_running_loss = 0.0
    val_running_correct = 0
    counter = 0
    with torch.no_grad():
        for i, data in tqdm(enumerate(datasetloader), total=len(datasetloader)):
            image, labels = data
            image = image.to(device)
            labels = labels.to(device)
            outputs = model(image)
            loss = criterion(outputs, labels)
            val_running_loss += loss.item()
            _, pred = torch.max(outputs.data, 1)
            val_running_correct += (pred == labels).sum().item()
            counter += 1  # Increment counter
    epoch_loss = val_running_loss / counter
    epoch_acc = 100. * (val_running_correct / len(datasetloader.dataset))
    return epoch_loss, epoch_acc

train_loss = []
train_acc = []
valid_loss = []
valid_acc = []

for epoch in range(EPOCHS):
    print(f'Epoch {epoch+1} of {EPOCHS}')
    train_epoch_loss, train_epoch_acc = train(model, train_dataset_loader,
                                               optimizer, criterion)
    valid_epoch_loss, valid_epoch_acc = validate(model, valid_dataset_loader, criterion)
    train_loss.append(train_epoch_loss)
    train_acc.append(train_epoch_acc)
    valid_loss.append(valid_epoch_loss)
    valid_acc.append(valid_epoch_acc)
    print(f'Train Loss: {train_epoch_loss:.3f}, Train Accuracy: {train_epoch_acc:.3f}')
    print(f'Validation Loss: {valid_epoch_loss:.3f}, Validation Accuracy: {valid_epoch_acc:.3f}')
    print("."*50)
