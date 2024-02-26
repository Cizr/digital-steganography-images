import heapq
import re
import pickle

class Node:
    def __init__(self, ch, freq, left=None, right=None):
        """
        Initializes a Node with character ch, frequency freq, left and right child nodes.
        Args:
        - ch: a character (can be None for internal nodes)
        - freq: an integer representing the frequency of the character in the input text
        - left: left child node (default: None)
        - right: right child node (default: None)
        """
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        """
        Overrides the less than function to make `Node` work with priority queue.
        It ensures that the highest priority item has the lowest frequency.
        """
        return self.freq < other.freq

def isLeaf(root):
    """
    Check if the given node is a leaf node in a binary tree.
    Parameters:
    - root (Node): The root node of the binary tree
    Returns:
    - bool: True if the given node is a leaf node, False otherwise
    """
    return root.left is None and root.right is None

def encode(root, s, huffman_code):
    """
    Traverse the Huffman Tree and store Huffman Codes in a dictionary.
    Parameters:
    - root: The root node of the Huffman Tree.
    - s: A string variable which keeps track of the current Huffman code.
    - huffman_code: A dictionary to store the Huffman codes of each character.
    """
    if root is None:
        return

    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)

def encodeHuffman(text):
    """
    Encode a given string using the Huffman coding algorithm.
    Parameters:
    - text (str): The string to be encoded
    """
    if len(text) == 0:
        return

    # Create a frequency dictionary for each character in the text
    freq = {i: text.count(i) for i in set(text)}

    # Save the frequency dictionary to a file using pickle
    with open('freq_data.pkl', 'wb') as f:
        pickle.dump(freq, f)

    # Create a priority queue to store the live nodes of the Huffman tree
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    # Build the Huffman tree
    while len(pq) != 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        total = left.freq + right.freq
        heapq.heappush(pq, Node(None, total, left, right))

    # Get the root of the Huffman tree
    root = pq[0]

    # Traverse the Huffman tree and store the Huffman codes in a dictionary
    huffmanCode = {}
    encode(root, '', huffmanCode)

    # Encode the given text using the Huffman codes
    encoded_text = ''.join(huffmanCode[c] for c in text)

    # Print a message indicating that encoding is done
    print("Encoding Done!")

    # Save the generated encoded string to a file
    with open('coded.txt', 'w') as f:
        f.write(encoded_text)

def decodeHuffman(encodedString, freq):
    """
    Decode a given Huffman encoded string using the frequency table.
    Parameters:
    - encodedString: The string to be decoded
    - freq: The frequency table of characters used to encode the string
    Returns:
    - str: The decoded string
    """
    # Construct priority queue using the frequency table
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    # Reconstruct Huffman tree using the priority queue
    while len(pq) != 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        total = left.freq + right.freq
        heapq.heappush(pq, Node(None, total, left, right))

    # Get root node of Huffman tree
    root = pq[0]
    decodedString = ""

    # Traverse the Huffman tree to decode the encoded string by moving left or right depending on the current bit
    index = -1
    while index < len(encodedString) - 1:
        current = root
        while not isLeaf(current):
            index += 1
            current = current.left if encodedString[index] == '0' else current.right
        decodedString += current.ch

    return decodedString

# Huffman coding algorithm implementation in Python
if __name__ == '__main__':
    process = input("Enter 1 for Encoding, Enter 2 for Decoding: ")

    if process == '1':
        textfile = input("Enter text file with the data in .txt format: ")
        text = ''
        with open(textfile, 'r') as file:
            # Read the text from the file and convert to lowercase
            text = file.read().lower()
        # Replace consecutive spaces with a single space
        text = re.sub('\s{2,}', ' ', text)
        # Remove newlines and new paragraphs
        text = re.sub('\n|\r\n|\r|\n\n+', ' ', text)

        encodeHuffman(text)

    elif process == '2':
        textfile = input("Enter file with the binary encrypted data in .txt format: ")
        freqfile = input("Enter file with the frequency data in .pkl format: ")

        # Load the encrypted data from the file
        with open(textfile, "r") as f:
            encr_data = f.read()
        # Load the frequency data from the file using pickle
        with open(freqfile, 'rb') as f:
            freq = pickle.load(f)

        # Decode the Huffman encoded data
        deco_data = decodeHuffman(encr_data, freq)

        # Save the decoded data to a file
        with open('deco-txt.txt', 'w') as decoded:
            decoded.write(deco_data)

        print('Data Decoded and saved in .txt file!')

    else:
        print("Please Enter a valid input!!")
