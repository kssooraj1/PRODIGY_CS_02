import numpy as np
from PIL import Image

class ImageEncryptionTool:
    def __init__(self):
        self.key = 123  # encryption key

    def encrypt_image(self, image_path):
        image = Image.open(image_path)
        pixels = np.array(image)

        # Apply encryption operation: swap red and blue channels
        encrypted_pixels = pixels.copy()
        encrypted_pixels[:, :, 0], encrypted_pixels[:, :, 2] = pixels[:, :, 2], pixels[:, :, 0]

        encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
        encrypted_image.save("encrypted_image.png")

    def decrypt_image(self, image_path):
        image = Image.open(image_path)
        pixels = np.array(image)

        # Apply decryption operation: swap red and blue channels (reverse of encryption)
        decrypted_pixels = pixels.copy()
        decrypted_pixels[:, :, 0], decrypted_pixels[:, :, 2] = pixels[:, :, 2], pixels[:, :, 0]

        decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
        decrypted_image.save("decrypted_image.png")

def main():
    tool = ImageEncryptionTool()

    print("1. Encrypt image")
    print("2. Decrypt image")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        image_path = input("Enter the image path: ")
        tool.encrypt_image(image_path)
        print("Image encrypted successfully!")
    elif choice == 2:
        image_path = input("Enter the encrypted image path: ")
        tool.decrypt_image(image_path)
        print("Image decrypted successfully!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
