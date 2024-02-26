# digital-steganography-images
A Python-based tool for concealing confidential information within images. embed and extract data seamlessly, adding an extra layer of privacy to your images. 

## Project Overview

This project focuses on enhancing data encoding and compression through the implementation of key features:

### Huffman Encoding and Compression:

A dedicated program has been added to handle Huffman encoding and compression for any .txt file.
This program ensures a higher compression ratio after encoding by sanitizing the input.

### Color Image Support:

The Histogram Shift algorithm has been upgraded to support encoding not only in grayscale but also in color image formats.
RGB channels (R, G, B) are utilized, increasing data capacity for hidden information.

### Versatile Cover Image Handling:

The program now offers options to encode, decode, or check the capacity of a given cover image.
Users can select the optimal cover image based on the amount of data to be concealed.

### Key Files for Decoding:

For Huffman encoding, a frequency table is saved, serving as a key for decoding binary-encoded data.
For Histogram Shift encoding, an enc_data.pkl file is saved, acting as a key to decode the encrypted image.

These improvements enhance the project's functionality and efficiency, making it adaptable for various data-hiding scenarios.

## Getting Started

Follow these steps to set up the project on your local machine:

```bash
# Update PIP
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

## Huffman.py
huffman.py file within this folder serves a pivotal role in implementing the Huffman Encoding and Compression algorithm. Its primary function is to generate a frequency table for a given input text file and subsequently construct a Huffman tree using a priority queue. This tree is then utilized to encode the specified secret text into binary format efficiently. Beyond encoding, the huffman.py file possesses the capability to decode an encoded binary back into plain text, leveraging the frequency information obtained during the encoding process.
Upon execution, the huffman.py file presents two distinct options:

Encoding:
Parameters: Accepts a text file containing the secret message that requires encoding.
Return: The encoded binary is saved in a .txt file, accompanied by the preservation of the frequency table, essential for decoding purposes.
![image (1)](https://github.com/Cizr/digital-steganography-images/assets/100844208/e5f30872-e137-47e9-a4af-fae0dd3763ef)

## histogram_shifting.py
histogram_shifting.py file, an integral component of this project, is dedicated to encoding a provided binary string from a .txt file into a cover image. The cover image can be in any format, with .png being recommended for optimal encoding capacity and desired output quality. When supplied with the binary string and cover image, the program efficiently generates an encoded image in .png format. It further preserves the enc_data.pkl file, essential for subsequent decoding of the encoded image. Notably, the .py file is not solely focused on encoding; it also possesses the capability to decode a given encoded image along with the provided enc_data.pkl file. During decoding, the program retrieves the binary-encoded text from the image and saves it into a .txt file. Upon execution,.py file offers three distinct options:

Encoding: Parameters: Accepts a text file containing the binary string to be encoded and the cover image.
  Return: Generates an encoded image and saves the enc_data.pkl file, containing necessary data for decoding.
Decoding: Parameters: Requires an encoded image and the corresponding enc_data.pkl file for decoding.
  Return: Retrieves the decoded binary and saves it into a .txt file.
![image (2)](https://github.com/Cizr/digital-steganography-images/assets/100844208/1bb0ce70-9c3a-4c7d-b8ba-64fe77c7ffd2)

