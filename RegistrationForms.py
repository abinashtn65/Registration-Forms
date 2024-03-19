import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1, n2,n3, n4,n5, n6):  
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())
    num4 = (n4.get())
    num5 = (n5.get())
    num6 = (n6.get())
    print(num1+" "+num2+" "+num3+" "+num4+" "+num5+" "+num6)
    label_result.config(text="Inserte: %s" % num1)
    return
   
root = tk.Tk()  
root.geometry('400x250')  
  
root.title('RegistrationForm')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
number5 = tk.StringVar()
number6 = tk.StringVar()


#Label To display Emp_ID,Emp_Name,EmailID ,Password,Emp_City,Emp_state.

n=tk.Label(root,text="***Employee registration Form***",font=("Arial", 12), fg = 'White' , bg='Green').grid(row=1, column=2)

labelNum1 = tk.Label(root, text="Emp_ID").grid(row=2, column=0)  
  
labelNum2 = tk.Label(root, text="Emp_Name").grid(row=3, column=0)

labelNum3 = tk.Label(root, text="EmailID").grid(row=4, column=0)
labelNum4 = tk.Label(root, text="Password").grid(row=5, column=0)
labelNum5 = tk.Label(root, text="Emp_City").grid(row=6, column=0)
labelNum6 = tk.Label(root, text="Emp_state").grid(row=7, column=0)
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=10, column=2)  
#Entry to Create Text field 
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=2, column=2)  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=3, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=4, column=2)
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=5, column=2)
entryNum5 = tk.Entry(root, textvariable=number5).grid(row=6, column=2)
entryNum6 = tk.Entry(root, textvariable=number6).grid(row=7, column=2) 
  
call_result = partial(call_result, labelResult, number1, number2,number3, number4,number5, number6)  
  
buttonCal = tk.Button(root, text="Submit", command=call_result).grid(row=8, column=0)  
  
root.mainloop()  
