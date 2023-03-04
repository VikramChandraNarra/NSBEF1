from flask import Flask, request
# import index as pm
import requests

app = Flask(__name__)

response = ""


def sendRequest(url, msg):
    global response
    headers = {'Content-Type': 'application/json'}
    data = {'message': msg}
    response2 = requests.get(url, headers=headers, json=data)
    # print(1)
    responseData = response2.json()
    temp = responseData["message"]
    if temp != "":
        response = temp
        print(response)
    else:
        print('No data received')

sendRequest("http://localhost:3000/chatbot/message", "What is your favourite dish?")

# @app.route('/chatbot/response', methods=['POST'])
# def index1():
#     global response
#     data = request.get_json()
#     if 'data' in data:
#         response = data["data"]
#         print(response)
#         return f'The data received is: {data["data"]}'
#     else:
#         return 'No data received'

@app.route('/r1/response', methods=['GET'])
def index2():
    global response

    if response != "":
        print("asad")
        temp = response
        response = ""
        return temp
    else:
        return ""

@app.route('/get/message', methods=['GET'])
def index3():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)