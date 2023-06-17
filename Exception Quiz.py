def quiz_on_exception():
    quiz_data = [
        {
            "question": "Which keyword is used for exception handling?",
            "options": ['a) raise', 'b) try', 'c) handle', 'd) exception'],
            "answer": 'b'
        },
        {
            "question": "What is the purpose of the 'finally' clause in Python exception handling?",
            "options": ['a) It executes no matter what', 'b) It is executed if an exception occurs', 'c) It is executed if no exception', 'd) None of the above'],
            "answer": 'a'
        },
        {
            "question": "Which built-in exception is raised when a function or operation is not implemented yet?",
            "options": ['a) NotImplementedError', 'b) ArithmeticError', 'c) BufferError', 'd) AssertionError'],
            "answer": 'a'
        },
        {
            "question": "Which of the following exceptions is NOT raised by Python built-in operations?",
            "options": ['a) IOError', 'b) FileNotFoundError', 'c) KeyNotFoundError', 'd) ZeroDivisionError'],
            "answer": 'c'
        },
        {
            "question": "What exception is raised when a local or global name is not found?",
            "options": ['a) AttributeError', 'b) KeyError', 'c) ImportError', 'd) NameError'],
            "answer": 'd'
        },
        {
            "question": "What exception is raised when the parser encounters a syntax error?",
            "options": ['a) AttributeError', 'b) SyntaxError', 'c) IndentationError', 'd) ValueError'],
            "answer": 'b'
        },
        {
            "question": "What exception is raised when there is incorrect indentation?",
            "options": ['a) IndentationError', 'b) ValueError', 'c) SyntaxError', 'd) TypeError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when an operation or function receives an argument of the right type but an inappropriate value?",
            "options": ['a) ValueError', 'b) TypeError', 'c) IndexError', 'd) KeyError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when a sequence subscript is out of range?",
            "options": ['a) KeyError', 'b) ValueError', 'c) TypeError', 'd) IndexError'],
            "answer": 'd'
        },
        {
            "question": "What exception is raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported?",
            "options": ['a) ImportError', 'b) ValueError', 'c) FileNotFoundError', 'd) AttributeError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when an operation runs out of memory?",
            "options": ['a) MemoryError', 'b) BufferError', 'c) OverflowError', 'd) ArithmeticError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when the result of an arithmetic operation is too large to be expressed by the normal number format?",
            "options": ['a) OverflowError', 'b) MemoryError', 'c) IndexError', 'd) ArithmeticError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when an attribute reference or assignment fails?",
            "options": ['a) AttributeError', 'b) KeyError', 'c) ImportError', 'd) NameError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when a file or directory is requested but doesn’t exist?",
            "options": ['a) FileNotFoundError', 'b) IOError', 'c) ImportError', 'd) KeyError'],
            "answer": 'a'
        },
        {
            "question": "What exception is raised when a dictionary key is not found?",
            "options": ['a) KeyError', 'b) ValueError', 'c) IndexError', 'd) FileNotFoundError'],
            "answer": 'a'
        },
    ]
    score = 0
    for i in range(len(quiz_data)):
        print(quiz_data[i]["question"])
        for j in quiz_data[i]["options"]:
            print(j)
        opt_list = []
        for k in quiz_data[i]["options"]:
            l = k.split()[0].split(")")[0]
            opt_list.append(l)
        while True:
            user_answer = input("enter the answer: ")
            if user_answer in opt_list:
                if user_answer == quiz_data[i]["answer"]:
                    print("correct")
                    score +=1
                    break
                else:
                    print("incorrect")
                    break
            else:
                print("please provide the correct option to check")
                continue
    print(f"your score is {score}/{len(quiz_data)}")

quiz_on_exception()