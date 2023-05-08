import poe
from django.http import HttpResponse
from django.shortcuts import render
from EdgeGPT import Chatbot, ConversationStyle

class yordam:
    def ai(promp):
        return ''
        client = poe.Client('srgQYUu1dVNFhnJIgU7LxQ%3D%3D')
        s = ''
        for chunk in client.send_message('a2',promp):
            s+=chunk['text_new']
        return s
def index(request):
    prompt = request.GET.get('pmt')
    if prompt is None:
        prompt = ' '
    a = yordam.ai(prompt)
    return render(request, 'main/index.html', {'prom': a})