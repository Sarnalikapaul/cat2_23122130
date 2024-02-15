from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth import authenticate, login

# Create your views here.

from django.contrib.auth.models import User


def create_user(request):
    if request.method == "POST":
        # Retrieve username and password from request
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username is provided
        if username:
            # Create user with a default last name
            user = User.objects.create_user(username=username, password=password)
            # Optionally, you can set additional user attributes here
            # Redirect to login page after successful user creation
            return redirect("login")
        else:
            # Handle the case where the username is not provided
            return render(
                request,
                "employee/create.html",
                {"error_message": "Username is required"},
            )

    return render(request, "employee/create.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("employee")  # Redirect to home page after login
        else:
            # Handle invalid login credentials here
            return render(
                request, "login.html", {"error_message": "Invalid username or password"}
            )
    else:
        return render(request, "employee/login.html")


def employee(request):
    employees = Task.objects.all()
    total_employees = employees.count()
    return render(
        request,
        "employee/employee.html",
        {"employees": employees, "total_employees": total_employees},
    )


def add_employee(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        task = request.POST["task"]

        # Create the employee object
        employee = Task.objects.create(
            name=name, email=email, address=address, phone=phone, task=task
        )

        # Optionally, you can perform validation here before saving the employee object

        # Save the employee object
        employee.save()

        return redirect("employee")  # Redirect to employee list page
    else:
        return render(request, "employee/employee.html")


def employee_list(request):
    employees = Task.objects.all()
    total_employees = employees.count()
    return render(
        request,
        "employee/employee.html",
        {"employees": employees, "total_employees": total_employees},
    )


def edit_employee(request, employee_id):
    employee = get_object_or_404(Task, pk=employee_id)

    if request.method == "POST":
        # Update employee data
        employee.name = request.POST["name"]
        employee.email = request.POST["email"]
        employee.address = request.POST["address"]
        employee.phone = request.POST["phone"]
        employee.task = request.POST["task"]
        employee.save()

        return redirect("employee")  # Redirect to employee list page

    return render(request, "employee/edit.html", {"employee": employee})


def delete_employee(request, employee_id):
    # Retrieve the employee object or return 404 if not found
    employee = get_object_or_404(Task, pk=employee_id)

    if employee:
        # If the request method is POST, it means the user confirmed deletion
        employee.delete()
        return redirect("employee")  # Redirect to employee list page

    return render(request, "employee/delete.html", {"employee": employee})
