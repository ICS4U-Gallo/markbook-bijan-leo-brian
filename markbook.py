"""
Markbook Application
Group members: 
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
  assignment = {}
  assignment['assignment_name'] = name
  assignment['assignment_due'] = due
  assignment['assignment_points'] = points

  return assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
  classroom = {}
  classroom['course_code'] = course_code
  classroom['course_name'] = course_name
  classroom['period'] = period
  classroom['teacher'] = teacher
  
  return classroom


def test_calculate_average_mark(student: Dict) -> float:
  total = 0
  counter = 0
  for i in student['marks']:
    total += i
    counter += 1
  average_mark = total / counter

  return average_mark


def add_student_to_classroom(student: Dict, classroom: Dict):

  classroom['student_list'].append(student)
  return classroom
    


def remove_student_from_classroom(student: Dict, classroom: Dict):

  del classroom['student']
  return classroom


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
