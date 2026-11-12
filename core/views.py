from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    BlogPost, 
    ContactInquiry, 
    Event, 
    JobApplication, 
    AppointmentBooking, 
    NewsletterSubscriber,
    InternshipApplication
)

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {'posts': posts})

def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    recent_posts = BlogPost.objects.exclude(id=post.id).order_by('-published_date')[:3]
    return render(request, 'blog_detail.html', {'post': post, 'recent_posts': recent_posts})

def events_view(request):
    upcoming_events = Event.objects.filter(status='UPCOMING').order_by('-created_at')
    past_events = Event.objects.filter(status='PAST').order_by('-created_at')
    recent_posts = BlogPost.objects.all().order_by('-published_date')[:3]
    return render(request, 'events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'recent_posts': recent_posts,
    })

def join(request):
    if request.method == 'POST':
        # 1. Grab values submitted by the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_or_college = request.POST.get('company_or_college')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        purpose = request.POST.get('purpose')

        # 2. Check that a date and slot were actually selected
        if not appointment_date or not appointment_time:
            messages.error(request, "Please select both a date and an appointment slot.")
            return redirect('join')

        # 3. Create a new record in the database
        AppointmentBooking.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            company_or_college=company_or_college,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            purpose=purpose
        )

        # 4. Display a confirmation message and refresh the page
        messages.success(request, f"Appointment successfully scheduled for {appointment_date} at {appointment_time}!")
        return redirect('join')

    # If someone just visits the page via GET, simply load the template
    return render(request, 'join.html')


def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', 'General Inquiry')
        message = request.POST.get('message', '')
        
        if name and email and message:
            ContactInquiry.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            success = True
            
    return render(request, 'contact.html', {'success': success})

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def newsletter_subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing!'})
            return JsonResponse({'status': 'info', 'message': 'You are already subscribed.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid email address.'}, status=400)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)
def team_view(request):
    return render(request, 'team.html')
def join_pwbl_view(request):
    return render(request, 'join_pwbl.html')  # or render your respective template
def sky_service_view(request):
    return render(request, 'sky.html')  # remove 'services/'
def air_service_view(request):
    return render(request, 'air.html')  # Removed 'services/' prefix
def fire_service_view(request):
    return render(request, 'fire.html')  # Removed 'services/' prefix
def water_service_view(request):
    return render(request, 'water.html')
def earth_service_view(request):
    return render(request, 'earth.html')

def internship(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        degree = request.POST.get('degree')
        domain = request.POST.get('domain')
        resume = request.FILES.get('resume')
        statement = request.POST.get('statement')

        # Save to database
        InternshipApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            college=college,
            degree=degree,
            domain=domain,
            resume=resume,
            statement=statement
        )

        messages.success(request, 'Your internship application has been submitted successfully!')
        return redirect('internship')

    return render(request, 'internship.html')



