from django.shortcuts import render,redirect,HttpResponse
from .models import upload,Employee, Task
from datetime import datetime


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def registerpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        empid = request.POST.get('empid')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = Employee(name=name, empid=empid, username=username, password=password)
        users.save()
        return redirect('employee_login')
    return render(request, 'registerpage.html')

def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            Employee.objects.get(username=username, password=password)
            return redirect('/task_list')
        except:
            return HttpResponse('Invalid Page ')
    return render(request, 'employee_login.html')

def manager(request):
        details = Employee.objects.filter(Status=False)
        return render(request, 'Manager Approval.html', {'value': details})

def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('/create_task')
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'manager_login.html')


def approve(request,id):
    data = Employee.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/manager')

def edit(request,id):
    details = Employee.objects.all()
    users = Employee.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        empid = request.POST.get('empid')
        projectname = request.POST.get('projectname')
        status = request.POST.get('status')
        users.Name = name
        users.EmpID = empid
        users.Projectname = projectname
        users.Status = status
        users.save()
        return redirect('/manager')
    return render(request,'Manager Approval.html',{'value':details,'a':users})

def delete(request,id):
    data = Employee.objects.filter(id=id).delete()
    return redirect('/manager')

def task_list(request):
    if request.user.is_authenticated:
        employee = Employee.objects.get(user=request.user)
        tasks = Task.objects.filter(assigned_to=employee)
        if request.method == 'POST':
            task_id = request.POST.get('task_id')
            new_status = request.POST.get('status')
            new_status_description = request.POST.get('status_description')
            task = Task.objects.get(id=task_id)
            task.status = new_status
            if new_status_description:
                task.status_description = new_status_description
            task.save()
    else:
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'empid': employee.empid if request.user.is_authenticated else None})

def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    employee = task.assigned_to
    task_name = task.name
    task_description = task.description
    if request.method == 'POST':
        new_status = request.POST.get('status')
        new_status_description = request.POST.get('status_description')
        task.status = new_status
        task.status_description = new_status_description
        task.save()
        return redirect('task_list')
    return render(request, 'update_task_status.html', {'task': task,'employee': employee,'task_name': task_name, 'task_description': task_description})

def create_task(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        name = request.POST.get('name')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        assigned_to = Employee.objects.get(empid=request.POST.get('assigned_to'))
        task = Task(name=name, description=description, due_date=due_date, assigned_to=assigned_to)
        task.save()
        return redirect('task_list')
    employees = Employee.objects.all()
    return render(request, 'create_task.html', {'employees': employees})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.due_date = datetime.strptime(request.POST.get('due_date'), '%Y-%m-%d').date()
        task.status = request.POST.get('status')
        assigned_to_id = request.POST.get('assigned_to')
        task.assigned_to = Employee.objects.get(id=assigned_to_id)
        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    else:
        return render(request, 'delete_task.html', {'task': task})


# Create your views here.
