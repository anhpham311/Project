from mongoengine import Document, StringField

class Companies(Document):
    title = StringField()
    address = StringField()
    industries = StringField()

