from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def entry(request):
    return render(request,'entry.html')
def entry(request):
    a = 100
    b = 200
    c = a * b
    print(c)  # For console output
    return render(request, 'entry.html', {"c": c})

def entry1(request):
    list1 = [100, 20, 300]
    print(list1)
    list1.append(50)
    print(list1)
    list1.append(60)
    print(list1)
    return render(request, "entry1.html", {"list": list1})
def entry2(request):
    if request.method=="GET":
        return render(request,"entry2.html")
    else:
        name=request.POST.get("name")
        print("name",name)
        age=request.POST.get("age")
        print("Age :",age)
        result=int(age)*int(age)
        print("result",result)
        
        return render(request,"entry2.html",{"result":result})
    
def entry3(request):
    result1 = None  # initialize to avoid NameError
    if request.method == "POST":
        a = request.POST.get("a")
        b = request.POST.get("b")
        try:
            result1 = int(a) * int(b)
        except (ValueError, TypeError):
            result1 = "Invalid input"
        print("Result1:", result1)
        return render(request, "entry3.html", {"result1": result1})
    else:
        return render(request, "entry3.html", {"result1": result1})

def home1(request):
    if request.method=="GET":
        return render(request,"home1.html")
    else:
        name=request.POST.get("name")
        print("name :",name)
        password=request.POST.get("password")
        print("password :",password)
    
        
        return render(request,"home.html")
    


