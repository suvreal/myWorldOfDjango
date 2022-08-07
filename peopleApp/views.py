from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import PeopleApp
import math

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


def indexSecond(request):
  template = loader.get_template('mysecond.html')
  return HttpResponse(template.render())


def extraInfoIndex(request):
  template = loader.get_template('extraInfoIndex.html')
  return HttpResponse(template.render())


def allPeoples(request):
    people = PeopleApp.objects.all().values()
    template = loader.get_template('allPeoples.html')
    context = {
        'people': people,
    }
    return HttpResponse(template.render(context, request))
    # this for return without template
    '''people = PeopleApp.objects.all().values()
    output = ""
    for x in people:
        output += x["firstname"]
        output += x["lastname"]
        output += x["cityname"]
        output += x["streetname"]
        #output += x["housecode"]
        #output += x["citycode"]
        #output += x["isadult"]
        output += x["levelofeducation"]
        output += x["currentproffession"]
    return HttpResponse(output)'''


def addPeoples(request):
  template = loader.get_template('addpeoples.html')
  return HttpResponse(template.render({}, request))
  

def addPeopleRecord(request):
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  cityname = request.POST['cityname']
  streetname = request.POST['streetname']
  housecode = request.POST['housecode']
  citycode = request.POST['citycode']
  isadult = request.POST['isadult']
  levelofeducation = request.POST['levelofeducation']
  currentproffession = request.POST['currentproffession']

  people = PeopleApp(
    firstname=firstname, 
    lastname=lastname,
    cityname=cityname,
    streetname=streetname,
    housecode=housecode,
    citycode=citycode,
    isadult=isadult,
    levelofeducation=levelofeducation,
    currentproffession=currentproffession,
  )
  people.save()
  return HttpResponseRedirect(reverse('index'))


def deletePeopleRecord(request, id):
  people = PeopleApp.objects.get(id=id)
  people.delete()
  return HttpResponseRedirect(reverse('allPeoples'))


def updatePeoples(request, id):
  people = PeopleApp.objects.get(id=id)
  template = loader.get_template('updatepeoples.html')
  context = {
    'people': people,
  }
  return HttpResponse(template.render(context, request))


def updatePeopleRecord(request, id):
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  cityname = request.POST['cityname']
  streetname = request.POST['streetname']
  housecode = request.POST['housecode']
  citycode = request.POST['citycode']
  isadult = request.POST.get('isadult', 0)
  levelofeducation = request.POST['levelofeducation']
  currentproffession = request.POST['currentproffession']
  people = PeopleApp.objects.get(id=id)
  people.firstname = firstname
  people.lastname = lastname
  people.cityname = cityname
  people.streetname = streetname
  people.housecode = housecode
  people.citycode = citycode
  people.isadult = isadult
  people.levelofeducation = levelofeducation
  people.currentproffession = currentproffession
  people.save()
  return HttpResponseRedirect(reverse('index'))




