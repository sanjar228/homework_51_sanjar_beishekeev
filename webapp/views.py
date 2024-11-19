from django.shortcuts import render, redirect
from .cats import Cat
import random



def index(request):

    if request.method == 'GET':

        return render(request, 'index.html')


    elif request.method == 'POST':
        c = Cat()
        c  = c.set_name(request.POST.get('name1'))
        return redirect('stats/')
    

def stats(request):
    if request.method=='GET':
        c = Cat()
        
        return render(request, 'stats.html', {'name':c.name, 'age':c.age, 'eat':c.eat, 'happy':c.happy, 'picture':c.get_picture()[0], 'color':c.get_picture()[1]})
    elif request.method == 'POST':
        t = str(request.POST.get('action'))
        
        c = Cat()
        print(c.eat, t)
        if t == '3':
            c.set_sleep(True)
        elif t=='2':
            if c.is_sleeping:
                pass
            else:
                c.set_eat(15)
                c.set_happy(5)
        else:
            if c.is_sleeping:
                c.set_sleep(False)
                c.set_happy(-5)
            else:
                chance = random.randint(1,3)
                if chance==1:
                    c.set_happy(-c.happy)
                else:
                    c.set_happy(15)
                    c.set_eat(-10)
        print(c.eat)
        return redirect('/stats/')
                        