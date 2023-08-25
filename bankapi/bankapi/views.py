from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("home page requested")
    friends = "This is the home page."

    return JsonResponse(friends, safe=False)