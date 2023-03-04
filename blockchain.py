class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, data):
        self.data = data
        self.hash = hash(data)

    def __repr__(self):
        return f'Block - data: {self.data}'


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'


blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
blockchain.add_block('three')

print(blockchain)
