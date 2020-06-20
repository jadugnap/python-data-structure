from huffman_coding import *

def test_pangram1():
    msg = "the quick brown fox jumps over a lazy dog"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

def test_pangram2():
    msg = "the five boxing wizards jump quickly"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

def test_pangram3():
    msg = "we promptly judged antique ivory buckles for the next prize"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)
