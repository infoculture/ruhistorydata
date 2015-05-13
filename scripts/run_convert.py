#!/usr/bin/env python


import sys, os, os.path

def run(dirname):
	files = os.listdir(dirname)
	for fname in files:
		sf, ext = fname.rsplit('.', 1)
		if ext != 'xlsx': continue
		print 'Processing %s' %(fname) 
		filename = os.path.join(dirname, fname)
		csvname = os.path.join(dirname, sf + '.csv')
		os.system('python xlsx2csv.py %s %s' %(filename, csvname))
		
		
if __name__ == "__main__":
	run(sys.argv[1])