'''
* Program #6: Mortgage Calculator GUI
* Programmer: Priya Jain
* Due: August 7, 2020
* CS 3A, Summer 2020
* Description: This GUI program will calculate the assessment value and property tax
given the property value.
'''

import tkinter

class PropertyGUI:
    def __init__(self):
      
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create frames
        self.value_frame = tkinter.Frame()
        self.assess_frame = tkinter.Frame()
        self.tax_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the value frame
        self.property_value = tkinter.Label(self.value_frame, text = 'Enter the property value: $')
        self.actual_value_Entry = tkinter.Entry(self.value_frame, width = 10)

        # Pack the value frame widgets
        self.property_value.pack(side = 'left')
        self.actual_value_Entry.pack(side = 'left')

        # Create the widgets for the assess frame
                  
        # Create a blank label for assessment value
        self.assessment_value = tkinter.Label(self.assess_frame, text = 'Assessment Value: ')

        # Pack the assess frame widgets
        self.assessment_value.pack()

        # Create the widgets for the tax frame
                
        # Create a blank label for property tax value
        self.tax_value = tkinter.Label(self.tax_frame, text = 'Property Tax: ')

        # Pack the tax frame widgets
        self.tax_value.pack()

        # Create the two buttons in the bottom frame
        self.but_calc = tkinter.Button(self.bottom_frame, text = "Calculate", command = self.calculate)
        self.but_quit = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
      
        # Pack the widgets in the bottom frame
        self.but_calc.pack(side = 'left')
        self.but_quit.pack(side = 'left')
                
        # Pack the frames
        self.value_frame.pack()
        self.assess_frame.pack()
        self.tax_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def calculate(self):
        # Get the values entered
        actual_value = float(self.actual_value_Entry.get())

        # Calculate assessment
        assess_val = 0.6 * actual_value

        # Update the assessment label
        self.assessment_value['text'] = 'Assessment Value: $' + str(assess_val)

        # Calculate tax
        tax_val = assess_val * 0.0075
        
        # Update the tax label
        self.tax_value['text'] = 'Property Tax: $' + str(tax_val)
            
# Create an instance of PropertyGUI
my_gui = PropertyGUI()