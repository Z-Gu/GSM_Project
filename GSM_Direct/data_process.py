from seg_temp import *

#Convert file to string, stripping off tailing space
def data_process(file, enrol = False):
	tmp = open(file, 'r')
	tmp = list(tmp)[0]
	tmp = tmp.strip()
        if enrol:
        	return s_t(tmp, 2)
        return s_t(tmp)
