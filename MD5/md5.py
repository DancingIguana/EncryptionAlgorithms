"""
Implementation references:

https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/064_md5_a_broken_secure_hash_algorithm_python_implementation/md5.py
https://en.wikipedia.org/wiki/MD5
https://www.comparitech.com/blog/information-security/md5-algorithm-with-examples/
"""

from io import BytesIO
from typing import BinaryIO
from typing import List
import numpy as np

# Each block has 512 bits = 64 bytes
byte_block_size = 64

# Standard initial vectors for MD5 implementation
initial_vectors = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)

# Standard shift values per round
shift_value_per_round = [
    [7,12,17,22]*4,
    [5,9,14,20]*4,
    [4,11,16,23]*4,
    [6,10,15,21]*4
]

# Standard randomness defined by sine function
sines = np.abs(np.sin(np.arange(64) + 1))  
sine_randomness = [int(x) for x in np.floor(2 ** 32 * sines)]


def left_rotate(x:int, shift_value:int) -> int:
    """
    Bit oeration for cyclic rotation to the left
    """
    return ((x << (shift_value & 31)) | ((x & 0xffffffff) >> (32 - (shift_value & 31)))) & 0xffffffff

def bit_not(x: int) -> int:
    """
    bit not operation substitution, ~b doesn't work properly for some reason.
    """
    return 4294967295 - x

"""
MD5 bit mixing operations
"""

def F(b:int, c:int, d:int) -> int:
    return (b & c) | ((bit_not(b) & d))

def G(b:int ,c:int ,d:int) -> int:
    return (d & b) | (bit_not(d) & c)

def H(b:int, c:int, d:int) -> int:
    return b ^ c ^ d

def I(b:int, c:int, d:int) -> int:
    return c ^ (b | bit_not(d))

mixer_for_round = [F,G,H,I]


"""
MD5 predefined permutations for reading integers
"""
# Predefined order of byte reading for MD5
round_1_perm = [i for i in range(16)]
round_2_perm = [(5*i + 1) % 16 for i in range(16)]
round_3_perm = [(3*i + 5) % 16 for i in range(16)]
round_4_perm = [(7*i) % 16 for i in range(16)]

msg_perm_for_round = [round_1_perm,round_2_perm,round_3_perm,round_4_perm]


def bytes2int_64_16(byte_chunk:bytearray) -> List[int]:
    """
    Given a bytearray of 64 bytes, return a list of 16 integers
    (in hex)
    """
    # Make sure to have byte chunks of size 64 = 512 bits
    #assert len(byte_chunk) == byte_block_size
    
    # Each chunk represents a total of 16 integers (words)
    # each 64/16 = 4 bytes represent 1 integer in the chunk
    ints = [int.from_bytes(byte_chunk[i:i+4],byteorder="little") for i in range(0, len(byte_chunk), 4)]
    #assert(len(ints) == 16)
    return ints

class MD5State:
    def __init__(self, msg):
        self.vectors: tuple[int,int,int,int] = initial_vectors
        self.msg_string = msg
        self.msg_bytes = bytearray(msg.encode())

    def get_int_from_bytes(self):
        return b''.join(x.to_bytes(length=4, byteorder='little') for x in self.vectors)
    
    def get_hex_int_from_bytes(self):
        return self.get_int_from_bytes().hex()

    def padding(self):
        # There must be 512 bits = 64 bytes = 16 integers per chunk
        #msg_ints = bytes2int_64_16(byte_chunks)}
        original_byte_length = len(self.msg_bytes)

        #Always append 1 at the end of the original stream
        self.msg_bytes.append(0x80)
        
        if original_byte_length % 62 == 0 and original_byte_length > 0:
            self.msg_bytes.append(0x00)
            chunk_bit_size = ((62*8) % (2**64))
            self.msg_bytes += bytearray(64)
            self.msg_bytes[-8:] = chunk_bit_size.to_bytes(length = 8, byteorder = "little")
            return
        
        # Check the length and pad with 0s until we have a chunk of size 512 bits 
        # = 64 bytes
        last_chunk_size = len(self.msg_bytes) % 64

        #0s padding
        padding_bytearray = bytearray(64 - last_chunk_size)
        self.msg_bytes += padding_bytearray

        # The last 8 bytes are reserved for the length of the original stream
        bit_length = (original_byte_length*8) % (2**64)
        self.msg_bytes[-8:] = bit_length.to_bytes(length = 8, byteorder = "little")

        return 

    def md5_loop(self):
        # 64 bytes = 512 bits per iteration
        num_iters = len(self.msg_bytes) // 64
        for i in range(num_iters):
            self.md5_step(self.msg_bytes[64*i : 64*i+64])

    def md5_step(self, msg_chunk: bytearray):
        # Get the 16 int values from the 64 byte (512 bits) chunk
        msg_ints = bytes2int_64_16(byte_chunk=msg_chunk)
        # Get the initial vectors from the state

        a, b, c, d = self.vectors
        # There are 4 rounds
        counter = 0
        for round_ in range(4):
            # In each round, there are 16 steps
            bit_mixer = mixer_for_round[round_]

            for i in range(16):
                
                int_idx = msg_perm_for_round[round_][i]
                #print("a1",a)
                #print(a,bit_mixer(b,c,d),msg_ints[int_idx],sine_randomness[counter])
                a = (a + bit_mixer(b,c,d) + msg_ints[int_idx] + sine_randomness[counter]) % (2**32)
                #print("a2",a)
                a = left_rotate(x = a, shift_value=shift_value_per_round[round_][i])
                #print("a3",a)
                a = (a+b) % (2**32)
                #print("a4",a)
                a, b, c, d = d, a, b, c
                counter += 1

        #Update the vectors
        self.vectors = (
            (self.vectors[0] + a) % (2**32),
            (self.vectors[1] + b) % (2**32),
            (self.vectors[2] + c) % (2**32),
            (self.vectors[3] + d) % (2**32),
        )


def md5(s:str) -> str:
    state = MD5State(s)
    state.padding()
    state.md5_loop()
    return state.get_hex_int_from_bytes()


"""
Reference tests:
https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/064_md5_a_broken_secure_hash_algorithm_python_implementation/md5.py
"""

tests = [
    ("","d41d8cd98f00b204e9800998ecf8427e"),
    ("a","0cc175b9c0f1b6a831c399e269772661"),
    ("abc","900150983cd24fb0d6963f7d28e17f72"),
    ("message digest","f96b697d7cb7938d525a2f31aaf161d0"),
    ("abcdefghijklmnopqrstuvwxyz","c3fcd3d76192e4007dfb496cca67e13b"),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","d174ab98d277d9f5a5611c2c9f419d9f"),
    ("12345678901234567890123456789012345678901234567890123456789012345678901234567890","57edf4a22be3c955ac49da2e2107b67a"),
    ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
    ("The quick brown fox jumps over the lazy dog.","e4d909c290d0fb1ca068ffaddf22cbd0")
]

def test_md5(tests):
    test_results_str = ""
    for i,test in enumerate(tests):
        answer = md5(test[0])
        if(answer == test[1]):
            success_message = f"Passed test {i}"
            print(success_message)
            test_results_str += f"\n{success_message}\nMessage: {test[0]}\nHash: {answer}"
        else:
            fail_message = f"Failed test {i}\nMessage: {test[0]}\nExpected: {test[1]}\nGot: {answer}"
            print(fail_message)
            test_results_str += f"\n{fail_message}"
    
    with open("./test_results.txt","w") as f:
        f.write(test_results_str)

    print("Test results available at ./test_results.txt")

test_md5(tests)
