# from flask import Flask, render_template, request, jsonify
# import textwrap
# from IPython.display import Markdown
# import os
# import google.generativeai as genai
# from IPython.display import Markdown
# from IPython.display import display
# from IPython.display import Markdown
# # Initialize Flask application
# app = Flask(__name__)

# # Set your Google API key
# os.environ['GOOGLE_API_KEY'] = "AIzaSyBXZwPIpASQp9fL0vkN0mGj4Dbh4pdTABM"

# # Configure generative model
# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
# model = genai.GenerativeModel('gemini-pro')

# # Function to format text as Markdown
# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# # Route to render the HTML form
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle form submission and generate content
# @app.route('/generate', methods=['POST'])
# def generate():
#     # Get query from form input
#     query = request.form['query']

#     # Generate content using the model
#     response = model.generate_content(query)
     
#     print(response)
#     formatted_response = response.text

#     # Convert Markdown to HTML
    
#     print(formatted_response)
#     # Render results template with generated content
#     return render_template('index.html', query=query, generated_content=str(formatted_response))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import textwrap
# from IPython.display import Markdown
# import os
# import google.generativeai as genai

 
# app = Flask(__name__)

 
# os.environ['GOOGLE_API_KEY'] = "AIzaSyBXZwPIpASQp9fL0vkN0mGj4Dbh4pdTABM"
 
# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
# model = genai.GenerativeModel('gemini-pro')

 
# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return textwrap.indent(text, '> ', predicate=lambda _: True)

 
# @app.route('/')
# def index():
#     return render_template('index.html')

 
# @app.route('/generate', methods=['POST'])
# def generate():
    
#     queries = request.form.getlist('query')

   
#     generated_content = []
#     for query in queries:
#         response = model.generate_content(query)
#         formatted_response = to_markdown(response.text)
#         print(formatted_response)
#         generated_content.append(str(formatted_response))

     
#     return render_template('index.html', queries=queries, generated_content=generated_content)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import textwrap
import os
import google.generativeai as genai

app = Flask(__name__)


os.environ['GOOGLE_API_KEY'] = "AIzaSyBXZwPIpASQp9fL0vkN0mGj4Dbh4pdTABM"


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


import textwrap
import re

def to_markdown(text):
    text = text.replace('•', '  *')   
    return textwrap.indent(re.sub(r'\*\*', '', text), ' ', predicate=lambda _: True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    queries = request.form.getlist('query')

    generated_content = []
    for query in queries:
        response = model.generate_content(query)
        formatted_response = to_markdown(response.text)
        generated_content.append(formatted_response)

    return render_template('index.html', queries=queries, generated_content=generated_content)

if __name__ == '__main__':
    app.run(debug=True)
 