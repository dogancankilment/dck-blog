from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

def test_view(request):

    return HttpResponse("hello_world")