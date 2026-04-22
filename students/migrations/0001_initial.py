from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('course_interest', models.CharField(choices=[('python', 'Python & Data Science'), ('webdev', 'Full-Stack Web Development'), ('ai_ml', 'AI & Machine Learning'), ('mobile', 'Mobile App Development'), ('cybersec', 'Cybersecurity'), ('devops', 'DevOps & Cloud'), ('other', 'Other')], max_length=50)),
                ('status', models.CharField(choices=[('new', 'New Lead'), ('contacted', 'Contacted'), ('enrolled', 'Enrolled'), ('dropped', 'Dropped')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
