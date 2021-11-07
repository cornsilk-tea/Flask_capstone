from flask import Flask, request
# from flask_ngrok import run_with_ngrok


app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/fileupload', methods=['POST'])
def upload_file():
    file = request.files['userfile']
    file.save('./'+ file.filename)
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)

