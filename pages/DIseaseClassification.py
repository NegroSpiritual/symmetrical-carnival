# # import torch
# # import torch.nn as nn
# # import torch.nn.functional as F
# # from torchvision import transforms
# # from PIL import Image
# # import streamlit as st

# # # Define the neural network architecture
# # class SimpleClassifier(nn.Module):
# #     def __init__(self):
# #         super(SimpleClassifier, self).__init__()
# #         self.conv1 = nn.Conv2d(3, 32, 5)
# #         self.conv2 = nn.Conv2d(32, 64, 5)
# #         self.conv3 = nn.Conv2d(64, 128, 3)
# #         self.conv4 = nn.Conv2d(128, 256, 5)
# #         self.fc1 = nn.Linear(256, 4)
# #         self.pool = nn.MaxPool2d(2, 2)

# #     def forward(self, x):
# #         x = self.pool(F.relu(self.conv1(x)))
# #         x = self.pool(F.relu(self.conv2(x)))
# #         x = self.pool(F.relu(self.conv3(x)))
# #         x = self.pool(F.relu(self.conv4(x)))
# #         bs, _, _, _ = x.shape
# #         x = F.adaptive_avg_pool2d(x, 1).reshape(bs, -1)
# #         x = self.fc1(x)
# #         return x

# # # Load the model
# # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # model = SimpleClassifier().to(device)

# # checkpoint = torch.load('model.pth', map_location=device)
# # model.load_state_dict(checkpoint['state_dict'])
# # model.eval()

# # # Define the preprocessing steps
# # transform = transforms.Compose([
# #     transforms.Resize((224, 224)),
# #     transforms.ToTensor(),
# #     transforms.Normalize(mean=[0.485, 0.456, 0.406],
# #                          std=[0.229, 0.224, 0.225])
# # ])
# # labels = ['balloning', 'cirrhosis', 'inflammation', 'steatosis'] 


# # # Display the web app title
# # st.title("Simple Image Classification Application")

# # # Enable users to upload images for the model to make predictions
# # file_up = st.file_uploader("Upload an image", type="jpg")

# # # Predict the class of the uploaded image
# # if file_up is not None:
# #     image = Image.open(file_up)
# #     st.image(image, caption='Uploaded Image.', use_column_width=True)

# #     # Preprocess the image and make predictions
# #     with st.spinner('Predicting...'):
# #         with torch.no_grad():
# #             input_tensor = transform(image).unsqueeze(0).to(device)
# #             output = model(input_tensor)
# #             _, predicted = torch.max(output, 1)
# #             predicted_class = labels[predicted.item()]

# #     # Display the predicted class label
# #     st.write(f"Predicted class: {predicted_class}")

# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torchvision import transforms
# from PIL import Image
# import streamlit as st

# # Define the neural network architecture
# class SimpleClassifier(nn.Module):
#     def __init__(self):
#         super(SimpleClassifier, self).__init__()
#         self.conv1 = nn.Conv2d(3, 32, 5)
#         self.conv2 = nn.Conv2d(32, 64, 5)
#         self.conv3 = nn.Conv2d(64, 128, 3)
#         self.conv4 = nn.Conv2d(128, 256, 5)
#         self.fc1 = nn.Linear(256, 4)
#         self.pool = nn.MaxPool2d(2, 2)

#     def forward(self, x):
#         x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = self.pool(F.relu(self.conv3(x)))
#         x = self.pool(F.relu(self.conv4(x)))
#         bs, _, _, _ = x.shape
#         x = F.adaptive_avg_pool2d(x, 1).reshape(bs, -1)
#         x = self.fc1(x)
#         return x

# # Load the model
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = SimpleClassifier().to(device)

# checkpoint = torch.load('model.pth', map_location=device)
# model.load_state_dict(checkpoint['state_dict'])
# model.eval()

# # Define the preprocessing steps
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                          std=[0.229, 0.224, 0.225])
# ])
# labels = ['balloning', 'cirrhosis', 'inflammation', 'steatosis']

# # Display the web app title
# st.title("Simple Image Classification Application")

# # Enable users to upload images for the model to make predictions
# file_up = st.file_uploader("Upload an image", type="jpg")

# # Predict the class of the uploaded image
# if file_up is not None:
#     image = Image.open(file_up)
#     st.image(image, caption='Uploaded Image.', use_column_width=True)

#     # Preprocess the image and make predictions
#     with st.spinner('Predicting...'):
#         with torch.no_grad():
#             input_tensor = transform(image).unsqueeze(0).to(device)
#             output = model(input_tensor)
#             _, predicted = torch.max(output, 1)
#             predicted_class = labels[predicted.item()]

#     # Display the predicted class label
#     st.write(f"Predicted class: {predicted_class}")

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import streamlit as st

# Define the neural network architecture
class SimpleClassifier(nn.Module):
    def __init__(self):
        super(SimpleClassifier, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 5)
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 256, 5)
        self.fc1 = nn.Linear(256, 4)
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))
        bs, _, _, _ = x.shape
        x = F.adaptive_avg_pool2d(x, 1).reshape(bs, -1)
        x = self.fc1(x)
        return x

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
labels = ['balloning', 'cirrhosis', 'inflammation', 'steatosis']

# Set the page to be centered and responsive
st.set_page_config(page_title="Disease Classification", page_icon="📈")

st.markdown("#Liver Disease Classification")
st.sidebar.header("Disease Classification")

# Display the web app title
st.title("Liver Disease Classification Web App")

# Enable users to upload images for the model to make predictions
file_up = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

# Predict the class of the uploaded image
if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Preprocess the image and make predictions
    with st.spinner('Predicting...'):
        with torch.no_grad():
            input_tensor = transform(image).unsqueeze(0).to(device)
            output = model(input_tensor)
            _, predicted = torch.max(output, 1)
            predicted_class = labels[predicted.item()]

   
    # Display the predicted class label
    st.markdown(f"<h3 style='text-align: center; color: #000000;'>This Cell is infected with: {predicted_class.capitalize()}</h3>", unsafe_allow_html=True)
