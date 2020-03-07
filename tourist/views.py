from django.shortcuts import render,redirect
from .forms import TouristsForm
from django.views import View
from django.contrib import messages
from .models import Tourists

# Create your views here.
class AddTouristsView(View):
    template_name = 'add_tourist.html'
    def get(self,request):
        context = {
            'form':TouristsForm
        }
        return render(request,self.template_name,context)


    def post(self,request,*args,**kwargs):
        form = TouristsForm(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,'Successfully added')
            return redirect('add_tourist')
        else:
            messages.add_message(request,messages.ERROR,'Sorry your request cannot be added')
            return redirect('add_tourist')


class AllTouristView(View):
    template_name = 'all_tourist.html'

    def get(self,request):
        context = {
            'all': Tourists.objects.filter(user_id = request.user.id)
        }
        return render(request,self.template_name,context)
        

def editTourist(request,id):
    form = TouristsForm(request.POST or None, instance=Tourists.objects.get(id=id))
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,'Successfully updated')
        return redirect('all_tourist')
    return render(request,'edit_tourist.html',context={'form':form})


def deleteTourist(request,id):
    tourist = Tourists.objects.get(id = id)
    tourist.delete()
    messages.add_message(request,messages.SUCCESS,'Successfully deleted')
    return redirect('all_tourist')