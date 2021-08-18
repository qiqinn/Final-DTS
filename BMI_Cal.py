from tkinter import *
from tkinter import messagebox



def calculate_bmi():
    try:
        float(weight_tf.get())
        float(height_tf.get())
    except:
        messagebox.showerror('salah input', 'usia, tinggi dan berat badan harus dalam angka')

    kg = float(weight_tf.get())
    m = float(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('Hasil', f'BMI = {bmi} \nkekurangan berat badan')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('Hasil', f'BMI = {bmi} \nberat badan normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('Hasil', f'BMI = {bmi} \nkelebihan berat badan')
    elif (bmi > 29.9):
        messagebox.showinfo('Hasil', f'BMI = {bmi} \nobesitas') 
    else:
        messagebox.showerror('Hasil', 'error')   

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

ws = Tk()
ws.title('Calculator BMI')
ws.geometry('540x400')
ws.config(bg='#686e70')



frame = Frame(
    ws,
    padx=100, 
    pady=100,
    
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Usia anda:"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=1, column=2, pady=5)


frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

age_lb = Label(
    frame,
    text="Jenis kelamin:"
)
age_lb.grid(row=2, column=1)

male_rb = Radiobutton(
    frame2,
    text = 'Laki laki',
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Perempuan',
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Tinggi badan (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Berat badan (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Hitung',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Keluar',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
