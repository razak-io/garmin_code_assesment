## Reasoning: 
The data is encoded using an implementation of Huffmans encoding which works as described below. 

This encoding algorithm was chosen due to the nature of the input data which could have duplicate values. 

In this encoding schema the number of bits used for encoding varies with frequency, with less frequently occurring characters using more bits and more frequently occurring characters using less bits. In this way, we can encode in such a way that uses the minimum numer of bits (approximately).

## The program works as follows:

### Step 1: Preprocessing
This first step of this algorithm involves counting the number of unique characters in the byte array. And keeping track of the characters and their frequencies in the Node objects which we will use in later steps

### Step 2: Create Huffman Tree
This process involves building a tree using the node list. Here the nodes are put inside a minimum priority heap with the nodes with the least counts being at the top. Then the following happens; The two nodes at the top of the heap are popped and a new node is created with these two as its left and right children. This node is not assigned a character however its count is equal to the sum of the count of its children’s nodes. And then this node is pushed on the heap again. This process continues until the we iterate over all the nodes and then the node at the head is returned.

### Step 3: Generate Code 
Here, the Huffman tree is used to generate prefix codes and it does this recursively. The tree is traversed as follows, at each step, if a node has a left child then the code of the left child will be updated by adding a 0 to the code of the node and then we recurse again for that node. If a node has a right child, the same steps are taken but instead of appending a 0, we append a 1. If we hit a node with no children, then we set its code to the code passed by the parent.

### Step 4: Encoding of the Byte Array
In this process, the prefix codes generated using Steps 1 to 3 are used to encode the file. The file is encoded as follows; for each item in the byte array, index the code_map and append the code at that index into the encoded array in place of that character

### Step 5: Decoding of Byte Array
This is similar to the encoding process with the main difference being that the rev_code_map (Note here the prefix code serve as the keys)
