from huffman_coding import *

def test_pangram_sentence():
    msg = "the quick brown fox jumps over a lazy dog"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

    msg = "the five boxing wizards jump quickly"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

    msg = "we promptly judged antique ivory buckles for the next prize"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

def test_single_chartype():
    msg = "www"
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

def test_single_char():
    msg = 'x'
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)

def test_empty_string():
    msg = ''
    encoded_msg, tree = huffman_encoding(msg, True)
    decoded_msg = huffman_decoding(encoded_msg, tree)
    assert(decoded_msg==msg)
