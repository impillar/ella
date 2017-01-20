import os
import re
import sys
import shutil

def main(folder):
	coverage = []
	size = 0
	for f in os.listdir(folder):
 		# in the current implementation, there should only one "coverage.data" file
		if f.startswith('coverage.dat.'): 
			coverage.append(os.path.join(folder, f))
		elif f == 'covids':
			size = len(open(os.path.join(folder, f)).readlines())

	#sorted(coverage, reverse=True)
	#print coverage
	#print 'size: ', size
	#print 'coverage: ', coverage

	# the array of covered methods
	covered = [0] * (size + 1)

	if len(coverage) < 1:
		print '0'
		exit(0)

	for cov_file in coverage:
		#print cov_file
		for num in open(cov_file).readlines():
			if re.match(r'\d+', num.strip()):
				n = int(num)
				covered[n] = 1
	sum = 0
	for a in covered:
		sum += a

	if size > 0:
		print sum * 1.0 / size
	else:
		print '0'


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Usage: python %s [FOLDER]' % __file__
		exit(0)
	main(sys.argv[1])
