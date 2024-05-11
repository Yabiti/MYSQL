def __int__(self, name, house):
    self.name = name
    self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")