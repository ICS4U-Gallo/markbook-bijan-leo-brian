from typing import Dict
import json

storage_file_path = 'markbook.json'
classroom = {}
student_info_lst = []
student_id = {}

def create_assignment(name: str, due: str, points: int) -> Dict:
  #Bijan & Nathan
  assignment = {
    "name": name, 
    "due": due,
    "points": points
    }
  
#   assignment['assignment_name'] = name
#   assignment['assignment_due'] = due
#   assignment['assignment_points'] = points

  return assignment



def create_classroom(course_code: str, course_name: str, period: int, teacher: str, student_name_lst: list) -> dict:
  #Bijan & Nathan
  global classroom, student_info_lst, student_id
  
  for name in student_name_lst:
    student_id = {}
    student_id["name"] = name
    student_id["age"] = ""
    student_id["gender"] = ""
    student_id["email"] = ""

    student_info_lst.append(student_id)
      
      
  classroom = {
    "course_code" : course_code,
    "course_name": course_name, 
    "period" : period,
    "teacher": teacher,
    "student_name_lst": student_name_lst,
    "student_info_lst": student_info_lst
  } 

  return  classroom
  
def student_info_update(name_of_student: str, age: int, gender: str, email: str,):
  #Bijan & Nathan
  global classroom, student_info_lst, student_id

  for student in classroom['student_info_lst']:
    if student['name'] == name_of_student:
      student['age'] = age
      student['gender'] = gender
      student['email'] = email
      break
      
    return classroom



#   classroom[student_info_lst][student_id][name_of_student]['age'] = age
#   classroom[student_info_lst][student_id][name_of_student]['gender'] = gender
#   classroom[student_info_lst][student_id][name_of_student]['email'] = email



def calculate_average_mark(student: Dict) -> int:
  #Bolin & Nathan & Bijan
  #total = 0
  #counter = 0
  #student_marks = student['marks']
  #for i in student_marks:
    #total += i
    #counter += 1
    #average_mark = total / counter
    #average_mark = int(average_mark)

  #return average_mark
  marks = student['marks']
  return sum(marks) / len(marks)


    
def add_student_to_classroom(new_students: dict):
  #Bijan & Nathan
  global student_info_lst
  #Debugged by Leo: type(new_students) list -> dict

  classroom['student_info_lst'].append(new_students)
  
  
def remove_student_from_classroom(remove_students: dict):
  #Bijan & Nathan
  global student_info_lst
  
  classroom['student_info_lst'].remove(remove_students)


            

def edit_student(student: Dict, **kwargs: Dict):
  #Bolin
  #for key, value in kwargs.items():
    #student[key] = value
  
  #return student
  for key in kwargs:
      student[key] = kwargs[key]
    
  return student
#Json module by Leo
def read_file():
  with open(storage_file_path, 'r') as f:
    data = json.loads(f.read())

  return data

def write_file(list):
    with open(storage_file_path, 'w') as f:
      data = json.dumps(list)
      f.write(data)
    return exit()

#UI 
def studentManagement():
  #Leo bug fix: var'student_list' -> 'student_info_lst'
  '''
  classroom = create_classroom(course_code="ICS4U",
                               course_name="Computer Science",
                               period=2,
                               teacher="Mr. Gallo",
                               student_name_lst=[])

  classroom['student_info_lst'] = [{ 'name':'Brian', 'marks':[90, 80] }, {'name':'Leo', 'marks':[70, 80]}]
  '''

  classroom = read_file()#read json file

  # Student is a dictionary that consists of the following keys: name: str, marks: list
  while True:
    print()
    print('Student Management')
    print('------------------')
    print('[1] Display students')
    print('[2] Add student')
    print('[3] Edit a student')
    print('[4] Remove student')
    print('[5] Exit app')
    print('------------------')
    print('')
    
    # Wait for user input
    option = input('Select an option [1-4]: ')

    if option == '1':
      print('')
      print('Current students:')
      for student in classroom['student_info_lst']:
        print('Name:', student['name'], ' | ', 'Average mark:', calculate_average_mark(student))
    
    elif option == '2':
      print('')
      name = input('Name: ')
      marks = input('Marks (seperated by one empty space): ')
      
      # Converting marks to a list of ints
      marksInStr = marks.split(' ')
      marksList = []
      for mark in marksInStr:
        marksList.append(int(mark))

      student = { 'name': name, 'marks': marksList }
      add_student_to_classroom(student)
      print('Student added successfully.')
    
    elif option == '4':
      print('')
      name = input('Name: ')
      student_found = False
      for student in classroom['student_info_lst']:
        if student['name'] == name:
          remove_student_from_classroom(student)
          student_found = True
          print('Student removed successfully.')
          break
      if student_found == False:
        print('Student not found.')
    
    elif option == '5':
      print('Exiting the app now.')
      write_file(classroom)
    
    else:
      print('Invalid option. Please try agian.')

    print('')

if __name__ == "__main__":    
    studentManagement()
