from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

cglURL = "https://mumbai.craigslist.org/search/?query={0}"

def home(request):
	return render(request,'base.html')

def new_search(request):
	search = request.POST.get('search')
	resp = requests.get(cglURL.format(search))
	soup = BeautifulSoup(resp.text, features='html.parser')

	post_listings = soup.find_all('li', {'class': 'result-row'})

	final_postings = list()

	print(post_listings[0])

	for post in post_listings:
		post_title = post.find(class_='result-title').text
		post_url = post.find('a').get('href')

		if post.find(class_='result-price'):
			post_price = post.find(class_='result-price').text
		else:
			post_price = 'N/A'

		post_image_url = 'https://craigslist.org/images/peace.jpg'

		final_postings.append((post_title, post_url, post_price, post_image_url))

	context = {
		'search': search,
		'final_postings': final_postings,
	}
	return render(request,'myapp/new_search.html',context)

# Create your views here.
