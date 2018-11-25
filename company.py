from mongoengine import Document, StringField, ListField

class Company(Document):
    title = StringField()
    address = StringField()
    industries = StringField()

class Search(Document):
    keyword = StringField()