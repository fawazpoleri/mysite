from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
from .models  import BlogDetails, Promo , branches,gallery as galry
from  website.forms import CareerForm

def index(request):
    branch_count = branches.objects.all().count()
    dict_branch = {
        'branch': branches.objects.all(),
        'branch_count' : branch_count,
        'Promo_details': Promo.objects.all(),
        'blog_details': BlogDetails.objects.all()
        
    }
    return render(request,"index.html", dict_branch)
def branch(request):
    branch_count = branches.objects.all().count()
    dict_branch = {
        'branch': branches.objects.all(),
        'branch_count' : branch_count,
        'page_name': "Our Branches"
    }
    return render(request,"branches.html",dict_branch )

def about(request):
    dict_branch = {
        'branch': branches.objects.all(),
        'page_name': "About us"
    }
    
    return render(request,"about.html",dict_branch)

def promotion(request): 
    dict_promo = {       
        'page_name': "Promotions",
        'Promo_details': Promo.objects.all()
             
    }
    return render(request,"promotion.html",dict_promo)

def blog(request):
    last = BlogDetails.objects.order_by('id')
    
    dict_blog = {
        'Last_item' : last,
        
        'page_name': "News And Updates",
        
        
        'blog_details': BlogDetails.objects.all()
        
    }
    return render(request,"blog_detail.html", dict_blog)


def contact(request):
    dict_contact = {
        
        'page_name': "Contact Us"
    }
    return render(request,"contact.html",dict_contact)

def career(request):
    dict_career = {
        
        'page_name': "Career"
    }
    return render(request,"career.html",dict_career)



def gallery(request):
    dict_gallery = {
        'gallery': galry.objects.all(),
         'page_name': "Gallery"
    }
    return render(request,"gallery.html",dict_gallery)

def CareerForm(request):
    form = CareerForm()
    form1 = {
        
         'form' : form
    }

    return render(request,"career.html",form1)





def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "career.html", context)


