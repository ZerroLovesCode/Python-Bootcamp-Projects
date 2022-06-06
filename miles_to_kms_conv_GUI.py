import tkinter

window = tkinter.Tk()

window.title('M to K')
# window.minsize(500, 500)
window.config(padx=20, pady=20)

def conv_to_kms():
    miles = float(m_inp.get())
    km = miles*1.609
    k_res.config(text=str(km))


m_inp = tkinter.Entry(width=7)
m_inp.grid(column=1, row=0)

m_label = tkinter.Label(text="Miles")
m_label.grid(column=2, row=0)

equ_label = tkinter.Label(text="is equal to")
equ_label.grid(column=0, row=1)

k_label = tkinter.Label(text="Kilometers")
k_label.grid(column=2, row=1)

k_res = tkinter.Label(text="0")
k_res.grid(column=1, row=1)

calc_button = tkinter.Button(text="Calculate", command=conv_to_kms)
calc_button.grid(column=1, row=2)

window.mainloop()
