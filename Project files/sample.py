class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_name(self):
        return self.name

   
    def get_age(self):
        return self.age    
    
    def get_grade(self):
        pass

class student(person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

   
    def get_grade(self):
        if self.marks >= 90 and self.marks <= 100:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
n, a, m = input().split()
s1 = student(n,a,int(m))    
print(f'{s1.get_name()}: {s1.get_name()}')    
print(f'{s1.get_age()}: {s1.get_age()}')    
print(f'{s1.get_grade()}: {s1.get_grade()}')c