from django.shortcuts import render_to_response
# from django.http import HttpResponse
# from django.template import loader,Context
# Create your views here.
# class Person(object):
#     def _init_(self,name,age,sex):
#         self.name = name;
#         self.age = age;
#         self.sex = sex;
#     def say(self):
#         return "I'm "+self.name
# def index(rep,parm):
#     user = {'username':'tom','age':23,'sex':'male'}
#     book_list =['python','java','php','web']
#     return render_to_response('index.html',{'title':'my page','book_list':book_list,'user':user,'id':parm}) 
# #     return HttpResponse('<h1>Hello Welcome to Django!</h1>')

# def index(rep):
#     t = loader.get_template('index.html')
#     c = Context({})
#     
#     return HttpResponse(t.render(c))
class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say(self):
        return "I'm "+self.name
def index(req):
    user = {'name':'tom','age':23,'sex':'male'}
#     user = Person('tom',24,'male')
    book_list=['python','java','php','web']
    return render_to_response('index.html',{'title':'my page','user':user,'book_list':book_list})
