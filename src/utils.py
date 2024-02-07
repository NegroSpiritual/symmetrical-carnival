import os
import shutil
import random
from PIL import Image
import matplotlib.pyplot as plt
import torch

def display_images(directory: str):
    #Display images from the train dataset 
    # Get the list of image files in the directory
    image_files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Randomly select 'num_images' images
    selected_images = random.sample(image_files, min(6, len(image_files)))

    # Display each selected image
    for image_file in selected_images:
        image_path = os.path.join(directory, image_file)
        img = Image.open(image_path)
    # Display image using Matplotlib
        plt.imshow(img)
        plt.title(image_file)
        plt.axis('off')  # Turn off axis labels
        plt.show()

def create_folder_and_move_files(file_list_path:str, folder_path:str):
    """
    Used to organize data with a given file list and folder name.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")

    # Read the list of file names from the text file
    with open(file_list_path, 'r') as file:
        file_names = file.read().splitlines()

    # Move the files to the new folder
    for file_name in file_names:
        source_path = os.path.abspath(file_name)
        destination_path = os.path.join(folder_path, os.path.basename(file_name))

        try:
            shutil.move(source_path, destination_path)
            print(f"File '{file_name}' moved to '{folder_path}'.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found in the current directory.")
        except (PermissionError, shutil.Error) as e:
            print(f"Error moving '{file_name}': {e}")

    print("All files moved successfully.")

def save_model(epochs, model, optimizer, criterion):
    torch.save({
        'epoch': epochs,
        'state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss':criterion
    }, 'outputs/model.pth')

def save_plots(train_acc, valid_acc, train_loss, valid_loss):
    """
    Function to save the loss and accuracy plots to disk.
    """
    # accuracy plots
    plt.figure(figsize=(10, 7))
    plt.plot(
        train_acc, color='green', linestyle='-', 
        label='train accuracy'
    )
    plt.plot(
        valid_acc, color='blue', linestyle='-', 
        label='validataion accuracy'
    )
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('outputs/accuracy.png')
    
    # loss plots
    plt.figure(figsize=(10, 7))
    plt.plot(
        train_loss, color='orange', linestyle='-', 
        label='train loss'
    )
    plt.plot(
        valid_loss, color='red', linestyle='-', 
        label='validataion loss'
    )
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('outputs/loss.png')