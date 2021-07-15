from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['name']
    worldlist=fulltext.split()

    worddictionary = {}
    for word in worldlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1




    return render(request,'index.html',{'fulltext':fulltext,'worldlist':len(worldlist),'worddictionary':worddictionary})
