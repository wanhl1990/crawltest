# codeing:utf-8

class UrlManger(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_new_url(self, url):
		if url is None:
			return False

		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self, urls):
		if url is None or len(url) == 0:
			return False

		for url in urls:
			sself.add_new_url(urls)

	def new_urls_size(self):
		return len(self.new_urls)

	def old_urls_size(self):
		return len(self.old_urls)

	def has_new_url(self):
		return self.new_urls_size() != 0