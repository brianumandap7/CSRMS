from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from dbcreate.models import Responder_tbl


# Create your views here.
def login(request):
	query = {
		
	}
	return render(request, 'login/login.html', query)


def lout(request):
	query = {
		
	}

	logout(request)
	return render(request, 'login/logout.html', query)

def profile(request):
	responder = Responder_tbl.objects.filter(Resp=request.user).first()
	responder1 = Responder_tbl.objects.filter(Resp=request.user)
	query = {
        "roles": responder.Roles.all() if responder else [],
        "responder": responder,
		"responder1": responder1,
		'udet': User.objects.filter(username = request.user),
	}
	return render(request, 'login/profile.html', query)
