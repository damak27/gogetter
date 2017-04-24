from django.conf.urls import url
from django.contrib.auth import views as auth_views
from  .import views


app_name ="success"

urlpatterns = [
    url(r'^$',views.homeView.as_view(),name='home'),
   # Detail For displaying articles detail
    url(r'^/create_an_account/$',views.CreateAccount.as_view(),name='register'),
    
    url(r'/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='Detail_article'),
    
    url(r'^/login/$', auth_views.login, {'template_name': 'success/user_account/login.html'}, name='login'),
   #Direct the user to a static html page upon logout 
    #url(r'logout/$', auth_views.logout, {'template_name': 'success/user_account/logout.html'}, name='logout'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'^/AboutView/$',views.AboutView, name='about_us'),
    # this for user contact us form
    url(r'contact/add/$',views.ContactView.as_view(),name='contact_add'),
    # To view list form contact form list view
    url(r'^/ContactUsView/$',views.ContactUsView.as_view(),name='contacts'),
    # to view each objects in detail contact form details 
    url(r'(?P<pk>[0-9]+)/$',views.contact_listView.as_view(),name='contacts_list'),
]

