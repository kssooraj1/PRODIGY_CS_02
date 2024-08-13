The ImageEncryptionTool class has two methods: encrypt_image and decrypt_image.
The encrypt_image method opens an image, converts it to a numpy array, and applies a simple encryption operation: it swaps the red and blue channels of each pixel. The encrypted image is then saved to a new file.
The decrypt_image method does the opposite: it swaps the red and blue channels of each pixel (reverse of encryption) to recover the original image.
The main function provides a simple menu for the user to choose between encrypting and decrypting an image. It prompts the user for the image path and calls the appropriate method.
