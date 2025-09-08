from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from dbcreate.models import Responder_tbl, Ticket_tbl, IR_tbl
from .forms import TicketForm

# Create your views here.

def cs(request):
	# --- Handle Ticket Form ---
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cs')  # reload same page after saving
    else:
        form = TicketForm()
		
    context = {
		'workbench': Ticket_tbl.objects.filter(Classification__Classification = "Workbench").count(),
		'vulnerabilities': Ticket_tbl.objects.filter(Classification__Classification = "Threat").count(),
		'sonar': Ticket_tbl.objects.filter(Classification__Classification = "Project Sonar").count(),
		'advisories': Ticket_tbl.objects.filter(Classification__Classification = "Threat Advisories").count(),

		'total': Ticket_tbl.objects.count(),
		'unassigned': Ticket_tbl.objects.filter(Responder = None).count(), #revise in where clause
		'investigation': Ticket_tbl.objects.exclude(Responder__isnull=True).count(),
		'resolved': IR_tbl.objects.filter(Status__Status = "Resolved").count(), #revise in where clause

		'form': form,
		'tdata': Ticket_tbl.objects.all(),
	}

    return render(request, 'cs/cs.html', context)