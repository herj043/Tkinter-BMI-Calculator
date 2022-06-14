import tkinter as tk

class smallText:
  def __init__(self, root, txt = "NONE", r = 0, c = 0):
    self.window = tk.Label(root, text=txt)
    self.column_span = 1
    self.row = r
    self.column = c

  def create_win(self):
    self.window.grid(row=self.row, column=self.column, columnspan = self.column_span)


# Variable
bmi_win = tk.Tk()
bmi_win.title("BMI Calculator")

text = smallText(bmi_win, """Welcome To BMI Calculator.
Enter your weight and height below.""", 0, 0)
text.column_span = 3
text.create_win()

frame = smallText(bmi_win, "- - - - - - - - - - - - - - - - -"\
+ " - - - - - - - ", 1, 0)
frame.column_span = 5
frame.create_win()

feet = smallText(bmi_win, "ft", 2, 0)
feet.create_win()

inch = smallText(bmi_win, "in", 3, 0)
inch.create_win()

results = tk.Button(bmi_win, text="Get Results")
results.grid(row=4,column=0, columnspan=3)



bmi_win.mainloop()