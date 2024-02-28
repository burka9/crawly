import datetime
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import BaseItem
from langid.langid import classify



def is_amharic(sentence):
    words = re.split(r'\W+', sentence)
    _is = 0

    for word in words:
        if classify(word)[0] == 'am':
            _is += 1

    return _is / len(words) > 0.5

items = [
	'span', 'b', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p', 'a',
	'button', 'label', 'li', 'td', 'th', 'strong', 'em', 'i', 'u', 's',
	'small', 'big', 'code', 'pre', 'blockquote', 'q', 'cite', 'summary',
	'details', 'figcaption', 'mark', 'ins', 'del', 'sub', 'sup', 'abbr',
	'address', 'article', 'aside', 'audio', 'bdi', 'bdo', 'canvas',
	'caption', 'col', 'colgroup', 'data', 'datalist', 'dd', 'dl', 'dt',
	'fieldset', 'figure', 'footer', 'form', 'header', 'hr', 'iframe',
	'img', 'input', 'kbd', 'legend', 'main', 'map', 'meter', 'nav',
	'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'progress',
	'ruby', 'rp', 'rt', 'rtc', 'section', 'select', 'source', 'table', 'tbody',
	'textarea', 'tfoot', 'thead', 'time', 'tr', 'track', 'ul', 'var', 'video'
]


def get_text(parent):
		text = ''
		for tag in parent.css(', '.join(items)):
				data = tag.css('::text').get()

				if data is not None and is_amharic(data):
						text += data + ' '

		return text.replace('\n', ' ')



class BaseSpider(CrawlSpider):
	name = 'base_spider'
	allowed_domains = ['']
	start_urls = ['']

	rules = (
		Rule(LinkExtractor(allow=()), callback='parse_item', follow=False),
	)

	def parse_item(self, response):
		loader = ItemLoader(item=BaseItem(), response=response)

		loader.add_value('url', response.url)
		loader.add_value('scrap_time', datetime.datetime.now())

		loader.add_value('text', get_text(response))

		yield loader.load_item()