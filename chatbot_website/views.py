from django.shortcuts import render

#codev20db
#ranegillian
#codev20chatbot

# Create your views here.
def home(request):
    return render(request, 'chatbot_website/index.html', {'title': 'Home'})

def about(request):
    return render(request, 'chatbot_website/pages/about.html', {'title': 'About'})

def faqs(request):
    return render(request, 'chatbot_website/pages/FAQs.html', {'title': 'FAQs'})

def handler404(request, exception):
    return render(request, 'chatbot_website/errors/404.html')

def handler500(request):
    return render(request, 'chatbot_website/errors/500.html')