from urllib.request import urlopen
from bs4 import BeautifulSoup
from mongoengine import Document, StringField
from mlab import connect
from company import Company

connect()

url = "https://trangvangvietnam.com/categories/484480/hoa-chat-thuc-pham.html"
conn = urlopen(url)

raw_data = conn.read()

html_page = raw_data.decode("utf-8")

soup = BeautifulSoup(html_page, "html.parser")
di = soup.find("div", id = "listingsearch")

di_list = di.find_all("div", "boxlistings")

companies = []
for i in di_list:
    h2 = i.div.h2
    title = h2.string
    top = i.find("div","listings_top")
    div = top.find("div","noidungchinh")
    logo = div.find("div", "logo_address")
    section = logo.find("div", "address_listings")
    info = section.find_all("p", "diachisection")
    address = info[1]
    add = address.text

    company = {
        "title": title,
        "address": add,
        "industry": "telecom"
    }
    companies.append(company)

for company in companies:
    
    # # Create document 
    c = Company(title=company['title'], address=company['address'], industries="telecom")
    c.save()
