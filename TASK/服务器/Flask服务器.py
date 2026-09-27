from flask import Flask,request,jsonify
app=Flask(__name__)
@app.get("/")
def home():
    return{"message":"hello friend","status":"ok"}
if __name__=="__main__":
    app.run(debug=True,port=5002)