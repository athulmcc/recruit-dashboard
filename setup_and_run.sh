#!/bin/bash
# ============================================
#  Recruit Dashboard - Quick Setup Script
# ============================================

echo "🎓 Setting up Recruit Dashboard..."
echo ""

# Check Python
python3 --version || { echo "❌ Python 3 required"; exit 1; }

# Install Django
echo "📦 Installing Django..."
pip install django --quiet

# Run migrations (already generated, just apply them)
echo "🗄️  Running migrations..."
python3 manage.py migrate

# Create superuser non-interactively
echo "👤 Creating superuser (admin / admin123)..."
python3 manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('  Superuser created: admin / admin123')
else:
    print('  Superuser already exists')
"

# Seed sample data
echo "🌱 Seeding sample students..."
python3 manage.py shell -c "
from students.models import Student
students = [
    {'name': 'Priya Sharma', 'email': 'priya@example.com', 'course_interest': 'ai_ml', 'status': 'new'},
    {'name': 'Arjun Nair', 'email': 'arjun@example.com', 'course_interest': 'webdev', 'status': 'contacted'},
    {'name': 'Meera Krishnan', 'email': 'meera@example.com', 'course_interest': 'python', 'status': 'enrolled'},
    {'name': 'Rahul Menon', 'email': 'rahul@example.com', 'course_interest': 'devops', 'status': 'new'},
    {'name': 'Lakshmi Pillai', 'email': 'lakshmi@example.com', 'course_interest': 'cybersec', 'status': 'contacted'},
]
count = 0
for s in students:
    obj, created = Student.objects.get_or_create(email=s['email'], defaults=s)
    if created: count += 1
print(f'  Added {count} sample students')
"

echo ""
echo "✅ Setup complete!"
echo ""
echo "  🌐 App:   http://127.0.0.1:8000/"
echo "  🔒 Admin: http://127.0.0.1:8000/admin/"
echo "  👤 Login: admin / admin123"
echo ""
echo "Starting server..."
python3 manage.py runserver
