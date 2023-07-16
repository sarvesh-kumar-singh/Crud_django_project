from django.shortcuts import render,HttpResponseRedirect,redirect
from .form import StudentRegistration
from .models import User



# This Function is used to Add New Student and show all student  
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
         nm=fm.cleaned_data['name']
         em=fm.cleaned_data['email']
         pw=fm.cleaned_data['password']
         reg=User(name=nm,email=em,password=pw)
         reg.save()
         fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stu=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stu})



# This function is used to Update Student data 
def update_data(request,id):
   if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
         fm.save()
        # return HttpResponseRedirect('/')
   else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
   return render (request,'enroll/updatestudent.html',{'form':fm})




   




    
# This function is used to Delete items
def delete_data(request, id):
   if request.method == 'POST':
      pi = User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')