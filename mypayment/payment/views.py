from django.http import HttpResponse
def set_cookie(request):
    response=HttpResponse("Cookie has been set")
    response.set_cookie('username','Gaudam')
    response.set_cookie('language','en')
    return response
def get_cookie(request):
    username=request.COOKIES.get('username')
    language=request.COOKIES.get('language')
    return HttpResponse(f"Username:{username},Language:{language}")
