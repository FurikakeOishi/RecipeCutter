import requests
from bs4 import BeautifulSoup
import xmltodict
#urls =['https://www.justonecookbook.com/post-sitemap2.xml','https://sallysbakingaddiction.com/recipe-index/',"https://www.epicurious.com/search/?content=recipe","https://www.delishknowledge.com/recipe-index/","https://www.recipetineats.com/recipes/"]

#for url in urls:
url = 'https://www.justonecookbook.com/post-sitemap2.xml'
siteMap=xmltodict.parse(requests.get(url).text)
urls=[url["loc"]for url in siteMap["urlset"]["url"]]
print(urls)
#print("\n".join(urls))
for url1 in urls:
    print(url1)
    f=open("test1.txt","w")
    f.write(url1)
    f.write("\n")
f.close()


