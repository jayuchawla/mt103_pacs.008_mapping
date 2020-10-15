# https://en.wikipedia.org/wiki/MT103
# http://www.sepaforcorporates.com/swift-for-corporates/read-swift-message-structure/
# https://www.sepaforcorporates.com/swift-for-corporates/explained-swift-gpi-uetr-unique-end-to-end-transaction-reference/
    
from mt103 import MT103

class mt103_:
    def __init__(self, message):
        transaction = MT103(message)

    def validate_transaction(self):