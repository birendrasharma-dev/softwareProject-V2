from flask import Flask, render_template

app = Flask("__name__")

DOC =[
  {
    'id':1,
    'name':'Birendra Sharma',
    'info':'Heart Surgeon'
  },
  {
    'id':2,
    'name':'Bishal Regmi',
    'info':' junior1 Heart Surgeon'
  },
  {
    'id':3,
    'name':'Anuj Thapa',
    'info':'junior2 Heart Surgeon'
  },
  {
    'id':4,
    'name':'Biswas Kafle',
    'info':'junior 3 Heart Surgeon'
  }
]


@app.route('/')
def hello_world():
  return render_template('home.html',
                        jobs=DOC)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
