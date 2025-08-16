# from flask import Flask, render_template, request, jsonify
# from langchain_groq import ChatGroq

# app = Flask(__name__)

# llm = ChatGroq(
#     temperature=0,
#     groq_api_key='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',
#     model_name="llama-3.1-70b-versatile"
# )

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get("message")
#     response = llm.invoke(user_input)
#     response_text = str(response)
#     return jsonify({"response": response_text})

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq

app = Flask(__name__)

llm = ChatGroq(
    temperature=0,
    groq_api_key='',
    model_name="llama-3.3-70b-versatile"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = llm.invoke(user_input)
    response_text = response.content  # Extract only the content of the message
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
