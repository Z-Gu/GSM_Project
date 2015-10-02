from subprocess import call

def get(lens = "Dummy"):

        #call the scanner, store as file

	file = lens + '_iso'
	tmp = open(file, 'w')
	call(["/root/scannerapi/scanner/scan_iso", "-s", lens], stdout = tmp)
	tmp.close()

        #Hexdump the binary to HEX string

	tmp_ = open(file + '_', 'w')
	call(["hexdump", "-e", '16/1 \"%02x\"', file], stdout = tmp_)
	tmp_.close()
	return file + '_'

	
	
