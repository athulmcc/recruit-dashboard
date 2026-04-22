from django.db import models


class Student(models.Model):
    COURSE_CHOICES = [
        ('python', 'Python & Data Science'),
        ('webdev', 'Full-Stack Web Development'),
        ('ai_ml', 'AI & Machine Learning'),
        ('mobile', 'Mobile App Development'),
        ('cybersec', 'Cybersecurity'),
        ('devops', 'DevOps & Cloud'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('new', 'New Lead'),
        ('contacted', 'Contacted'),
        ('enrolled', 'Enrolled'),
        ('dropped', 'Dropped'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    course_interest = models.CharField(max_length=50, choices=COURSE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email})"
