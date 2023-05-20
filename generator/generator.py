import random
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        date_of_birth=faker_ru.date(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10000, 100000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    path = rf'D:\PythonHarper\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_subject():
    subject_dict = {1: "Hindi",
                    2: "English",
                    3: "Maths",
                    4: "Physics",
                    5: "Chemistry",
                    6: "Biology",
                    7: "Computer Science",
                    8: "Commerce",
                    9: "Accounting",
                    10: "Economics",
                    11: "Arts",
                    12: "Social Studies",
                    13: "History",
                    14: "Civics"
                    }
    return subject_dict[random.randint(1, 14)]
