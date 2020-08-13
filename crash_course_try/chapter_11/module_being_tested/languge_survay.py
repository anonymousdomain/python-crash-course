from python.crash_course_try.chapter_11.module_being_tested.survay import AnonymousSurvay
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
survay=AnonymousSurvay(question)
"""show question"""
survay.show_questions()
while True:
    res=input("languge\n")
    if res=='q':
        break
    survay.stor_responses(res)
"""show responses"""
survay.show_responses()