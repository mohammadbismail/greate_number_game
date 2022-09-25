from django.shortcuts import render, redirect
from random import randint


def renderindex(request):
    if "randnum" not in request.session:
        request.session["randnum"] = randint(1, 100)
    print(request.session["randnum"])
    return render(request, "index.html")


def process(request):
    request.session["input"] = request.POST["rec"]

    if int(request.session["input"]) < int(request.session["randnum"]):
        request.session["status"] = "low"

    elif int(request.session["input"]) > int(request.session["randnum"]):
        request.session["status"] = "high"

    elif int(request.session["input"]) == int(request.session["randnum"]):
        request.session["status"] = "equal"

    return redirect("/")


def deleted(request):
    del request.session["input"]
    del request.session["randnum"]

    return redirect("/")
