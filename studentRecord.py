import re
import sys
def input2(text : str = "", re_pattern : str = None, err_msg : str = ""):
    if type(re_pattern) != str:
        return input(text)
    temp = input(text)
    while re.match(re_pattern, temp) == None:
        sys.stderr.write(err_msg)
        temp = input(text)
    return temp
class StudentRecord(object):
    GRADE_LOWER_BOUND = 1
    GRADE_UPPER_BOUND = 12
    @classmethod
    def create(cls):
        promptFormat = "Enter the student's %s: "
        name = input2(promptFormat%"name", "^[A-z ][A-z\- ]*$","Invalid Input, (hint) input must: start with an alphabet; only contain [alphabet, space, hyphen]\n")
        gradeLevel = None
        def gradeLevelIter():
            nonlocal gradeLevel
            gradeLevel = int(input2(promptFormat%"grade level", "^\d+$",f"Invalid Input, (hint) input must: only contain digit characters, and be within the range of {StudentRecord.GRADE_LOWER_BOUND} to {StudentRecord.GRADE_UPPER_BOUND}\n"))
            return not (gradeLevel < StudentRecord.GRADE_LOWER_BOUND or gradeLevel > StudentRecord.GRADE_UPPER_BOUND)
        try:
            for _ in iter(gradeLevelIter, True):
                sys.stderr.write(f"Invalid Grade Level, (hint) input must be within the range of {StudentRecord.GRADE_LOWER_BOUND} to {StudentRecord.GRADE_UPPER_BOUND}\n")
        except StopIteration:
            pass
        section = input2(promptFormat%"section", "^[A-z][A-z\- ]*$", "Invalid Input, (hint) input must: start with an alphabet, only contain [alphabet, space, hyphen]\n")
        print()
        grades = [
            float(input2(promptFormat%f"{i} quarter grade", "^(\d+\.?\d*|\.\d+)$","Invalid Input, (hint) input must be a floating-point or whole number\n")) for i in ("first", "second", "third", "fourth")
            ]
        print()
        return cls(
            name = name.strip(" "),
            gradeLevel = gradeLevel,
            section = section,
            grades = grades
            )
    def __init__(self, /, name : str , gradeLevel : int, section : str, grades : [float]):
        if len(grades) != 4:
            raise Exception("grades must contain 4 items")
        for i in grades:
            if type(i) != float:
                raise Exception("grades must contain floating numbers only")
        super().__init__()
        self.name = name
        self.gradeLevel = gradeLevel
        self.section = section
        self.grades = grades
    def viewInfo(self) -> None:
        print("Student Name: %s"%self.name)
        print("Grade and Section: %d-%s"%(self.gradeLevel, self.section))
        print()
        print("Grades:\n\t%s"%("\n\t".join([f'{i} Quarter: {format(j,".3f")[:-1]}' for i,j in zip(("First", "Second", "Third", "Fourth"), self.grades)])))
    def __iter__(self):
        return iter((
            ("name" , self.name),
            ("grade_level" ,self.gradeLevel),
            ("section" ,self.section),
            ("grades", dict(zip(("q1","q2","q3","q4"),self.grades)))
            ))
def main():
    record = StudentRecord.create()
    record.viewInfo()
    return 0
if __name__ == "__main__":
    main()
