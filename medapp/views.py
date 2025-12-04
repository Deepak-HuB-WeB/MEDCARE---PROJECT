from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm


# Authentication
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'medapp/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard with DB counts
@login_required
def dashboard(request):
    context = {
        "total_doctors": Doctor.objects.count(),
        "total_patients": Patient.objects.count(),
        "total_appointments": Appointment.objects.count(),
    }
    return render(request, 'medapp/dashboard.html', context)


# ================= Doctors CRUD =================
@login_required
def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'medapp/doctors.html', {"doctors": doctors})


@login_required
def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully!")
            return redirect('doctors')
    else:
        form = DoctorForm()

    return render(request, 'medapp/add_doctor.html', {"form": form})


@login_required
def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor updated successfully!")
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'medapp/edit_doctor.html', {"form": form})


@login_required
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    messages.warning(request, "Doctor deleted!")
    return redirect('doctors')


# ================= Patients CRUD =================
@login_required
def patients(request):
    patients = Patient.objects.all()
    return render(request, 'medapp/patients.html', {"patients": patients})

@login_required
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient added successfully!")
            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'medapp/add_patient.html', {"form": form})



@login_required
def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully!")
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'medapp/edit_patient.html', {"form": form})


@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.warning(request, "Patient deleted!")
    return redirect('patients')


# ================= Appointments CRUD =================
@login_required
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'medapp/appointments.html', {"appointments": appointments})


@login_required
def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment added successfully!")
            return redirect('appointments')
    else:
        form = AppointmentForm()

    return render(request, 'medapp/add_appointment.html', {"form": form})



@login_required
def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect('appointments')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'medapp/edit_appointment.html', {"form": form})


@login_required
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    messages.warning(request, "Appointment deleted!")
    return redirect('appointments')
