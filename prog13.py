from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "hello,my backend API is Running!"
@app.route('/test')
def test():
    return {"message":"API working","status":"success"}
if __name__=='__main__':
    app.run(debug=True)