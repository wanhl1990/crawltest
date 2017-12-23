import threading
import os
import time, random	

def run_thread(urls):
	print 'Current %s is running\n' % threading.current_thread().name

	for url in urls:
		print '%s -------- > %s\n' % (threading.current_thread().name, url)
		time.sleep(random.random())

	print '%s ending' % threading.current_thread().name


#if __name__ == '__main__':
t1 = threading.Thread(target=run_thread, name='Thread1', args= (['url1', 'url2'],))
t2 = threading.Thread(target=run_thread, name='Thread2', args= (['url3', 'url4'],))

t1.start()
t2.start()

t1.join()
t2.join()

print 'threading over'