from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()

    # Search
    search_query = request.GET.get('search', '').strip()
    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    # Filter by course
    course_filter = request.GET.get('course', '').strip()
    if course_filter:
        students = students.filter(course_interest=course_filter)

    # Filter by status
    status_filter = request.GET.get('status', '').strip()
    if status_filter:
        students = students.filter(status=status_filter)

    # Stats for dashboard
    total = Student.objects.count()
    enrolled = Student.objects.filter(status='enrolled').count()
    new_leads = Student.objects.filter(status='new').count()
    contacted = Student.objects.filter(status='contacted').count()

    context = {
        'students': students,
        'total_students': total,
        'enrolled_count': enrolled,
        'new_leads_count': new_leads,
        'contacted_count': contacted,
        'course_choices': Student.COURSE_CHOICES,
        'status_choices': Student.STATUS_CHOICES,
        'search_query': search_query,
        'course_filter': course_filter,
        'status_filter': status_filter,
        'result_count': students.count(),
    }
    return render(request, 'students/student_list.html', context)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'✅ {student.name} has been added successfully!')
            return redirect('student_list')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ {student.name} updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/add_student.html', {
        'form': form,
        'edit_mode': True,
        'student': student,
    })


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.success(request, f'🗑️ {name} has been removed.')
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})
