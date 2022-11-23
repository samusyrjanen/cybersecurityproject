from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the notepads index.")#.html template here. like this:  return render(request, 'polls/detail.html', {'question': question})

def notes(request):
    return HttpResponse('you are at the note page')
