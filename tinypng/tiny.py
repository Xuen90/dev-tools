# -*- coding: utf-8 -*-
import os
import sys
import time
import tinify
import random

# your api key
api_keys = [
	'your api key'
]

def compress(full_path):
	file_path = full_path[:full_path.rfind('\\') + 1]
	file_name = full_path[full_path.rfind('\\') + 1:]
	new_floder = 'compressed\\'

	# create new floder
	if not os.path.exists(('%s%s' % (file_path, new_floder))):
		os.mkdir(('%s%s' % (file_path, new_floder)))

	# print log
	print file_name, ' >>> ', ('%s%s' % (new_floder, file_name))
	new_file = ('%s%s%s' % (file_path, new_floder, file_name))
	# print file_path
	# print file_name
	# print 'new file', new_file

	source = tinify.from_file(full_path)
	source.to_file(new_file)
    
if __name__ == "__main__":
	# check api key
	if len(api_keys) > 0:
		# set an api key
		tinify.key = api_keys[random.randint(0, len(api_keys) - 1)]

		if len(sys.argv) > 1:
			print 'compress start...\n'
			for arg in sys.argv:
				if arg.endswith('png') or arg.endswith('jpg'):
					compress(arg)
			print '\ncompress completed!'
			raw_input('press any key to continue...')
	else:
		raw_input('please set api key!')