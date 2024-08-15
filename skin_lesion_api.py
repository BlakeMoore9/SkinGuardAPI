from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
import io

# List of labels for predictions
labels = [
    "Precancerous Lesions: Actinic Keratoses and Intraepithelial Carcinoma",
    "Malignant Tumor: Basal Cell Carcinoma",
    "Benign Keratoses",
    "Dermatofibroma: Benign",
    "Malignant Tumor: Melanoma",
    "Benign Skin Lesion: Melanocytic Nevi",
    "Benign Vascular Lesion"
]

app = FastAPI()

# Allowed file types for uploads
ALLOWED_TYPES = ["image/jpeg", "image/png"]

# Path to the model
MODEL_PATH = "./model/best_weights.h5"
model = load_model(MODEL_PATH)

def resize_and_pad_image(img, desired_size=224) -> Image:
    """
    Resize the image to the desired size while maintaining its original aspect ratio.
    Pad the image with black pixels if it's not square.
    
    Parameters:
    - img (PIL.Image): Input image.
    - desired_size (int): The size to resize the shortest side of the image to.

    Returns:
    - PIL.Image: Resized and padded image.
    """
    # Calculate aspect ratio of the original image
    aspect_ratio = img.width / img.height
    new_width = int(desired_size * aspect_ratio)
    new_height = desired_size

    # Resize the image while maintaining the aspect ratio
    img_resized = img.resize((new_width, new_height), Image.BICUBIC)

    # Pad the image to make it square
    img_padded = ImageOps.expand(img_resized, (0, 0, desired_size - new_width, 0), fill='black')

    # Convert RGBA images to RGB
    if img_padded.mode == "RGBA":
        img_padded = img_padded.convert("RGB")

    return img_padded

def prepare_image_for_prediction(img_data):
    """
    Load, preprocess, and prepare an image for prediction.
    
    Args:
        img_data (bytes): Image data in bytes.
    
    Returns:
        numpy.ndarray: Preprocessed image ready for model prediction.
    """
    # Load the image
    img = Image.open(io.BytesIO(img_data))
    
    # Convert the image to RGB format (this drops the alpha channel if it exists, in png for example)
    img = img.convert("RGB")
    
    # Resize and pad the image
    img_padded = resize_and_pad_image(img)
    
    # Convert the image to an array and expand its dimensions
    img_array = np.expand_dims(img_to_array(img_padded), axis=0)
    
    # Apply the preprocess_input function specific to ResNet-50
    preprocessed_img = preprocess_input(img_array)
    
    return preprocessed_img


@app.get("/")
def read_root() -> FileResponse:
    """Serve the main HTML page."""
    return FileResponse("index.html")

@app.post("/upload/")
async def upload_image(file: UploadFile = UploadFile(...)) -> JSONResponse:
    """
    Endpoint to upload an image and get a prediction.

    Parameters:
    - file (UploadFile): Image file uploaded by the user.

    Returns:
    - JSONResponse: Predicted class and confidence.
    """
    try:
        # Check if the uploaded file type is supported
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(detail=f"File type not supported: {file.content_type}", status_code=415)

        # Read the image data from the uploaded file
        image_data = await file.read()

        # Preprocess the image for prediction
        preprocessed_img = prepare_image_for_prediction(image_data)
        
        # Get model predictions
        predictions = model.predict(preprocessed_img)

        # Extract the class with the highest prediction confidence
        predicted_class = np.argmax(predictions[0])
        predicted_label = labels[predicted_class]
        predicted_probability = predictions[0][predicted_class]

        return JSONResponse(content={"predicted_class": predicted_label, "confidence": float(predicted_probability)}, status_code=200)

    except Exception as e:
        # Print error for debugging and raise an HTTP exception
        print(f"Error: {e}")
        raise HTTPException(detail=str(e), status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
