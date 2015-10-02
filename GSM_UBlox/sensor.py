from subprocess import call
method_program = {
			"-template": "scan_iso",
			"-image": "scan_png"
		  }

def get(form, lens = "Dummy"):
	if form not in method_program:
		print "The format is not known!\n"
		return False
	file = lens + '_' + form[1:]
	tmp = open(file, 'w')
	call(["/root/scannerapi/scanner/"+method_program[form], "-s", lens], stdout = tmp)
	tmp.close()
	if form == "-template":
		tmp_ = open(file + '_', 'w')
		call(["hexdump", "-e", '16/1 \"%02x\"', file], stdout = tmp_)
		tmp_.close()
		return file + '_'
	return file

	
	
