from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils.hashcompat import md5_constructor
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

def lists(request):
    if request.user is not None and request.user.is_authenticated():
        return render_to_response('lists.htm', {'usr': request.user},context_instance=RequestContext(request))
    else:
        return render_to_response('main.htm',{},context_instance=RequestContext(request))


def main(request,pass_ok=1):
    if request.user is None and not request.user.is_authenticated():
        return render_to_response('main.htm',{},context_instance=RequestContext(request))
    else:
        return render_to_response('lists.htm', {'usr': request.user},context_instance=RequestContext(request))

def reg(request,pass_ok=1,login_ok=1):
    return render_to_response('reg.htm',{'pass_ok':pass_ok,'login_ok':login_ok},context_instance=RequestContext(request))

def createacc(request):
    usrname=request.POST['usrname']
    p1=request.POST['p1']
    p2=request.POST['p2']
    clone=User.objects.filter(username=usrname)
    if clone:
        return reg(request,1,0)
    if p1!=p2:
        return reg(request,0)
    else:
        #add user and login
        phash=make_password(p1)
        NewUsr = User.objects.create_user(usrname, None, p1)
        NewUsr.save()
        user = authenticate(username=usrname, password=p1)
        if user is None:
            render_to_response('ca_succes.htm', {'accname': 'fail'})
        auth.login(request, user)
        return render_to_response('ca_succes.htm', {'accname': usrname})

def mylogin(request):
    usrname=request.POST['usrname']
    passwd=request.POST['passwd']
    phash=make_password(passwd)
    user = auth.authenticate(username=usrname, password=passwd)
    if user is not None and user.is_active:
        auth.login(request, user)
        return render_to_response('lists.htm', {'usr': request.user},context_instance=RequestContext(request))
    else:
        return render_to_response('main.htm',{'pass_ok':0},context_instance=RequestContext(request))
        
def mylogout(request):
    auth.logout(request)
    # return HttpResponseRedirect('/')
    return render_to_response('main.htm',{},context_instance=RequestContext(request))