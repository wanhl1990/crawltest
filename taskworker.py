# coding:utf-8

import time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print 'Connect to server %s' % server_addr

m = QueueManager(address=(server_addr, 8001), authkey='123')

m.connect

task = m.get_task_queue()
result = m.get_result_queue()

while(not task.empty):
	image_url = task.get(timeout=5)
	print 'run download url %s' % image_url
	time.sleep(1)
	print '%s download over' % image_url