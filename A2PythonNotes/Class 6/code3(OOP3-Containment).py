class Lesson:
    def __init__(self, t, d, r):
        self.__LessonTitle = t
        self.__DurationMinutes = d
        self.__RequiresLab = r
    def OutputLessonDetails(self):
        print(self.__LessonTitle)
        print("Total time in minutes:", self.__DurationMinutes)
        print("Lab:", self.__RequiresLab)

class Assessment:
    def __init__(self, t, m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m
    def OutputAssessmentDetails(self):
        print(self.__AssessmentTitle)
        print("Maximum Marks:", self.__MaxMarks)

class Course:
    def __init__(self, t, m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = Assessment
    def AddLesson(self, t, d, r):
        self.__NumberOfLessons += 1
        self.__CourseLesson.append(Lesson(t, d, r))
    def AddAssessment(self, t, m):
        self.__CourseAssessment = Assessment(t, m)
    def OutputCourseDetails(self):
        print(self.__CourseTitle)
        print()
        print("Maximum Students:", self.__MaxStudents)
        print()
        print("Total Lessons:", self.__NumberOfLessons)
        print()
        print(self.__CourseAssessment.OutputAssessmentDetails())
        print()
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())
            print()

MyCourse = Course("Computer Science", 30)       # sets up new course

MyCourse.AddAssessment("Programming", 75)       # adds an assessment

MyCourse.AddLesson("Problem Solving", 60, False)        # adds 3 lessons
MyCourse.AddLesson("Programming", 120, True)
MyCourse.AddLesson("Theory", 120, False)

MyCourse.OutputCourseDetails()      # prints all details
