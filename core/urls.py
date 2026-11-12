from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    path('events/', views.events_view, name='events'),
    path('join/', views.join, name='join'),
    path('contact/', views.contact_view, name='contact'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('api/newsletter-subscribe/', views.newsletter_subscribe_view, name='newsletter_subscribe'),
    path('team/', views.team_view, name='team'),
    path('join-pwbl/', views.join_pwbl_view, name='join_pwbl'),
    path('services/sky/', views.sky_service_view, name='service_sky'),
    path('services/air/', views.air_service_view, name='service_air'),
    path('services/fire/', views.fire_service_view, name='service_fire'),
    path('services/water/', views.water_service_view, name='service_water'),
    path('services/earth/', views.earth_service_view, name='service_earth'),
    path('internship/', views.internship, name='internship'),
]

handler404 = 'core.views.custom_404_view'
handler500 = 'core.views.custom_500_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)