import numpy as np
import cv2

def mse(image1, image2):
    return np.mean((image1 - image2) ** 2)

original_image = cv2.imread(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hh.tif", 0)
denoised_image = cv2.GaussianBlur(original_image, (5, 5), 0)

mse_value = mse(original_image, denoised_image)
print(f"Mean Squared Error: {mse_value}")
