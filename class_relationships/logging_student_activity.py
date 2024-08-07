from abc import ABC, abstractmethod

# This interface done by inheriting from ABC.

class LoggingStudentActivity(ABC):

    @abstractmethod
    def log_student_activity(self, activity_description):
        pass