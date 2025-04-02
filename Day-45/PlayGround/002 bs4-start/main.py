from bs4 import BeautifulSoup
import lxml
with open ('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents , 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())

all_actor_tag = soup.find_all(name='p')

for tag in all_actor_tag:
    print (tag.getText())

heading = soup.find(name='h1' , id='name')
print(heading)

company_url = soup.select_one(selector='p em strong a')
print(company_url)