# PES header

import struct


def ByteToHex( byteStr ):
	return ''.join( [ "%02X" % ord( x ) for x in byteStr ] ).strip()

class PesHeader:
	def __init__(self, file):
		self.read_pes_header_from_file(file)


	def read_pes_header_from_file(self, f):
		self.raw_format = f.read(8) # File Format
		self.raw_pec_start = f.read(4) # PEC start value
		self.pec_start = struct.unpack('<I', self.raw_pec_start)[0] # as int
		self.raw_hoop_type = f.read(2) # Hoop type
		self.raw_nv_1 = f.read(2) # Not verified value 1
		self.raw_n_stitch_g = f.read(2) # Number of stitch groups


	def get_description(self):
		output = "# PES Header:"
		output += '\nFormat:                ' + self.raw_format
		output += '\nPEC start:             %d' % (self.pec_start)
		output += '\nHoop value:            ' + ByteToHex(self.raw_hoop_type)
		output += '\nHoop type:             ' + self.get_hoop_description()
		output += '\nNot verified value 1:  ' + ByteToHex(self.raw_nv_1)
		output += '\nNumber of stitch grps: ' + ByteToHex(self.raw_n_stitch_g)
		return output

	def get_hoop_description(self):
		return {
			'0000': '100mm x 100mm',
			'0100': '130mm x 180mm',
		}.get(self.raw_hoop_type, 'unknown')
