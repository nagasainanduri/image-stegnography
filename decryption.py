import cv2
import os
import tkinter as tk
from tkinter import filedialog


def select_file(file_type_description, file_extensions):
    """Opens a file dialog for the user to select a file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title=f"Select {file_type_description}",
        filetypes=[(file_type_description, file_extensions)],
    )
    root.destroy()
    return file_path


def decrypt_image(image_path, original_msg_length):
    """Extracts hidden text from an image based on pixel values."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load the image.")
        return None

    char_map = {i: chr(i) for i in range(256)}
    message = ""
    n, m, z = 0, 0, 0

    for i in range(original_msg_length):
        char_value = img[n, m, z]
        if char_value in char_map:
            message += char_map[char_value]
        else:
            print(f"Warning: Unexpected pixel value [{n}, {m}, {z}] = {char_value}")
            return None

        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
                if n >= img.shape[0]:
                    break

    return message


def main_decrypt():
    """Main function to handle decryption process."""
    image_path = select_file("Encrypted Image", "*.png *.jpg *.jpeg")
    if not image_path:
        print("No image selected. Exiting...")
        return

    password_file_path = select_file("Password File", "*.txt")
    if not password_file_path:
        print("No password file selected. Exiting...")
        return

    try:
        with open(password_file_path, "r", encoding="utf-8") as f:
            password = f.read().strip()
    except Exception as e:
        print(f"Error reading password file: {e}")
        return

    pas = input("Enter passcode for decryption: ").strip()

    if pas != password:
        print("❌ ERROR: Incorrect passcode!")
        return

    try:
        original_msg_length = int(input("Enter the length of the original message: "))
    except ValueError:
        print("Error: Invalid input for message length.")
        return

    decrypted_message = decrypt_image(image_path, original_msg_length)
    if decrypted_message:
        print("\n✅ Decrypted message:\n", decrypted_message)

        # Save decrypted message in the same directory as the encrypted image
        image_directory = os.path.dirname(image_path)
        output_file = os.path.join(image_directory, "decrypted_message.txt")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(decrypted_message)

        print(f"\n💾 Decrypted message saved to '{output_file}'")
    else:
        print("⚠️ Decryption failed. Message might be corrupted.")


if __name__ == "__main__":
    main_decrypt()
