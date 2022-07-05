import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input GitHub Username: ")
url = 'https://github.com/' + github_user
req = requests.get(url)
soup = bs(req.content, 'html.parser') #grabbing the HTML source code 
profile_image = soup.find('img', {'class' : 'avatar avatar-user width-full border color-bg-default'}) ['src'] #grabbing specific image
print(profile_image)

