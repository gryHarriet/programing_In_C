#ObjectOriented programing

class student:
    def kcpe(self):
      if self.exams <= 50:
        return "Fail"
      else:
         return "Congratulations"
    
    def __init__(self, name, exams):
        self.name = name
        self.exams = exams
      
student1 = student("Kev", 80)
print(student1.name)
print(student1.exams)
results = student1.kcpe()
print(results)
