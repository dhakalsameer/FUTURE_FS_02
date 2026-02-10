from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lead
from .forms import LeadForm


def create_lead(request):
    """
    Public contact form
    """
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_success')
    else:
        form = LeadForm()

    return render(request, 'crm/create_lead.html', {'form': form})


def lead_success(request):
    return render(request, 'crm/lead_success.html')


@login_required
def dashboard(request):
    leads = Lead.objects.all().order_by('-created_at')
    return render(request, 'crm/dashboard.html', {'leads': leads})
