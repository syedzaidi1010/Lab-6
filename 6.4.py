from skimage.metrics import structural_similarity as ssim
import cv2

original_image = cv2.imread(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hh.tif", 0)
denoised_image = cv2.GaussianBlur(original_image, (5, 5), 0)

ssim_value = ssim(original_image, denoised_image)
print(f"Structural Similarity Index (SSIM): {ssim_value}")
