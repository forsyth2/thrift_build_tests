import sys
sys.path.insert(0, '../thrift/gen-py')

import Tools.ttypes;
import ProcessorService.Processor;

class Server(ProcessorService.Processor.Iface):
    def __init__(self):
        pass

    def process(self, b):
        return Tools.ttypes.A()

if __name__ == '__main__':
    s = Server()
