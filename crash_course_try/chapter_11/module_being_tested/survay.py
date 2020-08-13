class AnonymousSurvay:

    """collect anonymous answer to the survay"""
    def __init__(self,questions):
        self.questions=questions
        self.responeses=[]
    def show_questions(self):
        """show the question"""
        print(f"question:{self.questions}")
    def stor_responses(self,new_responses):
        """store new responses"""
        self.responeses.append(new_responses)
    def show_responses(self):
        """show the responses from the anonymous survay"""
        print("survay result")
        for response in self.responeses:
            print(f"respones:{response}")