# Django imports
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template import Context, Template

# Internal project imports
from .helper import business_search, location_search, resume_parser
from .forms import UploadResumeForm

# python imports
import requests, json

def index(request):
    if request.method == 'POST':
        form = UploadResumeForm(request.POST, request.FILES)
        if form.is_valid():
            keywords = resume_parser(request.FILES.get('file', False))
            return HttpResponseRedirect('/search/') # TODO: use the keywords
    else:
        form = UploadResumeForm()
    return render(request, 'search/index.html', {'form': form})


def search(request):
    """ returns jobs based on keyword and location """
    # r = requests.get("http://api.angel.co/1/jobs")
    # response_data = r.json()
    # final_jobs = []
    # for job in response_data["jobs"]:
    #     job_tags = job['tags']
    #     job_match = True
    #     for tag in job_tags:
    #         if tag['tag_type'] is "SkillTag" and not business_search(tag['name']):
    #             job_match = False
    #         if tag['tag_type'] is "LocationTag" and not location_search(location, tag['name']):
    #             job_match = False
    #     # if category matches business and location matches search, check for desc and add it to list.
    #     if job_match and (keyword in job['description']):
    #         final_jobs.append(job)
    # context = {'jobs': final_jobs}
    # return render(request, 'search/search.html', context)
    return HttpResponse("Works for now")
