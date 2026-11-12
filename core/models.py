from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactInquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=200, default='General Inquiry')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Event(models.Model):
    STATUS_CHOICES = (
        ('UPCOMING', 'Upcoming Event'),
        ('PAST', 'Past Event / Archive'),
    )
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UPCOMING')
    event_type = models.CharField(max_length=100, default="Conference")
    category = models.CharField(max_length=100, default="Innovation & Tech")
    location = models.CharField(max_length=250, default="Jaipur, Rajasthan")
    day_str = models.CharField(max_length=10, default="20")
    month_str = models.CharField(max_length=10, default="APR")
    date_str = models.CharField(max_length=120, default="2026-10-15 @ 10:00 AM - 04:00 PM")
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_status_display()}] {self.title}"

class JobApplication(models.Model):
    roles = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    experience_years = models.CharField(max_length=50)
    bio_description = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.roles}"

class AppointmentBooking(models.Model):
    date = models.CharField(max_length=50)
    time_slot = models.CharField(max_length=50, default="11:00 AM - 12:00 PM")
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment on {self.date}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class InternshipApplication(models.Model):
    DOMAIN_CHOICES = [
        ('tech_dev', 'Software & Web Development'),
        ('clean_energy', 'Clean Energy & Sustainability Research'),
        ('data_analytics', 'Data Analysis & Market Research'),
        ('digital_marketing', 'Digital Marketing & Outreach'),
        ('operations', 'Project Operations & Management'),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES)
    resume = models.FileField(upload_to='resumes/')
    statement = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_domain_display()}"
class AppointmentBooking(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_or_college = models.CharField(max_length=200, blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=50)
    purpose = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-appointment_date', '-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date} ({self.appointment_time})"

