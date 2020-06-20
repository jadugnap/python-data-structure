import hashlib
import time, datetime

class Block:
    def __init__(self, id, data, prev_hash=0):
        self.id = id
        self.data = data
        self.timestamp = int(time.time())
        self.prev_hash = prev_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def __repr__(self):
        time_str = datetime.datetime.fromtimestamp(self.get_timestamp()).strftime('%Y/%m/%d-%H:%M:%S')
        return f"Block-id{self.get_id()}-{self.get_data()}-{time_str}-prev={self.get_short_prev_hash()}-cur={self.get_short_hash()}"

    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def get_timestamp(self):
        return self.timestamp

    def get_prev_hash(self):
        return self.prev_hash

    def get_short_prev_hash(self):
        if self.prev_hash:
            return self.prev_hash[:8]
        return 0

    def get_hash(self):
        return self.hash

    def get_short_hash(self):
        if self.hash:
            return self.hash[:8]
        return 0

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur_block = self.head
        linked_list = str(cur_block.get_data())
        cur_block = cur_block.next
        while cur_block:
            linked_list += " -> " + str(cur_block.get_data())
            cur_block = cur_block.next
        return linked_list

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def append_block(self, data):
        if self.head is None:
            self.head = Block(self.size, data)
            self.tail = self.head
            self.size += 1
            return self.tail
        node = self.tail
        prev_hash = node.get_hash()
        node.set_next(Block(self.size, data, prev_hash))
        self.tail = node.next
        self.size += 1
        return self.tail

if __name__=="__main__":
    my_blockchain = Blockchain()
    b0 = my_blockchain.append_block("trans0")
    b1 = my_blockchain.append_block("trans1")
    b2 = my_blockchain.append_block("trans2")
    print(my_blockchain)
    print(b0)
    print(b1)
    print(b2)
    new_b3 = my_blockchain.append_block("new_trans3")
    print(my_blockchain)
    print(new_b3)
