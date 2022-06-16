import tkinter as tk

### Classes ###

class smallText:
  def __init__(self, root, txt = "NONE", r = 0, c = 0, column_span = 1):
    self.window = tk.Label(root, text=txt)
    self.window.grid(row=r, column=c, columnspan= column_span)

class insertText:
  def __init__(self, root, wide = 1, r = 0, c = 0, column_span = 1):
    self.window = tk.Entry(root, width= wide)
    self.window.grid(row=r, column=c, columnspan= column_span)

  def __repr__(self):
    return self.window.get()


### Functions ###

# Calculates the numbers to find your BMI
def find_bmi(ft, inch, lbs):
  # Can't use the objects, they must become str then int
  try: 
    convert_to_str = [str(ft), str(inch), str(lbs)]
    convert_to_int = [int(convert_to_str[0]),int(convert_to_str[1]), int(convert_to_str[2])]
    
    feet, inch, weight = convert_to_int
    height = feet * 12 + inch

    bmi = round((703 * weight) / (height ** 2), 1)
    create_bmi_window(bmi)
  except:
    print("ERROR: ALL INFORMATION MUST BE FILLED AND HOLD ONLY NUMBERS")

# Creates a window and color codes the results after find_bmi
def create_bmi_window(bmi):
  if bmi < 18.5:
    window_color = "#9999ff"
    weight_class = "UnderWeight"
  elif 18.5 <= bmi < 25:
    window_color = "#99ff99"
    weight_class = "Normal"
  else:
    window_color = "#ff9999"
    weight_class = "OverWeight"
    
  results_win = tk.Tk()
  results_win.config(background=window_color)

  weight_class_text = tk.Label(results_win, text="Weight Class: " + weight_class)
  weight_class_text.config(background=window_color)
  weight_class_text.pack()
  
  bmi_text = tk.Label(results_win, text="BMI Results: " + str(bmi))
  bmi_text.config(background=window_color)
  bmi_text.pack()

  close_button = tk.Button(results_win, text="close window", command= results_win.destroy)
  close_button.config(background=window_color)
  close_button.pack()

  results_win.mainloop()

  
### Running Program ###
  
bmi_win = tk.Tk()
bmi_win.title("BMI Calculator")

text = smallText(bmi_win, """Welcome To BMI Calculator.
Enter your weight and height below.
(fill and use only numbers)""", 0, 0, 5)

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