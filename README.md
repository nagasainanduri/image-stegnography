# Image Steganography

## Problem Statement
Steganography involves embedding secret data within a digital image to ensure secure and imperceptible transmission. The problem is to develop a method that maximizes data hiding capacity while maintaining the image quality and ensuring robustness against detection and extraction attempts. The approach must balance between effective data concealment and minimal distortion of the original image. This method should also be computationally efficient and adaptable to various types of image formats.

## Technologies Used
- Python
  - Libraries: OpenCV, NumPy, Pillow, Cryptography

## Basic Functionalities

### Encoding
The encoding functionality allows users to embed secret data into a digital image. This process involves selecting an image and the data to be hidden. The script uses advanced algorithms to ensure that the data is embedded in a way that is imperceptible to the human eye, maintaining the original image quality.

### Decoding
The decoding functionality retrieves the hidden data from the encoded image. This feature ensures that the extracted data is accurate and intact, providing a reliable method for data retrieval without compromising the image's integrity.

## How to Use ?

1. **Installation**: Ensure you have Python installed on your system. Install the required libraries using pip. Below are the installation methods for different operating systems:

   - **Windows**:
     1. Download and install Python from the [official website](https://www.python.org/downloads/windows/).
     2. Open Command Prompt and run:
        ```bash
        pip install opencv-python numpy pillow cryptography
        ```

   - **Linux**:
     1. Install Python using your package manager, e.g., for Ubuntu:
        ```bash
        sudo apt update
        sudo apt install python3 python3-pip
        ```
     2. Run the following command in the terminal:
        ```bash
        pip3 install opencv-python numpy pillow cryptography
        ```

   - **macOS**:
     1. Install Python using Homebrew:
        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install python
        ```
     2. Run the following command in the terminal:
        ```bash
        pip3 install opencv-python numpy pillow cryptography
        ```

2. **Encoding Data**:
   - Run the encoding script.
   - Provide the path to the image and the data you wish to encode.
   - The script will output a new image file with the embedded data.

3. **Decoding Data**:
   - Run the decoding script.
   - Provide the path to the encoded image.
   - The script will extract and display the hidden data.

This project provides a robust and efficient method for secure data transmission using image steganography, ensuring both high data hiding capacity and minimal image distortion.
