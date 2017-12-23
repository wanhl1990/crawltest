import os

if __name__ == '__main___':
	print 'current process {%s} start ' % (os.getpid())

	pid = os.fork()

	if pid < 0:
		print 'error in fork'
	elif pid == 0:
		print 'fork success , it is the children process , pid is {%s}, parent pid is {%s}' % (os.getpid(), os.getppid())
	else:
		print 'I {%s} create child process {%s}' % (os.getpid(), pid)
