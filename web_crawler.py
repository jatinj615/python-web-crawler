import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	page=1
	while page <= max_pages:
		url = "https://internshala.com/internships/virtual-web%20development-internship-in-delhi/duration-2/part_time-true/page-" + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll( 'a' , {'class': 'view_detail_button'}):
			href = 'https://internshala.com' + link.get('href')
			print(href + "\n")
			get_single_internship_data(href)
		page += 1	

def get_single_internship_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for skills in soup.findAll('span' , {'id': 'skillNames'}):
		print("Skills Required : " + skills.string + "\n")
		
spider(1)