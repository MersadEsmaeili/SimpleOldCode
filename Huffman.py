from heapq import heappush, heappop, heapify
from collections import defaultdict

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Count the frequency of each character in the text
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    # Create a priority queue (min heap) and push all nodes into it
    heap = []
    for char, freq in freq_dict.items():
        node = Node(char, freq)
        heappush(heap, node)

    # Merge nodes until only one node is left (the root of the Huffman Tree)
    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heappush(heap, merged)

    # Return the root of the Huffman Tree
    return heappop(heap)

# Function to traverse the Huffman Tree and build the Huffman codes
def build_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.char:
            codes[node.char] = code
            return

        traverse(node.left, code + '0')
        traverse(node.right, code + '1')

    traverse(root, '')

    return codes

# Function to encode text using Huffman codes
def huffman_encode(text, codes):
    encoded_text = ''
    for char in text:
        encoded_text += codes[char]
    return encoded_text

# Function to decode encoded text using Huffman codes
def huffman_decode(encoded_text, root):
    decoded_text = ''
    node = root

    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_text += node.char
            node = root

    return decoded_text


# Get user input
text = input("Enter the text: ")

# Build Huffman Tree
huffman_tree = build_huffman_tree(text)

# Build Huffman codes
huffman_codes = build_huffman_codes(huffman_tree)

# Encode text using Huffman codes
encoded_text = huffman_encode(text, huffman_codes)
print("Encoded text:", encoded_text)

# Decode encoded text using Huffman codes
decoded_text = huffman_decode(encoded_text, huffman_tree)
print("Decoded text:", decoded_text)
