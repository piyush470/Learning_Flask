from flask import  Flask,render_template
app=Flask(__name__)

@app.route("/") #--> home page searching keyword
def home():
    name="Piyush" #data
    age=82 #data
    return render_template('home.html',nm=name,age=age) #take it to html file

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/student/")
def studentdata():
    data=['Mayour','Pankaj','Rishab','Vikash','Piyush']
    s1={'name':'Piyush','age':'21','address':"Bhopal",'Marks':90.12}
    s2={'name':'Pankaj','age':'23','address':"Karond",'Marks':0.12}
    s3={'name':'Rishab','age':'24','address':"Sadak",'Marks':5.12}
    s4={'name':'Vikash','age':'25','address':"Karond",'Marks':15.12}
    s5={'name':'Paras','age':'26','address':"Lalghati",'Marks':12.12}
    data1=[s1,s2,s3,s4,s5]
    return render_template('studentdata.html',dt=data,s1=s1,list=data1)

#run app
if __name__=="__main__":
    app.run(debug=True)