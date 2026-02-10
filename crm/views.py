from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lead
from .forms import LeadForm
from django.shortcuts import get_object_or_404


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

    total_leads = Lead.objects.count()
    converted_leads = Lead.objects.filter(status='converted').count()

    return render(request, 'crm/dashboard.html', {
        'leads': leads,
        'total_leads': total_leads,
        'converted_leads': converted_leads,
    })


@login_required
def update_lead_status(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)

    if request.method == 'POST':
        lead.status = request.POST.get('status')
        lead.save()

    return redirect('dashboard')