from django.http import JsonResponse
def home(request):
    data={
        'name':'Rahul',
        'city':True,
        'age':24,
        'phd':None
    }
    return JsonResponse(data)
