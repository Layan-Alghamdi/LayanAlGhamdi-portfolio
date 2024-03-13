from flask import Flask, render_template

app = Flask(__name__)
projects = [
{'id':1,
'project' : 'Web Scrapping',
'skills' : 'urllib python, python Requests,Selenium , BeatifulSoup'},
{'id':2,
'project' : 'AI model for flare mointoring',
'skills' : 'python pandas, microsoft azure, pychagpt , sikitlib, matplotlib'},
{} 
]

@app.route("/")
def hello_world():
  return render_template('home.html', myskills = projects,
                        myname='layan AlGhamdi')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080) #run flask server

