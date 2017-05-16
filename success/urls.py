from django.conf.urls import url
from django.contrib.auth import views as auth_views
from  .import views


app_name ="success"

urlpatterns = [
    url(r'^$',views.homeView.as_view(),name='home'),
   # Detail For displaying articles detail
    url(r'create_an_account/$',views.CreateAccount.as_view(),name='register'),
    
    url(r'(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='Detail_article'),
    
    url(r'login/$', auth_views.login, {'template_name': 'success/user_account/login.html'}, name='login'),
   #Direct the user to a static html page upon logout 
    #url(r'logout/$', auth_views.logout, {'template_name': 'success/user_account/logout.html'}, name='logout'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'AboutView/$',views.AboutView, name='about_us'),
    # this for user contact us form
    url(r'contact/add/$',views.ContactView.as_view(),name='contact_add'),
    # To view list form contact form list view
    url(r'ContactUsView/$',views.ContactUsView.as_view(),name='contacts'),
    # to view each objects in detail contact form details 
    url(r'(?P<pk>[0-9]+)/$',views.contact_listView.as_view(),name='contacts_list'),
    # urls when user login 
    url(r'profileAccount/$',views.profileAccount.as_view(),name='profile_account'),
    #Security urls
    url(r'Security/$',views.Security,name='Security'),
    url(r'Posibility/$',views.Posiblity,name='Posibility'),
    url(r'Partner/$',views.Partner,name='Partner'),
    #url(r'user_profile/(?P<profile_id>\d+)/$',views.user_profile, name="userprofile"),
    url(r'update_profile/$',views.update_profile, name="update_profile"),
   # url(r'profile/?<profile_id>\d+/$',views.user_profile, name="userprofile")

    #Profile Urls


    #url(r'profile/(?p<profile_id>\d+/$','user_profile.views.profile');
    #url(r'update_profile/(?p<profile_id>\d+/$','user_profile.views.update_profile');
    #url(r'your_profile/(?p<profile_id>\d+/$','user_profile.views.your_profile');


]

