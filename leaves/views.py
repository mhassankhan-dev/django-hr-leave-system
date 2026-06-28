from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest
from .forms import LeaveApplyForm

# 1. Chutti Apply Karne Ka View
@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveApplyForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False) # Abhi database mein save mat karo
            leave.employee = request.user   # Current logged-in user ko assign karo
            leave.save()                    # Ab finally save kar do
            return redirect('dashboard')
    else:
        form = LeaveApplyForm()
    
    return render(request, 'leaves/apply_leave.html', {'form': form})

# 2. Dashboard View (Jahan status nazar aayega)
@login_required
def dashboard(request):
    # Sirf us user ki leaves filter karo jo logged in hai
    my_leaves = LeaveRequest.objects.filter(employee=request.user).order_by('-applied_on')
    return render(request, 'leaves/dashboard.html', {'leaves': my_leaves})