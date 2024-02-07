from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import torch
from torchvision import transforms
from PIL import Image

router = APIRouter(
    tags=['CORE'],
    prefix="/core"
)

# Load your PyTorch model
model = torch.load("model.pth", map_location=torch.device('cpu'))  # Load your trained model
model.eval()

# Define image preprocessing transforms
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load class labels (if applicable)
class_labels = ["steatosis", "cirrhosis", "inflammation", "balloning"]  # Replace with your actual class labels

def get_predicted_label(output):
    # Perform post-processing to get the predicted class label
    _, predicted_idx = torch.max(output, 1)
    predicted_label = class_labels[predicted_idx.item()]
    return predicted_label

@router.post("/upload/")
def upload_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a temporary location
        with open(f"temp/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Load and preprocess the uploaded image
        image = Image.open(f"temp/{file.filename}")
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)  # Add batch dimension
        
        # Perform inference using the model
        with torch.no_grad():
            output = model(input_batch)
        
        # Get the predicted class label
        predicted_label = get_predicted_label(output)
        
        # Return the inference result with the predicted class label
        return JSONResponse(content={"message": "Upload successful", "predicted_label": predicted_label}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)
