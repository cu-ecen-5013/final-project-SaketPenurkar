try:
	file_handler = open('/home/saket/Downloads/temp.txt', 'r+')
	file_handler.truncate(0)
except Exception as e:
	print(e)
