from django.views import generic
from success.models import Articles,Contact,Quotes,UserProfile
from django.views.generic import View
from success.forms import Creat_account #,UserProfileForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# this will redirect you to a another link  once your model field successfully field
from  django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response




        # Home page for about us
def AboutView(request):
     content = ""#home_detail.objects.all()     
     return render(request,"success/about_us.html",{'content':content})
# Sucurity view
def Security(request):
    content = ""
    return render(request, "success/gogetter_static_pages/security.html",{'content':content})
def Posiblity(request):
    content = ""
    return render(request, "success/gogetter_static_pages/posibility.html",{'content':content})

#To Display detail of the Article objects in home page
class DetailView(generic.DetailView):
    model = Articles
    template_name ='success/detail_page.html'
    
            # views  for  user login`
class profileAccount(generic.ListView):
    model = UserProfile
    template_name ='success/user_account/profile_account.html'
# View To Create  User account
class CreateAccount(View):
    form_class = Creat_account
    template_name = 'success/user_account/registration_form.html'
    # the get() will get the registration form when ever the user call it 
      
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    # this will submit the form when the user press the submit
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #clean normalize Data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #Returns user objects if Crendentials Correct
            # Verifies if usernama,email,company exist in the database
            user = authenticate(username=username,password=password,email=email)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # The user will be redirected to this page on successful account creation 
                    return redirect('success:profile_account')
        return render(request,self.template_name,{'form':form})
  # for creating the user contact form       
class  ContactView(CreateView):
    model = Contact
    fields =   ['First_name','Last_name','phone_number','Country','email_address','text_content']
    # will redirect the user to another page on success
    success_url = reverse_lazy('success:contacts')
    # View to view information of users contact form
class ContactUsView(generic.ListView):
    template_name = 'success/contactlistview_page.html'  
    context_object_name ="contact"  
    def get_queryset(self):
        return Contact.objects.order_by('Country')
    def get_context_data(self,**kwargs):
        context = super(ContactUsView,self).get_context_data(**kwargs)
        context['article'] = Articles.objects.order_by('Created_time')
        return context
        
     
        
        
        
        # Views the details of users form submit 
        # this view will be redirected to the user after summiting contact form  from ContactView 
class contact_listView(generic.DetailView):
    model = Contact,
 
    template_name = 'success/contact_detailview.html'
    #Generic view to display home_page when user visit the site 

# Home page view 
class homeView(generic.ListView):
    template_name = 'success/home_page.html' 
    context_object_name="articles"   
    def get_queryset(self):
        return Articles.objects.order_by('article_title')
    def get_context_data(self,**kwargs):
        contex = super(homeView,self).get_context_data(**kwargs)
        contex['quote']=Quotes.objects.order_by('quote')
        return contex
        """
# user profile view 
@login_required
def update_profile(request):
    userprofile = UserProfile.object.get(user=request.user)
    form = UserProfileForm(initial={'bio':userprofile.bio})
    return render_to_response('success/update_profile.html',{'form':form},RequestContext(request))

"""