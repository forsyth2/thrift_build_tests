import sys
DIRECTORY = subprocess.check_output('git rev-parse --show-toplevel'.split()).strip()
sys.path.insert(0, '%s/thrift/gen-py' % DIRECTORY)

import Tools.ttypes;
import ProcessorService.Processor;

class Server(ProcessorService.Processor.Iface):
    def __init__(self):
        pass

    def process(self, b):
        return Tools.ttypes.A()

if __name__ == '__main__':
    s = Server()
