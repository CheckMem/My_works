









import tkinter as tk

window = tk.Tk()


label = tk.Label(
    text="Привет, Tkinter!",
    foreground="magenta2",  # Устанавливает белый текст
    background="red3"  # Устанавливает черный фон
)
label.pack()  #без этого не будет выводить
window.mainloop()





# import tkinter as tk
# window = tk.Tk()
# greeting = tk.Label(text="Привет, Tkinter!")
# greeting.pack()
# window.mainloop()