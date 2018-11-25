from urllib.request import urlopen
from bs4 import BeautifulSoup
from mongoengine import Document, StringField
from mlab import connect
from company import Company
# 1. Connect to database:
connect()

# 2. Prepare data
url = "https://trangvangvietnam.com/categories/210260/an-ninh-an-toan-he-thong-va-thiet-bi-an-toan.html"
conn = urlopen(url)

# 1. Read the data:
raw_data = conn.read()

# 2. Decode the data
html_page = raw_data.decode('utf-8')

# 3. Open connection to file
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
        "industry": "safety"
    }
    companies.append(company)

for company in companies:
    
    # # Create document 
    
    c = Company(title=company['title'], address=company['address'], industries="safety")

    # # Save
    c.save()

    
