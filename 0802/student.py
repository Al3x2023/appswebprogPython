class Student:
    count = 0  # Variable de clase para contar instancias

    def __init__(self, name, age, language, city):
        self.name = name
        self.age = age
        self.language = language
        self.city = city
        Student.count += 1  # Incrementar el contador de instancias

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Language: {self.language}, City: {self.city}"

    @classmethod
    def get_total_students_class(cls):
        return cls.count

    @classmethod
    def get_total_students(cls):
        return cls.count

# Comprobar si el script se está ejecutando directamente
if __name__ == '__main__':
    estudiante = Student(name="Juan", age=21, language="Python", city="Math")
    print(Student.get_total_students())
    print(Student.get_total_students_class())

    estudiante.name = "Josesito"

    estudiante2 = Student(name="Ana", age=21, language="Python", city="Math")
    print(Student.get_total_students())
    print(Student.get_total_students_class())
