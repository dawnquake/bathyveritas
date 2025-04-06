from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('case_studies', views.case_studies, name='case_studies'),
    path('benchmarking', views.benchmarking, name='benchmarking'),
    path('submit_benchmark', views.submit_benchmark, name='submit_benchmark'),
    path('view_benchmark', views.view_benchmark, name='view_benchmark'),
    path('product_offering', views.product_offering, name='product_offering'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
