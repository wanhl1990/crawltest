# coding:utf-8

from UrlManager import UrlManger
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader
from DataOutput import DataOutput
import pdb

class SpiderMan(object):

    def __init__(self):
        self.manger = UrlManger()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        print 'crawl %s ' % root_url
        self.manger.add_new_url(root_url)

        #pdb.set_trace()
        while (self.manger.has_new_url() and self.manger.old_urls_size() < 100):
            try:
                new_url = self.manger.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manger.add_new_urls(new_urls)
                self.output.store_data(data)
                print 'Has crawl %s links ' % self.manger.old_urls_size()
            except Exception, e:
                print "crawl failed %s" % e
                break

        self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    root_url = "http://baike.baidu.com/view/284853.htm"
    spider_man.crawl(root_url)
