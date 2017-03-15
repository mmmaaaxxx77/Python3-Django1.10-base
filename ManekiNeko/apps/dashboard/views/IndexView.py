from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ManekiNeko.core.singleton.singleton import Singleton


@login_required
def index(request):
    if request.method == 'GET':

        test = Test
        i = test.count(test)

        return render(request, 'dashboard/index.html', {'count': i})

@login_required
def index2(request):
    if request.method == 'GET':

        test = Test
        i = test.count(test)

        return render(request, 'dashboard/index.html', {'count': i})


class Test(metaclass=Singleton):
    count2 = 0

    def __init__(self):
        self.count = 0

    def count(self):
        self.count2 += 1
        return self.count2
