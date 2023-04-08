from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import *
from pywebio.pin import *
import openai

def app():
    put_html("<center><h2>sahandasoaii</h2></center>").style("color:tomato; padding:1px;  ")
    put_html("<center><img src='' width='400'></center>")
    openai.api_key = "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"
    ask = input('chatgpt: wat do make')
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = ask,
        temperature=0.9,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text = response['choices'][0]['text']
    code = textarea('Code Edit:[ yuor serch]',
    code={
    'mode' : "python",
    'theme': 'dracula',
    },value=text)



start_server(app,port=1266,debug=True)