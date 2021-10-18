def get_student_score(self):
        return self.student_name
    
    def get_student_score(self):
        return self.student_score

    def set_student_score(self, value):
        self.student_name = value
    
    def set_student_score(self, value):
        self.student_score = value

    #- class method working on a class attribute
    @classmethod   
    def student_num(cls):
        cls.count_Students += 1
