class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age



    def show_info(self):
        print(f"Name: {self.name} ") 
        print(f"Age: {self.age} ") 
       

class Student(Person):
        School_name = "ABC School"

        def __init__(self, name, age,class_name,roll,marks = 0):
            super().__init__(name, age)

            self.class_name = class_name
            self.roll = roll
            self.__marks = 0
            self.set_marks(marks)

        #setter method    

        def set_marks(self,marks):

            if 0 <= marks <= 100:
                 self.__marks = marks
            else:
                 print('Invalid marks! Marks must be between 0 to 100')

        #getter method
        def get_marks(self):
             return self.__marks 

        def grade(self):

            if 80 <= self.__marks <= 100:
                return "A+"

            elif 70 <= self.__marks <= 79:
                return "A"

            elif 65 <= self.__marks <= 69:
                return "A-"

            elif 60 <= self.__marks <= 64:
                return "B+"

            elif 55 <= self.__marks <= 59:
                return "B"

            elif 50 <= self.__marks <= 54:
                return "C+"

            elif 40 <= self.__marks <= 49:
                return "C"

            else:
                return "Fail"   

        def show_info(self):
            super().show_info() 
            print(f"Class: {self.class_name}")   
            print(f"Roll: {self.roll}")  
            print(f"Marks: {self.__marks}")  
            print(f"Grade: {self.grade()}") 
