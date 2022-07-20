from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "input.html")


def calculate(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    op = request.POST['op']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        if op == "add":
            res = a + b

        elif op == "sub":
            res = a - b 

        elif op == "mul":
            res = a * b  

        elif op == "div":
            res = a / b  

        else :
            res = "Invalid Operator"   

        return render(request, "input.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "input.html", {"result": res})


