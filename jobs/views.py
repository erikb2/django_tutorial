
import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job, candidate

# Create your views here.
def index(request):
    actual_jobs = Job.objects.all()
    context = {
        'actual_jobs': actual_jobs,
    }
    return render(request, 'jobs/index.html', context)

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    date = job.pub_date
    "{:%m/%d/%Y}".format(date)
    return render(request, 'jobs/detail.html', { 'job':job, 'date':date })