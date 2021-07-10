from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    #return 'Revemi'
    return render_template('index.html')

@app.route('/about')
def about():
    #return 'Revemi'
    return render_template('about.html')

@app.route('/products')
def product():
    #return 'Revemi'
    return render_template('products.html')

@app.route('/value-chain')
def value():
    #return 'Revemi'
    return render_template('value-chain.html')

@app.route('/sustainability')
def sustain():
    #return 'Revemi'
    return render_template('sustainability.html')


if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host='0.0.0.0', port=8080)