import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds115094.mlab.com:15094/companies
host = "ds115094.mlab.com"
port = 15094
db_name = "companies"
user_name = "admin"
password = "toilaanh11"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())