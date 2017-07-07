#! /usr/bin/python2.7

import sys
import struct
from collections import namedtuple


# The PES lib
from LibPes.pesheader import PesHeader


###########################################
# Mappings and helpers for PES specifics  #
###########################################


def ReadCEmbOneBlock(file):
	return false


def ReadCSewSegBlock(file):
	return false




###########################################
# Open file and load and print contents   #
###########################################



with open(sys.argv[1], "rb") as f:
	header = PesHeader(f)
	print( header.get_description() )
	f.seek(header.pec_start, 0)
	print( 'PEC HEAD:              ' + f.read(3) )

