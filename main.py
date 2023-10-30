import cv2
import pytesseract
from aadhaar_read import front_data, back_data
import numpy as np


if __name__ == "__main__":
    #Replace with tesseract path on your system
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    #Replace with path of Front pic of Aadhaar
    aadhaar_front_img_path = r"Front_Sample.jpg"
    #Replace with path of Back pic of Aadhaar
    aadhaar_back_img_path = r"Back_Sample.jpg"

    # Path to aadhaar front image
    img = cv2.imread(aadhaar_front_img_path)

    # Convert to GrayScale
    gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Create a binary mask for dark black regions
    mask = gr <= 180
    # Create an all-white image
    gray = np.ones_like(gr) * 255
    # Apply the mask to keep dark black regions
    gray[mask] = gr[mask]
    # getting all values (except address) from Front Aadhaar Card Image
    regex_name,regex_gender,regex_dob,regex_aadhaar_number = front_data(gray)
    regex_name = " ".join(regex_name[:3])
    print("Name :", regex_name)
    print("Gender :",regex_gender)
    print("DOB/Year :",regex_dob)
    print("Aadhaar Number :",regex_aadhaar_number)
    
    # path to aadhaar back image (address side)
    img = cv2.imread(aadhaar_back_img_path)
    gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Create a binary mask for dark black regions
    mask = gr <= 180
    # Create an all-white image
    gray = np.ones_like(gr) * 255
    # Apply the mask to keep dark black regions
    gray[mask] = gr[mask]
    # Keep only the english address part of the image, below we kept only right half
    crop_img = gray[:, int(gray.shape[1]/2):]
    # getting address back
    regex_address = back_data(crop_img)
    print("Address :", regex_address)