from django.db import models
from django.contrib.auth.models import User

class LeaveRequest(models.Model):
    # Status ke options
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Database Columns
    employee = models.ForeignKey(User, on_delete=models.CASCADE) # Kisne chutti apply ki
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.username} - {self.start_date} ({self.status})"