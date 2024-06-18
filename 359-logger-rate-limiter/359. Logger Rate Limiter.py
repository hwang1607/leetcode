class Logger:

    def __init__(self):
        self.seen = {} #msg : timestamp
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.seen:
            if timestamp - self.seen[message] >= 10:
                self.seen[message] = timestamp
                return True
            return False
        
        self.seen[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)