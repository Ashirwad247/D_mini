from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivityForm
from .models import Activity
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivityForm
from .models import Activity
from datetime import timedelta

def index(request):
    activities = Activity.objects.all()
    return render(request, 'tracker/index.html', {'activities': activities})

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            # Convert hours to timedelta and save it in time_spent
            time_spent_hours = int(request.POST.get('time_spent_hours'))
            activity.time_spent = timedelta(hours=time_spent_hours)
            # Save activity (automatically calculates score in model)
            activity.save()
            return redirect('index')
    else:
        form = ActivityForm()
    
    return render(request, 'tracker/add_activity.html', {'form': form})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'tracker/activity_detail.html', {'activity': activity})

def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    time_spent_hours = activity.time_spent.total_seconds() / 3600
    
  
    time_spent_hours = int(time_spent_hours) if time_spent_hours.is_integer() else time_spent_hours

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            time_spent_hours_input = request.POST.get('time_spent_hours')
            if time_spent_hours_input:
                activity.time_spent = timedelta(hours=float(time_spent_hours_input))
            activity.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)

    return render(request, 'tracker/edit_activity.html', {
        'form': form, 
        'activity': activity, 
        'time_spent_hours': time_spent_hours
    })




def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('index')  
    return render(request, 'tracker/delete_activity.html', {'activity': activity})
