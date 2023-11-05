# calculator class to perform basic mathematical operations

class calculator:
    def __init__(self) -> None:
        print('Welcome to codesoft calculator!...')
        self.temp=0
        iteration=1
        l1=('+','-','*','**','/','//','%')
        
        while True:
            operator=input('choose operator (+,-,/,*,//,**,%) which you wanna perfor for stop operations enter stop :-  ').upper()
           
            if operator=='STOP':
                print('Thanks for visiting our calculator')
                break
            elif operator in l1:                 
                
                
                # Function to handle operations with two operands
                def two_operands():
                    val1 = 0
                    val2 =0 



                    try:
                        val1 = int(input('Enter value 1: '))
                    except:
                        print('integer value has not been entered .')
                    
                    try:
                        val2 = int(input('Enter value 2: '))
                    
                    # Handle non-integer input
                    except :
                        print('integer value has not been entered .')
                    

                   # Perform the selected operation
                    match operator:
                        case '+':
                            self.temp=val1+val2
                            print(f'addition of {val1} and {val2}:-',self.temp)
                        case '-':
                            self.temp=val1-val2
                            print(f'division of {val1} and {val2}:-',self.temp)
                        case '*':
                            self.temp=val1*val2
                            print(f'multiplication of {val1} and {val2}:-',self.temp)
                        case '**':
                            self.temp=val1**val2
                            print(f'multiplication of {val1} and {val2}:-',self.temp)
                        case '/':
                            self.temp=val1/val2
                            print(f'multiplication of {val1} and {val2}:-',self.temp)
                        case '//':
                            self.temp=val1//val2
                            print(f'multiplication of {val1} and {val2}:-',self.temp)
                        case '%':
                            self.temp=val1%val2
                            print(f'multiplication of {val1} and {val2}:-',self.temp) 


            # Function to handle operations with more than two operands
                def _more_than_two_operands():
                    val1=0

                    try:
                        val1=int(input('Enter value:-'))
                    # Handle division by zero error and any others
                    except :
                        print('Enter value in intiger or floating format')
                        _more_than_two_operands()
                    else:
                        # Perform the selected operation
                        match operator:
                            case '+':
                                print(f'addition of {val1} and {self.temp}:-',end=' ')
                                self.temp+=val1
                                print(self.temp)
                            case '-':
                                print(f'division of {self.temp} and {val1} :-',end=' ')
                                self.temp-=val1
                                print(self.temp)
                            case '*':
                                print(f'multiplication of {self.temp} and {val1}:-',end=' ')
                                self.temp*=val1
                                print(self.temp)
                            case '**':
                                print(f'Exponentiation of {self.temp} and {val1}:-',end=' ')
                                self.temp**=val1
                                print(self.temp)
                            case '/':
                                print(f'division of {self.temp} and {val1}:-',end=' ')
                                self.temp/=val1
                                print(self.temp)
                            case '//':
                                print(f'Floor Division of {self.temp} and {val1}:-',end=' ')
                                self.temp//=val1
                                print(self.temp)
                            case '%':
                                print(f'division of {self.temp} and {val1}:-',end=' ')
                                self.temp%=val1
                                print(self.temp)
                if  iteration==1:
                    two_operands()
                else:
                    _more_than_two_operands()
                iteration+=1
                

            else:
                # Handle invalid operator input
                print('Choose currect option')

# Create an instance of the Calculator class
obj=calculator()
