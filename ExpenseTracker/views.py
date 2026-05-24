from django.shortcuts import render,redirect
from .models import Expense
from django.contrib.auth.decorators import login_required
from .forms import AddForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login

@login_required
def list_expense(request):
    expense = Expense.objects.filter(user = request.user)
    return render(request,'expense_list.html',{'expense': expense})
@login_required    
def add_expense(request):
    if request.method== 'POST':
        form= AddForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form= AddForm()
    return render(request,'add_expense.html',{'form':form})

def register(request):
    if request.method== 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,'you get registered')
            return redirect('expense_list')
        else:
            messages.error(request,'sorry registeration is failed please check details') 
    else:
        form=UserCreationForm()
    return render(request,'register.html',{"form":form})           
    
