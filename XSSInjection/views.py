from django.shortcuts import render

# Create your views here.
def home(request):
    data = request.POST.get('name')
    print(data)

    return render(request, 'home.html', {'data': data})


def vulnerable(request):
    data = request.POST.get('name')
    print(data)

    return render(request, 'vulnerable.html', {'data': data})