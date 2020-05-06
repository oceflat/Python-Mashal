#!/usr/bin/python
# -*- Coding: utf-8 -*-

import os
import sys
import time
import marshal

def python2():
	try:
		os.system('clear')
		n = raw_input('Enter you file to be Encoded : ')
		a = open(n).read()
		d = compile(a, '', 'exec')
		i = marshal.dumps(d)
		aa = open('marshal_' + n, 'w')
		aa.write('import marshal\n')
		aa.write('exec(marshal.loads(' + repr(i) + '))')
		aa.close()
		time.sleep(2)
		print('File' + n + ' Success encoded !\r\nOutput file : marshal_' + n)
	except KeyboardInterrupt:
		print('File' + n + ' Failed to encode')
		exit()

if __name__ == '__main__':
	python2()
