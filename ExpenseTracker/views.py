from django.shortcuts import render,redirect, get_object_or_404
from .models import Expense
from .forms import AddForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.views.generic import ListView, DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
def cover(request):
    if request.user.is_authenticated:
        return redirect('expense_list')
    return render(request, 'cover.html') 
class ExpenseListView(LoginRequiredMixin,ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expense'
    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        
        expense = Expense.objects.filter(user=self.request.user)
        
        if query:
            expense = expense.filter(
                Q(name__icontains=query) | Q(category__icontains=query)
            )
        if category:
            expense = expense.filter(category=category)
        
        return expense
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Expense.objects.filter(user=self.request.user)\
                            .values_list('category', flat=True).distinct()
        context['selected_category'] = self.request.GET.get('category')    
        return context

class ExpenseFormMixin(LoginRequiredMixin):
    model = Expense
    template_name = 'add_expense.html'
    fields = ['name', 'amount', 'category', 'description', 'image']
    success_url = reverse_lazy('expense_list')

class AddExpense(ExpenseFormMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateExpense(ExpenseFormMixin, UpdateView):
    pass

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
class DeleteExpense(LoginRequiredMixin,DeleteView):
    model= Expense
    template_name= 'confirm.html'
    success_url= reverse_lazy('expense_list')
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

