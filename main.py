from flask import Flask
import requests

app = Flask(__name__) 

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/image")
def retrieve_image():
    file_server_response = requests.get('http://localhost:8080/Veronica002.jpg')
    image_binary = file_server_response.content
    response = app.make_response(image_binary)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='Veronica002.jpg')
    return response