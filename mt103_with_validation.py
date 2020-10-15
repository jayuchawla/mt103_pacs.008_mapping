# https://en.wikipedia.org/wiki/MT103
# http://www.sepaforcorporates.com/swift-for-corporates/read-swift-message-structure/
# https://www.sepaforcorporates.com/swift-for-corporates/explained-swift-gpi-uetr-unique-end-to-end-transaction-reference/
    
from mt103 import MT103

class mt103_:
    def __init__(self, message):
        self.transaction = MT103(message)
        self.appId = ["A","F","L"]
        self.serviceId = ["01","03","21"]

    def validate_transaction(self):
        self.validateBasicHeader(self.transaction.basic_header)
        self.validateApplicationHeader(self.transaction.application_header)
        self.validateUserHeader(self.transaction.user_header)
        elf.validateBody(self.transaction.text)
        self.validateTrailer(self.transaction.trailer)

    def validateBasicHeader(self,basic_header):
        """identified by 1"""
        # validate application id
        if not basic_header[0] in self.appId:
            raise ValueError("ILLEGAL APPLICATION ID ENCOUNTERED")
        
        # validate service id
        elif not basic_header[1:3] in self.serviceId:
            raise ValueError("ILLEGAL SERVICE ID ENCOUNTERED")

        # validate bank code
        
    def validateApplicationHeader(self, application_header):
        pass

    def validateUserHeader(self, user_header):
        pass

    def validateBody(self, body):
        pass

    def validateTrailer(self, trailer):
        pass

