from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        # Obyekt yaratishda modeldagi barcha majburiy (required) maydonlarni kiriting
        self.student = Student.objects.create(
            first_name="Ali",
            last_name="Valiyev",
            email="ali@test.com",
            password="testpassword123",
            school="1-maktab",
            grade=9,
            subject="Matematika",
            exam_date="2026-04-20", # Xatolik aynan shu yerda edi
            exam_time="09:00"
        )

    def test_create_student(self):
        """Talaba muvaffaqiyatli yaratilganini tekshirish"""
        self.assertEqual(self.student.first_name, "Ali")
        self.assertEqual(self.student.grade, 9)

    def test_delete_student(self):
        """Talaba o'chirilishini tekshirish"""
        count_before = Student.objects.count()
        self.student.delete()
        self.assertEqual(Student.objects.count(), count_before - 1)