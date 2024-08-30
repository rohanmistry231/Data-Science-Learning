def blockchain_hash(data):
    # generating a basic hash
    return data + '*'

class Block:
    # block represents a storage unit
    def __init__(self, data, hash, previous_hash):
        self.data = data  # data shows what the storage unit is storing
        self.hash = hash    # unique value generated for block based on data. it helps in varifying the block data
        self.previous_hash = previous_hash  # link between blocks and blockchain. used to create a link between new block and last block


class Blockchain:
    # a chain system keeping blocks
    def __init__(self):
        genesis = Block('genesis_data', 'genesis_hash', 'genesis_previous_hash')
        # every block  consist of prior block. first block has a genesis block
        self.chain = [genesis]  # to store block objects

    def add_block(self, data):
        last_hash = self.chain[-1].hash  # finding the previous block hash
        hash = blockchain_hash(data + last_hash)  # creating a hash for block
        block = Block(data, hash, last_hash)  # create a instance

        self.chain.append(block)

my_blockchain = Blockchain()
my_blockchain.add_block('one')
my_blockchain.add_block('two')
my_blockchain.add_block("three")
my_blockchain.add_block("four")
my_blockchain.add_block("five")


for block in my_blockchain.chain:
    print(block.__dict__)  #  __dict__ creates a key value collection