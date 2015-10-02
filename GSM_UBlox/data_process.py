from seg_temp import s_t
form = ["-image", "-template"]

def data_process(file, form, method):
	tmp = open(file, 'r')
	if form == "-template" :
		tmp = list(tmp)[0]
		tmp = tmp.strip()
		if method == "-gsm":
			return ' '.join(s_t(tmp)) + '\n'
	if form == "-image":
		pass
