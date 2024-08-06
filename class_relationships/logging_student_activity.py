from abc import ABC, abstractmethod

class LoggingStudentActivity(ABC):

    @abstractmethod
    def log_student_activity(self, activity_description):
        pass