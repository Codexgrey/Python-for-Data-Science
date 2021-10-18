#-- OOP Continues...
class EthnicMeal:
    def igbo(self):
        print("Akpu")

    def yoruba(self):
        print("Amala")

    def hausa(self):
        print("Tuwo Shinkafa")

# food_one = EthnicMeal()
# food_one.igbo()

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Accessor Instance Methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    # Mutator Instance Methods
    def set_name(self, value):
        self.name = value

    def set_age(self, value):
        self.age = value

    def set_gender(self, value):
        self.gender = value
    

s1 = Student("Bobby", 15, "Male")
s2 = Student("Aliyah", 19, "Female")
# print(s1.get_name())
# print(s2.get_name())

# get_data = input("Enter new name here: ")
# s2.set_name(get_data)
# print(s2.get_name())


class School:
    #- class attribute
    count_Students = 0 
    sum_scores = 0

    def __init__(self, student_name, student_score):
        self.student_name = student_name
        self.student_score = student_score
        self.student_num()
        School.sum_scores += self.get_student_score()

    def __add__(self, other):
        sum = self.student_score + other.student_score
        return sum

    def get_student_name(self):
        return self.student_name
    
    def get_student_score(self):
        return self.student_score

    def set_student_name(self, value):
        self.student_name = value
    
    def set_student_score(self, value):
        self.student_score = value

    #- class method working on a class attribute
    @classmethod   
    def student_num(cls):
        cls.count_Students += 1
  
    @classmethod
    def average_score(cls):
        output = cls.sum_scores / cls.count_Students
        return round(output, 2)

    @staticmethod
    def info():
        print("This is a class for students.")
        



    
p1 = School("Jesse", 61.56), School("Brian", 80.0)
p2 = School("Mac Intre", 71.00)
School.student_num()
# output = p1 + p2
# print(p1[1].get_student_name())
# print(output)
# print(School.count_Students)
# print(School.average_score())


class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_rating(self):
        return self.rating

class Platform:
    def __init__(self, name, max_movies):
        self.name = name
        self.max_movies = max_movies
        self.movie_list = []

    def add_movie(self, value):
        if len(self.movie_list) < self.max_movies:
            self.movie_list.append(value)
        else:
            print("Can't take in anymore movies")

    def get_average_rating(self):
        ratingSum = 0
        for movie in self.movie_list:
            ratingSum += movie.get_rating()

        average = ratingSum/len(self.movie_list)
        return round(average, 2)



m1 = Movie("Interstellar", 2015, 3.8)
m2 = Movie("Inception", 2010, 4.0)
m3 = Movie("Joker", 2019, 4.2)
m4 = Movie("In Time", 2012, 4.9)

p1 = Platform("HBO", 3)
p1.add_movie(m1)
p1.add_movie(m2)
p1.add_movie(m3)
p1.add_movie(m4)

# print(p1.movie_list)
# print(p1.get_average_rating())
# for instance in p1.list_of_movies:
#     print(instance.get_title())


#-- error handling
try:
    wrong = 10 + "10"
except:
    wring = 10 + 5


#--- Databases

