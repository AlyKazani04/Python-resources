class lesson:
    def __init__(self,t,m,r):
        self.lessonTitle = t
        self.durationMins = m
        self.LabRequired = r
    
    
    def outputLessonDetails(self):
        print("Lesson title:" , self.lessonTitle)
        print("Duration in Mins:", self.durationMins)
        print("Is lab required:" , self.LabRequired)

class assessment:
    def __init__(self,t,m):
        self.assessmentTitle = t
        self.maxMarks = m
    def outputAssessmentDetails(self):
        print("Assessment title:", self.assessmentTitle)
        print("Max marks:", self.maxMarks)

class course:
    def __init__(self,t,m,n):
        self.CourseTitle = t
        self.maxStds = m
        self.numofLessons = n
        self.courseLesson = []
        self.courseAssessment = assessment
    def addLesson(self,t,m,r):
        self.courseLesson.append(lesson(t,m,r))
    def addAssessment(self,t ,m):
        self.courseAssessment = assessment(t,m)
    
    def outputCourseDetails(self):
        print("Course Title:" , self.CourseTitle)
        print("Total Students:", self.maxStds)
        print("Total Lessons:", self.numofLessons)
        for i in range(self.numofLessons):
            print(self.courseLesson[i].outputLessonDetails())
        self.courseAssessment.outputAssessmentDetails()

mycourse = course("Computer Science", 25,2)
mycourse.addAssessment("Mock P4", 75)
mycourse.addLesson("Containment", 45, True)
mycourse.addLesson("Files" ,45, True)
mycourse.outputCourseDetails()