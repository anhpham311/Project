from flask import Flask,render_template, request ,redirect, url_for
from random import choice
from mlab import connect
from flask import Flask, flash
from company import Company, Search

app = Flask(__name__)
connect()

@app.route("/", methods = ["GET", "POST"])
def home():
  if request.method == "GET":
    return render_template("home.html")
  elif request.method == "POST":
    form = request.form
    keyword = form["search"]
    return redirect(url_for("result",keyword=keyword))

@app.route("/result/<keyword>", methods = ["GET","POST"])
def result(keyword):
    result = Company.objects(title__contains= keyword)
    return render_template("result.html", result = result)

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/payment")
def payment():
  return render_template("payment.html")  

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/signup") 
def signup():
  return render_template("signup.html") 

@app.route("/nhadautu")
def nhadautu():
  return render_template("nhadautu.html") 

@app.route("/startup") 
def startup():
  return render_template("startup.html") 

@app.route("/registercompany", methods=["GET","POST"]) 
def register():
  if request.method == "GET": 
    return render_template("registercompany.html") 
  if request.method == "POST":
    form = request.form
    title = form['title']
    add = form['address']
    industry = form['industries']
    # if title in Company.title():
    #   return "This company has been register"
    # else:
    p = Company(title=title, address=add, industries=industry)
    p.save()
    return "Thank you for register your company"

@app.route("/company_profile/")
def company():
  safety = Company.objects(industries = "safety")
  agriculture = Company.objects(industries = "agriculture")
  automotive = Company.objects(industries = "automotive")
  oilgas = Company.objects(industries = "oilgas")
  packaged = Company.objects(industries = "packaged")
  telecom = Company.objects(industries = "telecom")

  h = str(safety)
  print(h)
  print(type(h))
  return render_template("company_profile.html", agriculture = agriculture, safety = safety, automotive=automotive, oilgas=oilgas, packaged=packaged, telecom=telecom)   


if __name__ == '__main__':
  app.run(debug=True)

        