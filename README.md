# Automated HR Leave Management System 🚀

A streamlined Django web application designed for small to medium businesses to manage employee leave requests efficiently.

## 🌟 Features
* **Employee Dashboard:** Users can apply for leaves specifying start dates, end dates, and reasons.
* **Real-time Status Tracking:** Employees can view the status of their requests (Pending, Approved, Rejected) on their personal dashboard.
* **HR / Admin Panel:** Built-in Django admin interface for HR managers to review, approve, or reject leave applications seamlessly.
* **Secure Authentication:** Only logged-in users can access the dashboard and apply for leaves.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite (Default Django DB)
* **Frontend:** HTML, Basic CSS

## ⚙️ How to Run Locally
1. Clone the repository:
   `git clone <your-github-repo-link>`
2. Navigate to the project directory:
   `cd company_hr`
3. Make migrations and migrate the database:
   `python manage.py makemigrations`
   `python manage.py migrate`
4. Create a superuser (HR Admin):
   `python manage.py createsuperuser`
5. Run the server:
   `python manage.py runserver`