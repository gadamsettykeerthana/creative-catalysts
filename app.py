import datetime
import random

# This is a simplified example and needs a lot more development
# For real-world implementation, you'd need a more complex data model, 
# a robust UI, and proper integration with BERT or another NLP model.

class Studbud:
    """
    AI Personalized Study Planner
    """

    def _init_(self):
        self.student_info = {}
        self.course_info = {}  # Holds information about each course
        self.study_plan = {}

    def collect_student_info(self):
        """Collects basic student information."""
        print("Let's gather some information to create your personalized plan!")
        self.student_info['name'] = input("What's your name? ")
        self.student_info['goal'] = input("What's your overall academic goal (e.g., get a B average, ace the exam)? ")
        self.student_info['study_style'] = input("What's your preferred study style (e.g., visual, auditory, kinesthetic)? ")
        self.student_info['available_time'] = self.get_available_time()  # Get a dictionary of available times

        # Collect information about courses (using a loop and function call)
        num_courses = int(input("How many courses are you taking? "))
        for i in range(num_courses):
            self.collect_course_info(i + 1)

    def collect_course_info(self, course_number):
        """Collects information about a single course."""
        course_name = input(f"What is the name of course {course_number}? ")
        self.course_info[course_name] = {}  # Initialize an empty dictionary for the course

        self.course_info[course_name]['difficulty'] = input(f"How difficult do you find {course_name} (e.g., easy, medium, hard)? ")
        self.course_info[course_name]['weaknesses'] = input(f"What are your weaknesses in {course_name} (e.g., calculus, grammar)? ")
        self.course_info[course_name]['exam_date'] = input(f"What is the date of the exam for {course_name} (YYYY-MM-DD)? ")

    def get_available_time(self):
        """Asks the user for available study times."""
        available_time = {}
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            time_str = input(f"What time(s) are you available to study on {day}? (e.g., 6-8pm, or 'none') ")
            available_time[day] = time_str.split(",") #allow multiple times, separated by comma
        return available_time

    def analyze_student_data(self):
        """
        Placeholder for BERT-based analysis.  Currently just prints the data.
        In a real application, this would use BERT to analyze student inputs.
        For example, it could use BERT to:
        - Understand the student's goal more deeply.
        - Identify specific areas of weakness based on the student's description.
        - Suggest optimal study techniques based on their learning style.
        """
        print("\nAnalyzing your data (placeholder - using BERT would happen here)...")
        print("Student Info:", self.student_info)
        print("Course Info:", self.course_info)

    def generate_study_plan(self):
        """Generates a basic study plan."""
        print("\nGenerating your personalized study plan...")

        start_date = datetime.date.today()
        for course_name, course_data in self.course_info.items():
            exam_date_str = course_data['exam_date']
            exam_date = datetime.datetime.strptime(exam_date_str, '%Y-%m-%d').date() #convert str to date
            days_until_exam = (exam_date - start_date).days
            print(f"\nStudy Plan for {course_name}: Exam on {exam_date_str} ({days_until_exam} days left)")

            # Simple heuristic:  More difficult courses get more study time.
            if course_data['difficulty'] == 'hard':
                study_hours_per_week = 4
            elif course_data['difficulty'] == 'medium':
                study_hours_per_week = 2
            else:
                study_hours_per_week = 1

            print(f"Recommended study time: {study_hours_per_week} hours per week.")

            # Assign study slots based on available time.
            print("Suggested Schedule:")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            hours_assigned = 0
            for day in days:
                if hours_assigned >= study_hours_per_week:
                    break

                available_times = self.student_info['available_time'][day] #get string from list
                available_times_list = available_times.split(',')
                if available_times_list and available_times_list[0].lower() != 'none':  # Check for 'none' and empty strings
                  for time_slot in available_times_list:
                    time_slot = time_slot.strip() #removes extra spaces from string
                    print(f"  {day}: {time_slot} - Focus on: {course_data['weaknesses']} in {course_name}")
                    hours_assigned += 1 #in a real app, parsing the time slot and using the hours would be important
                    if hours_assigned >= study_hours_per_week:
                        break
        print("\nRemember, this is just a suggested plan. Adjust it to fit your needs!")


    def run(self):
        """Main function to run the study planner."""
        self.collect_student_info()
        self.analyze_student_data()  # Placeholder for BERT analysis
        self.generate_study_plan()



if _name_ == "_main_":
    study_planner = Studbud()
    study_planner.run()
