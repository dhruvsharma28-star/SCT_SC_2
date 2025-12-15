from PIL import Image
import random

def encrypt_decrypt_image(input_path, output_path, key=99):
    img = Image.open(input_path)
    pixels = list(img.getdata())

    encrypted_pixels = []

    for pixel in pixels:
        # If pixel is a single value (grayscale)
        if isinstance(pixel, int):
            encrypted_pixels.append(pixel ^ key)

        # If pixel is RGB or RGBA
        else:
            encrypted_pixels.append(
                tuple(channel ^ key for channel in pixel)
            )

    # Shuffle pixel positions
    random.seed(key)
    random.shuffle(encrypted_pixels)

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(encrypted_pixels)
    new_img.save(output_path)

    print("Image processed successfully!")


# -------- RUN HERE --------
encrypt_decrypt_image("image.png", "encrypted.png", key=99)