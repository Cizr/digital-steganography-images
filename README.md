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

