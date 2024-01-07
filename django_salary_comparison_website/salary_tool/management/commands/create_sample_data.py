from django.core.management.base import BaseCommand
from salary_tool.models import Job, SalaryData
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to create sample data...'))

        job_titles = ['Data Scientist', 'Software Engineer', 'Product Manager', 'UX Designer', 'Data Analyst', 'DevOps Engineer', 'Marketing Specialist']
        experience_years_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for title in job_titles:
            Job.objects.create(title=title)

        for _ in range(200):  # You can adjust the number of entries
            job = random.choice(Job.objects.all())
            salary = Decimal(random.uniform(500, 5000))
            experience_years = random.choice(experience_years_choices)
            gender = random.choice(['male', 'female'])

            SalaryData.objects.create(
                job=job,
                salary=salary,
                experience_years=experience_years,
                gender=gender
            )

        self.stdout.write(self.style.SUCCESS('Sample data creation complete.'))
