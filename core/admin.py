from django.contrib import admin
from .models import (
    BlogPost,
    ContactInquiry,
    Event,
    JobApplication,
    AppointmentBooking,
    NewsletterSubscriber,
    InternshipApplication,
)


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'event_type', 'date_str', 'location')
    list_filter = ('status', 'event_type')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'experience_years', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'roles')


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)

@admin.register(InternshipApplication)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'college', 'domain', 'applied_at')
    search_fields = ('full_name', 'email', 'college')
    list_filter = ('domain', 'applied_at')
    readonly_fields = ('applied_at',)

@admin.register(AppointmentBooking)
class AppointmentBookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'appointment_date', 'appointment_time', 'created_at')
    list_filter = ('appointment_date', 'appointment_time')
    search_fields = ('full_name', 'email', 'phone', 'company_or_college')
    ordering = ('-appointment_date',)
    readonly_fields = ('created_at',)
