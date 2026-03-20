from django.shortcuts import render,redirect,get_object_or_404
from .models import Transaction,New_user
from .forms import TransactionForm,RegisterForm,LoginForm
from django.db.models import Sum
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
 






# Create your views here.



def home(request):
    return render(request, 'home.html')
@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request,'transaction_list.html', {'transactions': transactions})

# Create View
@login_required
def transaction_create(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('transaction_list')
    return render(request,'transaction_form.html', {'form': form})

# Update View
@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        return redirect('transaction_list')
    return render(request,'transaction_form.html', {'form': form})

# Delete View
@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('transaction_list')

# Summary View
@login_required
def summary_view(request):
    income = Transaction.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Transaction.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expense

    return render(request, 'summary.html', {
        'income': income,
        'expense': expense,
        'balance': balance
    })

#reg view


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'reg.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('transaction_list')  # change to your home page
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'log.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('/')




