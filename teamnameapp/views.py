from django.shortcuts import render

# Create your views here.

def team(request):
    return render(request, "team.html")

def result(request):
    userinput = int(request.GET['input'])
    if userinput == 3:
        output = "우리가 바로 3팀이3🥰"
    else:
        output = "언제 실물을 볼 수 있을까요..😢"
    return render(request, "result.html", {'output':output})