import tkinter as tk

class smallText:
  def __init__(self, root, txt = "NONE", r = 0, c = 0, column_span = 1):
    self.window = tk.Label(root, text=txt)
    self.window.grid(row=r, column=c, columnspan= column_span)

class insertText:
  def __init__(self, root, wide = 1, r = 0, c = 0, column_span = 1):
    self.window = tk.Entry(root, width= wide)
    self.window.grid(row=r, column=c, columnspan= column_span)

  def __repr__(self):
    return int(self.window.get())

def find_bmi(ft, inch, weight):
  pass


bmi_win = tk.Tk()
bmi_win.title("BMI Calculator")

text = smallText(bmi_win, """Welcome To BMI Calculator.
Enter your weight and height below.""", 0, 0, 5)


frame = smallText(bmi_win, "- - - - - - - - - - - - - - - - -"\
+ " - - - - - - - ", 1, 0, 5)

feet = smallText(bmi_win, "ft", 2, 0)
feet_text_box = insertText(bmi_win, 5, 2, 1)

inch = smallText(bmi_win, "in", 3, 0)
inch_text_box = insertText(bmi_win, 5, 3, 1)

weight = smallText(bmi_win, "weight(lbs)", 2, 4)
weight_text_box = insertText(bmi_win, 10, 3, 4)


results = tk.Button(bmi_win, text="Get Results", command=lambda: find_bmi(feet_text_box, inch_text_box, weight_text_box))
results.grid(row=4,column=0, columnspan=5)



bmi_win.mainloop()