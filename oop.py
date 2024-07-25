# Define class
class Calculator:
    def __init__(self,str=''):
        self.screen=str
        self.pre_ans=None
        self.ans=None
        self.ans_cpy=None
    def __repr__(self):
        return "This is a calculator"
    def do_math(self):
        str=input("Type this, I will help u: ")
        if "+" in str:
            a=str.split("+")
            self.screen=str
            self.ans=int(a[0])+int(a[1])
            # Pre_answer
            self.pre_ans=self.ans_cpy
            self.ans_cpy=self.ans
        # For other operations
        """
        elif "-" in str:
            a=str.split("-")
            print(int(a[0])-int(a[1]))  
        elif "x" in str:
            a=str.split("x")
            print(int(a[0])*int(a[1])) 
        elif ":" in str:
            a=str.split(":")
            print(int(a[0])/int(a[1])) 
        else:
            print("Syntax Error")
        """
    def print_ans(self):
        print(self.screen)
        print(f"   {self.ans}")
    
    def print_Pre_ans(self):
        print(f"Pre_ans: {self.pre_ans}")
            
#Test class
casio=Calculator()
casio.do_math()
casio.print_ans()
casio.do_math()
casio.print_ans()
casio.do_math()
casio.print_ans()
casio.print_Pre_ans()
        