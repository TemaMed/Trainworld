# -*- coding: utf-8 -*-
import sys
import string
from django.shortcuts import render
import os
import json
from django.utils import timezone
from .models import Post


def open_file(name):
    file = r"\trainworld\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def write_in_file(name, text):
    file = r"\trainworld\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "w", encoding='utf-8') as fh:
        fh.write(text)
    pass


def head(request):
    ports = open_file("ports")
    return render(request, "trainworld/head.html", {'ports': ports})


def search1(request):
    ports = open_file("ports")
    return render(request, "trainworld/main.html", {'ports': ports})


def info_list(request):
    ports = open_file("ports")
    return render(request, "trainworld/main.html", {'ports': ports})


def get_port(request):
    ports = open_file("ports")
    for i in ports:
        if i["city"] == request.POST.get("name"):
            return render(request, "trainworld/info_port.html", {'port': i})

    return render(request, "trainworld/main.html", {'ports': ports})


def auth(request):
    ports = open_file("ports")
    logininfo = {"login": "admin", "password": "admin"}
    if request.POST.get('login') == logininfo["login"] and request.POST.get('password') == logininfo["password"]:
        return render(request, "trainworld/admin_editor.html", {'ports': ports})

    ports = open_file("Ports")
    return render(request, "trainworld/main.html", {'ports': ports})


def admin(request):
    logininfo = open_file("admin")
    for i in logininfo:
        if request.POST.get('login') == i["login"] and request.POST.get('password') == i["password"]:
            return render(request, "trainworld/add_train.html", {"port": request.POST.get("city")})

    ports = open_file("Ports")
    return render(request, "trainworld/main.html", {'ports': ports})


def add_port(request):
    ports = open_file("ports")
    newport = {"id": str(len([""])),
               "name_port": request.POST.get("name_port"),
               "city": request.POST.get("city"),
               "status": request.POST.get("status"),
               "trains": [
               ]
               }
    ports.append(newport)
    write_in_file("Ports", str(ports).replace("\'", "\""))

    return render(request, "trainworld/main.html", {'ports': ports})


def add_train(request):
    ports = open_file("ports")
    for i in ports:
        if i["city"] == request.POST.get("city"):
            t = {"train": request.POST.get("train"),
                 "name": request.POST.get("name"),
                 "type": request.POST.get("type"),
                 "class": request.POST.get("class"),
                 "arrival": request.POST.get("arrival"),
                 "depurt": request.POST.get("depurt"),
                 "timerun": request.POST.get("timerun"),
                 "timeend": request.POST.get("timeend")
                 }
            i["trains"].append(t)
            write_in_file("ports", str(ports).replace("\'", "\""))

    return render(request, "trainworld/main.html", {'ports': ports})


def add_manager(request):
    managers = open_file("admin")
    ports = open_file("ports")
    newmanager = {"login": request.POST.get("login"),
                  "password": request.POST.get("password")}
    managers.append(newmanager)
    write_in_file("admin", str(managers).replace("\'", "\""))

    return render(request, "trainworld/main.html", {'ports': ports})


def search(request):
    ports = open_file("ports")
    for i in ports:
        if i["city"] == request.POST.get("search"):
            return render(request, "trainworld/info_port.html", {'port': i})

    return render(request, "trainworld/main.html", {'ports': ports})


def delete(request):
    ports = open_file("ports")
    for i in ports:
        if i["city"] == request.POST.get("se"):
            ports.remove(i)
            write_in_file("ports", str(ports).replace("\'", "\""))
            return render(request, "trainworld/main.html", {'ports': ports})

    return render(request, "trainworld/main.html", {'ports': ports})


def delete_train(request):
    ports = open_file("ports")
    for i in ports:
        if i["city"] == request.POST.get("se"):
            ports.remove(i)
            write_in_file("ports", str(ports).replace("\'", "\""))
            return render(request, "trainworld/main.html", {'ports': ports})

    return render(request, "trainworld/main.html", {'ports': ports})