import threading
from bs4 import BeautifulSoup
import requests
from db import search_word

def fetch_new_domain():
	words = search_word.find_all()
 
	if not words:
		print("No words found")
		return None
 
	for item in words:
		if item['is_searched'] is False:
			thread = threading.Thread(target=get_urls, args=(item['word'],))
			thread.start()
			# search_word.set_is_searched(item['word'], True)
			break


def gen_urls(word: str):
	page = 1
	urls = []
	url = gen_url(word, page)
  
	html = fetch_html(url)
	links = extract_search_links(html)

	print(links)


def gen_url(word: str, page: int):
	return f'https://www.abyssinica.com/search?q={word}&p={page}'


def fetch_html(url):
	try:
		response = requests.get(url)
		return response.text
	except Exception as ex:
		print(ex)
		return None

def extract_search_links(html):
	soup = BeautifulSoup(html, 'html.parser')
	links = soup.find_all('div.searchResultItem a')
	_links = []
 
	for link in links:
		_links.append(link.get('href'))
  
	return _links
