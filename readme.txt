The ImageEncryptionTool class has two methods: encrypt_image and decrypt_image.
The encrypt_image method opens an image, converts it to a numpy array, and applies a simple encryption operation: it swaps the red and blue channels of each pixel. The encrypted image is then saved to a new file.
The decrypt_image method does the opposite: it swaps the red and blue channels of each pixel (reverse of encryption) to recover the original image.
The main function provides a simple menu for the user to choose between encrypting and decrypting an image. It prompts the user for the image path and calls the appropriate method.
This program assumes that the image is in the same directory as the script. You can modify the image_path variable to specify a different directory or file path.

Note that this is a very basic encryption scheme and is not secure for practical use. In a real-world scenario, you would want to use a more robust encryption algorithm, such as AES, and a secure key management system.
