# Importing the modules from the created file
from Student.add_student import add_student 
from Teacher.add_teacher import add_teacher
from utilityy.logger import log_message

log_message("Application Started")
add_student("Rohit", 10)
add_teacher("Mr Pratish", "Chemistry")
log_message("Application Closed")


"""
if the folders are not in the same location you can use __all__ = [<file name>]
{This is a simple Absolute import Example}
"""