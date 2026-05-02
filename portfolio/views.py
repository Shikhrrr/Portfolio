"""
Portfolio views — index, hire form, resume download.
"""

import os
from itertools import groupby

from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import (
    SiteConfig, Experience, Project, Skill, Achievement, HireRequest
)


def index(request):
    """
    Main portfolio page — single scrollable page.
    Pulls all content from the database and passes to Jinja2 template.
    """
    config = SiteConfig.get_solo()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()

    # Group skills by category preserving the defined order
    CATEGORY_ORDER = ['Languages', 'Frameworks & Tools', 'AI/ML', 'Databases', 'Concepts']
    all_skills = list(Skill.objects.all())

    skills_by_category = {}
    for cat in CATEGORY_ORDER:
        cat_skills = [s for s in all_skills if s.category == cat]
        if cat_skills:
            skills_by_category[cat] = cat_skills

    # Education (hardcoded — not model-driven per spec)
    education = [
        {
            'institution': 'IIIT Sonepat',
            'degree': 'B.Tech Computer Science & Engineering',
            'details': 'GPA: 8.2 / 10',
            'year': 'Expected 2027',
        },
        {
            'institution': 'Delhi Public School, Kalyanpur',
            'degree': 'Class XII (PCM + CS)',
            'details': '92.6%',
            'year': '2023',
        },
        {
            'institution': 'Delhi Public School, Kalyanpur',
            'degree': 'Class X',
            'details': '95.6%',
            'year': '2021',
        },
    ]

    # Check for success message from hire form
    hire_success = request.GET.get('hire_success') == '1'

    from django.middleware.csrf import get_token
    context = {
        'config': config,
        'experiences': experiences,
        'projects': projects,
        'skills_by_category': skills_by_category,
        'achievements': achievements,
        'education': education,
        'hire_success': hire_success,
        'csrf_token': get_token(request),
    }

    return render(request, 'portfolio/index.html', context)


@require_POST
def hire(request):
    """
    Handle contact form POST submission.
    Saves to DB and redirects back with success param.
    """
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    company = request.POST.get('company', '').strip()
    message = request.POST.get('message', '').strip()

    if name and email and message:
        HireRequest.objects.create(
            name=name,
            email=email,
            company=company,
            message=message,
        )

    return redirect('/?hire_success=1#contact')


def download_resume(request):
    """
    Serve the resume PDF for download.
    Checks if a file is uploaded in SiteConfig; returns friendly error if not.
    """
    config = SiteConfig.get_solo()

    if not config.resume_file:
        return HttpResponse(
            '<html><body style="font-family:monospace;background:#0A0A0A;color:#FF2200;'
            'display:flex;align-items:center;justify-content:center;height:100vh;margin:0;">'
            '<div style="text-align:center;">'
            '<h1 style="font-size:3rem;">RESUME NOT UPLOADED</h1>'
            '<p>The resume PDF has not been uploaded yet.<br>'
            'Check back soon or contact shikharkan.work@gmail.com</p>'
            '<a href="/" style="color:#FFEE00;">← Back to Portfolio</a>'
            '</div></body></html>',
            status=404
        )

    file_path = config.resume_file.path
    if not os.path.exists(file_path):
        raise Http404('Resume file not found on server.')

    response = FileResponse(
        open(file_path, 'rb'),
        content_type='application/pdf',
    )
    response['Content-Disposition'] = 'attachment; filename="Shikhar_Kanaujia_Resume.pdf"'
    return response
