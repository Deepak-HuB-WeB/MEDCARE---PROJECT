# 🏥 MEDCARE - Hospital Management System

MEDCARE is a web-based Hospital Management System built using Django & MySQL. It helps hospitals manage Doctors, Patients, and Appointments efficiently and digitally with an easy-to-use interface.

-------------------------------------------------------------

## 🚀 Features

✔️ Doctor Management – Add, View, Edit, Delete doctors  
✔️ Patient Management – Manage patient details and records  
✔️ Appointment Scheduling – Book appointments with doctors  
✔️ User Authentication – Secure login system  
✔️ Admin Dashboard – Statistics & data panels  
✔️ Responsive UI – Works on desktop and mobile  

-------------------------------------------------------------

## 🛠️ Tech Stack

| Component     | Technology |
|---------------|------------|
| Backend       | Django (Python) |
| Frontend      | HTML, CSS, Bootstrap |
| Database      | MySQL |
| Authentication| Django Auth System |

-------------------------------------------------------------

## 📌 Requirements

Before running this project, make sure you have installed:

🔹 Python 3.6+  
🔹 Django  
🔹 MySQL  
🔹 MySQL Connector (mysqlclient or pymysql)

-------------------------------------------------------------

## 📥 Installation & Setup Guide

Follow the steps below to run this project on your system:

### 1️⃣ Clone the Repository
git clone https://github.com/Deepak-HuB-WeB/MEDCARE---PROJECT.git
cd MEDCARE---PROJECT

### 2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate   (For Windows)

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Configure MySQL Database

Create a MySQL database (example name):
medcare_db

Then open settings.py and update:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medcare_db',
        'USER': 'root',
        'PASSWORD': '',      
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### 5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 6️⃣ Create Superuser
python manage.py createsuperuser

### 7️⃣ Run the Server
python manage.py runserver

-------------------------------------------------------------

🌐 OPEN PROJECT IN BROWSER:
http://127.0.0.1:8000/

🔐 ADMIN LOGIN:
http://127.0.0.1:8000/admin/
(Use superuser credentials)

-------------------------------------------------------------

## 💡 Tips

📌 If mysqlclient fails installation, install pymysql instead:
pip install pymysql

That concludes the project...


