from django.shortcuts import render,redirect, get_object_or_404
from .models import Expense
from django.contrib.auth.decorators import login_required
from .forms import AddForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q

@login_required
def list_expense(request):
    quary= request.GET.get('q')
    if quary:
        expense= Expense.objects.filter(Q(name__icontains=quary)|Q(category__icontains=quary),user=request.user)
    else:    
        expense = Expense.objects.filter(user = request.user)
    return render(request,'expense_list.html',{'expense': expense})
@login_required    
def add_expense(request):
    if request.method== 'POST':
        form= AddForm(request.POST,request.FILES)
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
@login_required
def edit_expense(request,pk):
    expense= get_object_or_404(Expense,pk=pk,user=request.user)
    if request.method=='POST':
        form=AddForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request,'you edited the expense')
            return redirect('expense_list')
        else:
            messages.error(request, 'please check the error')
    else:
        form=AddForm(instance=expense)
    return render(request,'add_expense.html', {'form':form})
@login_required
def delete_expense(request,pk):
    expense=get_object_or_404(Expense,pk=pk,user=request.user)
    if request.method=='POST':
        expense.delete()
        return redirect('expense_list')
    return render(request,'confirm.html',{'expense': expense})    

