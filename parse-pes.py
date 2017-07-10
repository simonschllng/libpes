import yaml
import sys
import pprint
import struct

import bin_parser.bin_parser
from bin_parser.bin_parser import BinReadFunctions

class Functions(BinReadFunctions):
    def float(self, data):
        return struct.unpack('f', data)[0]
    def inv(self, data):
        return data ^ 0xff

#usage: python2 ./parse-pes.py PES-FILE

parser = bin_parser.BinReader(
    open(sys.argv[1]).read(),
    yaml.safe_load(open('pes-definitions/structure.yml')),
    yaml.safe_load(open('pes-definitions/types.yaml')),
    functions=Functions())


pp = pprint.PrettyPrinter(indent=4)
pp.pprint( parser.parsed )

