from blockchain import *

def test_blockchain_list():
    my_blockchain = Blockchain()
    b0 = my_blockchain.append_block("trans0")
    b1 = my_blockchain.append_block("trans1")
    b2 = my_blockchain.append_block("trans2")
    
    assert(my_blockchain.get_head()==b0)
    assert(b0.get_prev_hash()==0)
    
    assert(b0.get_next()==b1)
    assert(b0.get_hash()==b1.get_prev_hash())
    
    assert(b1.get_next()==b2)
    assert(b1.get_hash()==b2.get_prev_hash())
    assert(my_blockchain.get_tail()==b2)
    
    new_b3 = my_blockchain.append_block("new_trans3")
    assert(b2.get_next()==new_b3)
    assert(b2.get_hash()==new_b3.get_prev_hash())
    assert(my_blockchain.get_tail()==new_b3)

def test_blockchain_single_block():
    my_blockchain = Blockchain()
    b0 = my_blockchain.append_block("trans0")
    assert(my_blockchain.get_head()==b0)
    assert(b0.get_id()==0)
    assert(b0.get_data()=="trans0")
    assert(b0.get_prev_hash()==0)
    assert(b0.get_hash()!=0)
    assert(b0.get_next()==None)
    assert(my_blockchain.get_tail()==b0)

def test_blockchain_no_block():
    my_blockchain = Blockchain()
    assert(my_blockchain.get_head()==None)
    assert(my_blockchain.get_tail()==None)
