from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .trainAI import TrainAI

ai = TrainAI()
ai.train()

def chatbot(request):
    context = {'title': 'Chatbot'}
    user = request.user
    if not request.user.is_authenticated:
        print("redirect")
        return redirect('website-login')

    return render(request, 'chatbot_website/pages/chatbot.html', context)

def chatbot_response(request):
    context = {'title': 'Chatbot'}
    user = request.user
    if not request.user.is_authenticated:
        #print("redirect")
        return redirect('website-login')

    #print (request.method)
    if request.method == "POST":
        userMessage = request.POST.get('userMessage')
        #print(userMessage)
        botResponse = ai.chat(userMessage)
        botAudio = ai.voice(botResponse)
        #threading for faster
        # Wait for all threads to complete
        #{% static data.audio %}
        #botAudio = r"{% static " + r"'chatbot_website/audio/" + botAudio + r"' %}"
        
        context['data'] = str(botResponse)
        context['audio'] = str(botAudio)
        #print(context)
        return JsonResponse(context)
        
# Create your views here.