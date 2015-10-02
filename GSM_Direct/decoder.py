import zip

def sort(list):
	list_ = list[:]
	l = len(list)
	for i in list:
		if int(i[1], 16) != l:
			return None
		list_[int(i[0], 16)] = i
	return list_

def decode(list):
	content = ""
	num = 0
	id = ""
	enrol = False
	content += list[0][6:]
	id = list[0][2:4]
	comp = int(list[0][4:6], 16)
	if comp%2 == 0:
		enrol = True
		comp /= 2
	num = (comp + 1) / 2
	for i in list[1:]:
		content += i[4:]
		if i[2:4] != id:
			return None
	content = content.replace('?', "00")
	print content
	content = zip.Decode(content)
	tmp = int(content[-1])
	content = "464d5200" + content[:-1] + tmp * '0'
	return [content, id, num, enrol]
		
		
