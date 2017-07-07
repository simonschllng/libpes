import sys
import struct

###########################################
# General util functions for binary files #
###########################################

def ByteToHex( byteStr ):
    return ''.join( [ "%02X" % ord( x ) for x in byteStr ] ).strip()



###########################################
# Mappings and helpers for PES specifics  #
###########################################

def hooptypes(value):
    return {
        '0000': '100mm x 100mm',
        '0100': '130mm x 180mm',
    }.get(value, 'unknown')


def RearPESHeader(file):
    return false

def ReadCEmbOneBlock(file):
    return false


def ReadCSewSegBlock(file):
    return false



###########################################
# Open file and load and print contents   #
###########################################


with open(sys.argv[1], "rb") as f:
    forma = f.read(8) # File Format
    pecst = f.read(4) # PEC start value
    pecstart = struct.unpack('<I', pecst)[0] # as int
    hoopv = f.read(2) # Hoop type
    nv1 = f.read(2) # Not verified value 1
    nstitchg = f.read(2) # Number of stitch groups
    print 'Format:                ' + forma
    print 'PEC start:             %d' % (pecstart)
    print 'Hoop value:            ' + ByteToHex(hoopv)
    print 'Hoop type:             ' + hooptypes(ByteToHex(hoopv))
    print 'Not verified value 1:  ' + ByteToHex(nv1)
    print 'Number of stitch grps: ' + ByteToHex(nstitchg)
    f.seek(pecstart, 0)
    print 'PEC HEAD:              ' + f.read(3)

