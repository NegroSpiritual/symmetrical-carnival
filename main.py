from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from torchvision import transforms
from PIL import Image
import torch, torch.nn as nn, torch.nn.functional as F
import json

class SimpleClassifier(nn.Module):
    def __init__(self):
        super(SimpleClassifier, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 5)
        self.conv2 = nn.Conv2d(32,64, 5)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 256, 5)

        self.fc1 = nn.Linear(256, 4)
        self.pool = nn.MaxPool2d(2,2)

    def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = self.pool(F.relu(self.conv3(x)))
            x = self.pool(F.relu(self.conv4(x)))

            bs , _ , _, _ = x.shape
            x = F.adaptive_avg_pool2d(x, 1).reshape(bs, -1)
            x = self.fc1(x)
            return x

labels = ['balloning', 'cirrhosis', 'inflammation', 'steatosis']

# Load the model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleClassifier().to(device)

checkpoint = torch.load('model.pth', map_location=device)
model.load_state_dict(checkpoint['state_dict'])
model.eval()

# Define the preprocessing steps
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
])

# Create the FastAPI app
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the FastAPI route
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Load and preprocess the input image
    input_image = Image.open(file.file)
    input_tensor = transform(input_image).to(device)  # Move input tensor to the same device as the model

    # Expand the input tensor to form a batch
    input_batch = input_tensor.unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        output = model(input_batch)

    # Get the predicted class
    _, predicted = torch.max(output, 1)

    # Get the class label
    predicted_class = labels[predicted.item()]

    return {"predicted_class": predicted_class}
# Run the FastAPI app
