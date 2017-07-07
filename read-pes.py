import sys
import struct
from collections import namedtuple

###########################################
# General util functions for binary files #
###########################################

def ByteToHex( byteStr ):
    return ''.join( [ "%02X" % ord( x ) for x in byteStr ] ).strip()


###########################################
# Data classes                            #
###########################################

PesHeader = namedtuple('PesHeader', 'format pec_start_value pec_start_int hoop_value nv1 n_stitch_g')


###########################################
# Mappings and helpers for PES specifics  #
###########################################

def hooptypes(value):
    return {
        '0000': '100mm x 100mm',
        '0100': '130mm x 180mm',
    }.get(value, 'unknown')


def ReadPESHeader(file):
    forma = f.read(8) # File Format
    pecst = f.read(4) # PEC start value
    pecstart = struct.unpack('<I', pecst)[0] # as int
    hoopv = f.read(2) # Hoop type
    nv1 = f.read(2) # Not verified value 1
    nstitchg = f.read(2) # Number of stitch groups
    return PesHeader(forma, pecst, pecstart, hoopv, nv1, nstitchg)

def ReadCEmbOneBlock(file):
    return false


def ReadCSewSegBlock(file):
    return false



###########################################
# Open file and load and print contents   #
###########################################


with open(sys.argv[1], "rb") as f:
    p = ReadPESHeader(f)
    print( 'Format:                ' + p.format )
    print( 'PEC start:             %d' % (p.pec_start_int) )
    print( 'Hoop value:            ' + ByteToHex(p.hoop_value) )
    print( 'Hoop type:             ' + hooptypes(ByteToHex(p.hoop_value)) )
    print( 'Not verified value 1:  ' + ByteToHex(p.nv1) )
    print( 'Number of stitch grps: ' + ByteToHex(p.n_stitch_g) )
    f.seek(p.pec_start_int, 0)
    print( 'PEC HEAD:              ' + f.read(3) )

