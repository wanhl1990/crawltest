import os, time, random
from multiprocessing import Pool 

def run_task(name):
	print '{%s} running process {%s}' % name, os.getpid()
	time.sleep(random.random * 3)
	print 'process {%s} over '% name

if __name__ == '__main__':
	print 'current process %s' % os.getpid()

	p = Pool(processes=3)
	for i in range(5):
		p.apply_async(run_task, args=(i, ))
	print 'waiting for all subprocess done'
	p.close()
	p.join()

	print 'All process done'