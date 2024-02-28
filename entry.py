from sys import argv
from urllib import parse

template = """from .base import BaseSpider


class {class_name}(BaseSpider):
	name = '{spider_name}'
	allowed_domains = ['{allowed_domain}']
	start_urls = ['{start_url}']

"""

script_name, spider_name, start_url = argv

start_url = 'https://' + start_url if not start_url.startswith('http') else start_url
url = parse.urlparse(start_url)

class_name = spider_name.capitalize() + 'Spider'

output = template.format(class_name=class_name, spider_name=spider_name, allowed_domain=url.netloc, start_url=start_url)

with open(f'crawly/spiders/{spider_name}.py', 'w') as file:
	file.write(output)