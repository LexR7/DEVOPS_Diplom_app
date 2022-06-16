import socket

# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

#def index(request):
#    hostname = socket.gethostname()
#    local_ip = socket.gethostbyname(hostname)
#    hello = "Hello, world. You're at the myapp index.\n"
#    hello = hello + "Hostname is "+hostname+"\nIP address is "+local_ip
#    return HttpResponse(hello, content_type="text/plain")
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/detail.html', {'question': question})

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
