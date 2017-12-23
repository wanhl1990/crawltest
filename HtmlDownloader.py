# coding:utf-8

import requests
class HtmlDownloader(object):
	# def __init__(self, target):
	# 	self.url = target

	def download(self, url):
		if url is None or len(url) == 0:
			return None

		user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0"

		headers = {'User-Agent': user_agent}
		req = requests.get(url, headers=headers)

		if req.status_code == 200:
			req.encodinz = 'utf-8'
			return req.text
		return None