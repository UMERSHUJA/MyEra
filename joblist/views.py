from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobList


def joblist(request):
    if request.method == "POST":
        job_title = request.POST['job_title']
        description = request.POST['description']
        icon = request.POST['image']
        company_name = request.POST['company_name']
        experience = request.POST['experience']
        job_type = request.POST['job_type']
        destination = request.POST['destination']
        job_link = request.POST['job_link']
        user_id = request.POST['user_id']
        
        joblist = JobList(job_title=job_title, description=description, icon=icon, company_name=company_name, experience=experience, job_type=job_type, destination=destination, job_link=job_link, user_id=user_id)
        joblist.save()
        
        messages.success(request, 'Your requested has been submitted, wait for the admin response')
        
        return redirect('dashboard')


