from seg_temp import *

#Convert file to string, stripping off tailing space
def data_process(file):
	tmp = open(file, 'r')
	tmp = list(tmp)[0]
	tmp = tmp.strip()
	return s_t(tmp)
