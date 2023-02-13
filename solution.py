# Huffman Encoding
import heapq

class Node:
    byte = None               
    left = None           
    right = None      
    count = 0
    code = ''
    
    def __init__(self,byte):
        self.byte =  byte;

    def __lt__(self, other):
        return self.count < other.count

    def __repr__(self):
        return str("Node") + str(self.__dict__)
        
    def __str__(self):
        return str("Node") + str(self.__dict__)


class HuffmanCoding:
    __code_map = {}
    __rev_code_map ={}

    def __count_byte(self, data):
        nodes = {byte :  Node(byte) for byte in set(data)}
        for byte in data:
            nodes[byte].count += 1
            
        huffman_nodes = sorted(nodes.values(), key=lambda Node: Node.count)
        return huffman_nodes
    
    def __build_huffman_tree(self, huffman_nodes):
        heapq.heapify(huffman_nodes)    
        
        n = len(huffman_nodes)
        for i in range(n-1):
            new_node = Node(None)
            new_node.left=(heapq.heappop(huffman_nodes))
            new_node.right=(heapq.heappop(huffman_nodes))
            new_node.count = new_node.left.count + new_node.right.count 
            heapq.heappush(huffman_nodes,new_node)
            
        return  heapq.heappop(huffman_nodes)
    
    def __generate_huffman_code(self, tree_node, code = '0b'):
        if (tree_node.left == None and tree_node.right == None):
            tree_node.code = code
            self.__code_map[tree_node.byte] = tree_node.code
            self.__rev_code_map[tree_node.code] = tree_node.byte
        else:
            self.__generate_huffman_code(tree_node.left,code + '0')
            self.__generate_huffman_code(tree_node.right,code + '1')

    def init_huffman_codes(self, data):
        if not data:
            raise ValueError('No data to generate codes with')
        nodes = self.__count_byte(data)
        root  = self.__build_huffman_tree(nodes)
        self.__generate_huffman_code(root)

    def byte_compress(self, data):
        if not self.__code_map:
            raise ValueError('Huffman Codes have not been initialized')
        
        encoded = []
        for byte in data:
            if byte in self.__code_map.keys():    
                encoded.append(self.__code_map[byte])
            else:
                raise ValueError(f'Invalid value passed: {byte}')
        return encoded
    
    def byte_decompress(self, compressed_data):
        if not self.__rev_code_map:
            raise ValueError('Huffman Codes have not been initialized')
            
        decoded = []
        for data in compressed_data:
            if data in self.__rev_code_map.keys():            
                decoded.append(self.__rev_code_map[data])
            else:
                raise ValueError(f'Invalid Code passed: {data}')
        return decoded

# Testing
data = bytes([0x03, 0x74, 0x04, 0x04, 0x04, 0x35, 0x35, 0x64, 
              0x64, 0x64, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x56, 0x45, 0x56, 0x56, 0x56, 0x09, 0x09, 0x09])

print('Original Data: ')
print(data)

huff = HuffmanCoding()
huff.init_huffman_codes(data)

print('\nEncoded Data: ')
compressed_bytes = huff.byte_compress(data)
print (compressed_bytes)

print('\nDecoded Data: ')
decompressed_bytes = huff.byte_decompress(compressed_bytes)
print(bytes(decompressed_bytes))

assert data == bytes(decompressed_bytes)
