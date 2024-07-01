from tkinter import *

cal = Tk()
cal.title("ماشین حساب")
operator = ""
text_input = StringVar()


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clear_button():
    global operator
    text = operator[:-1]
    operator = text
    text_input.set(text)


def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = sumup

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def fact_func():
    global operator
    result = str(factorial(int(operator)))
    operator = result
    text_input.set(result)

def power():
    global operator
    operator = pow(int(operator), 2)
    text_input.set(operator)

def power3():
    global operator
    operator = pow(int(operator), 3)
    text_input.set(operator)

def sqrt():
    global operator
    if int(operator)>=0:
        temp = str(eval(operator+'**(1/2)'))
        operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def sign_change():
    global operator
    if operator[0]=='-':
        temp = operator[1:]
    else:
        temp = '-'+operator
    operator = temp
    text_input.set(temp)   

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=50, insertwidth=4,
            bg='powder blue', justify='right').grid(columnspan=5)

btn7 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7',
            command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8',
            command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9',
            command=lambda: btnClick(9)).grid(row=1, column=2)
btnClear = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 19, 'bold'), text='C',
            command=btnClearDisplay).grid(row=1, column=3)
clear = Button(cal, text="<", padx=16, pady=18, bd=8, fg="black", font=('arial', 18, 'bold'),
            command=lambda: clear_button()).grid(row=1, column=4)


btn4 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4',
            command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5',
            command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6',
            command=lambda: btnClick(6)).grid(row=2, column=2)
addition = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 19, 'bold'), text='+',
            command=lambda: btnClick('+')).grid(row=2, column=3)
subtraction = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-',
            command=lambda: btnClick('-')).grid(row=2, column=4)


btn1 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1',
            command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2',
            command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3',
            command=lambda: btnClick(3)).grid(row=3, column=2)
multiply = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='*',
            command=lambda: btnClick('*')).grid(row=3, column=3)
division = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/',
            command=lambda: btnClick('/')).grid(row=3, column=4)

signs = Button(cal,padx=16,pady=17,bd=8,fg='black',font=('arial', 18,'bold'), text='\u00B1',
               command=sign_change).grid(row=4, column=0)
btn0 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0',
            command=lambda: btnClick(0)).grid(row=4, column=1)
btn = Button(cal, padx=18, pady=15, bd=8, fg='black', font=('arial', 22, 'bold'), text='.',
            command=lambda: btnClick('.')).grid(row=4, column=2)
l_bracket = Button(cal, padx=18, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='(',
            command=lambda: btnClick('(')).grid(row=4, column=3)
r_bracket = Button(cal, padx=16, pady=14, bd=8, fg='black', font=('arial', 22, 'bold'), text=')',
            command=lambda: btnClick(')')).grid(row=4, column=4)


second_power = Button(cal,padx=16,pady=17,bd=8,fg='black',font=('arial', 18,'bold'),
                text='x\u00B2', command=lambda:power()).grid(row=5,column=0)
third_power = Button(cal,padx=16,pady=17,bd=8,fg='black',font=('arial', 18,'bold'),
                text='x\u00B3', command=lambda:power3()).grid(row=5,column=1)
btnfactorial = Button(cal, padx=16, pady=16, bd=8, fg='black',text='x!', font=('arial', 18, 'bold'),
                   command=fact_func).grid(row=5, column=2)
btnsqrt = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 18,'bold'), text='\u00B2\u221A',
                    command=sqrt).grid(row=5, column=3)
btnEquals = Button(cal, padx=16, pady=16, bd=6, fg='black', font=('arial', 20, 'bold'), text='=',
            command=btnEqualsInput).grid(row=5, column=4)

cal.mainloop()
