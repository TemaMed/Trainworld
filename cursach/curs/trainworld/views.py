# -*- coding: utf-8 -*-
import sys
import string
from django.shortcuts import render
import os
import json
from django.utils import timezone



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
    logininfo = {"login": "admin", "password": "admin"}
    if request.POST.get('login') == logininfo["login"] and request.POST.get('password') == logininfo["password"]:
        return render(request, "trainworld/admin_editor.html", {})

    ports = open_file("Ports")
    return render(request, "trainworld/main.html", {'ports': ports})


def admin(request):
    return render(request, "trainworld/admin.html")

def add_port(request):
    ports = open_file("ports")
    newport = {"city": request.POST.get("city"),
                       "name_port": request.POST.get("name_port"),
                       "city": request.POST.get("city"),
                       "status": request.POST.get("status"),
                       "trains": [
                           {
                               "train": "0",
                               "name": request.POST.get("name"),
                               "type": request.POST.get("type"),
                               "class": request.POST.get("class"),
                               "arrival": request.POST.get("arrival"),
                               "depurt": request.POST.get("depurt"),
                               "timerun": request.POST.get("timerun"),
                               "timeend": request.POST.get("timeend")
                           }
                       ]
                       }
    ports.append(newport)
    print(ports)
    write_in_file("Ports", str(ports).replace("\'", "\""))

    return render(request, "trainworld/main.html", {'ports': ports})