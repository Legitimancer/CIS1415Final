"""
Program: FinalProject_DChilds.py
Author: Dan Childs
Program opens a GUI based meal planner. A lunch and dinner option
for each day of the week is displayed. Under each meal is a drop
down menu allowing the user to randomize the displayed meal, enter
a custom meal title, or leave the label blank to allow for eating
out. Along the bottom are buttons allowing the user to randomize
every displayed meal or add a new meal to the master list.
"""


import random
import tkinter
from breezypythongui import *
from tkinter import *


class MenuGenerator(EasyFrame):
    """Displays a randomized weekly meal plan with drop down options."""

    def __init__(self):
        """Sets up window and widgets."""
        EasyFrame.__init__(self, title = "Weekly Meal Plan")

        #Monday day label, dish labels, and dish options
        #Menu bars were not covered in class
        monPanel = self.addPanel(row = 0, column = 0)
        mondayLabel = monPanel.addLabel(text = "Monday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        monLunchLabel = monPanel.addLabel(text = "Lunch",
                                          row = 1, column = 0,
                                          background = "gray92")
        monLBar = monPanel.addMenuBar(row = 2, column = 0)
        mondayLunch = monLBar.addMenu(text = "Options")
        mondayLunch.addMenuItem("Randomize",
                                command =lambda : self.randomize(monLunchLabel))
        mondayLunch.addMenuItem("Customize",
                                command =lambda : self.customize(monLunchLabel))
        mondayLunch.addMenuItem("Blank",
                                command =lambda : self.blank(monLunchLabel))
        monDinnerLabel = monPanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        monDBar = monPanel.addMenuBar(row = 4, column = 0)
        mondayDinner = monDBar.addMenu(text = "Options")
        mondayDinner.addMenuItem("Randomize",
                                 command =lambda : self.randomize(monDinnerLabel))
        mondayDinner.addMenuItem("Customize",
                                 command =lambda : self.customize(monDinnerLabel))
        mondayDinner.addMenuItem("Blank",
                                 command =lambda : self.blank(monDinnerLabel))

        #Tuesday
        tuePanel = self.addPanel(row = 0, column = 1, background = "grey")
        tuesdayLabel = tuePanel.addLabel(text = "Tuesday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        tueLunchLabel = tuePanel.addLabel(text = "Lunch",
                                               row = 1, column = 0,
                                           background = "gray92")
        tueLBar = tuePanel.addMenuBar(row = 2, column = 0)
        tuesdayLunch = tueLBar.addMenu(text = "Options")
        tuesdayLunch.addMenuItem("Randomize",
                                 command =lambda : self.randomize(tueLunchLabel))
        tuesdayLunch.addMenuItem("Customize",
                                 command =lambda : self.customize(tueLunchLabel))
        tuesdayLunch.addMenuItem("Blank",
                                 command =lambda : self.blank(tueLunchLabel))
        tueDinnerLabel = tuePanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        tueDBar = tuePanel.addMenuBar(row = 4, column = 0)
        tuesdayDinner = tueDBar.addMenu(text = "Options")
        tuesdayDinner.addMenuItem("Randomize",
                                  command =lambda : self.randomize(tueDinnerLabel))
        tuesdayDinner.addMenuItem("Customize",
                                  command =lambda : self.customize(tueDinnerLabel))
        tuesdayDinner.addMenuItem("Blank",
                                  command =lambda : self.blank(tueDinnerLabel))

        #Wednesday
        wedPanel = self.addPanel(row = 0, column = 2)
        wednesdayLabel = wedPanel.addLabel(text = "Wednesday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        wedLunchLabel = wedPanel.addLabel(text = "Lunch",
                                               row = 1, column = 0,
                                           background = "gray92")
        wedLBar = wedPanel.addMenuBar(row = 2, column = 0)
        wednesdayLunch = wedLBar.addMenu(text = "Options")
        wednesdayLunch.addMenuItem("Randomize",
                                   command =lambda : self.randomize(wedLunchLabel))
        wednesdayLunch.addMenuItem("Customize",
                                   command =lambda : self.customize(wedLunchLabel))
        wednesdayLunch.addMenuItem("Blank",
                                   command =lambda : self.blank(wedLunchLabel))
        wedDinnerLabel = wedPanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        wedDBar = wedPanel.addMenuBar(row = 4, column = 0)
        wednesdayDinner = wedDBar.addMenu(text = "Options")
        wednesdayDinner.addMenuItem("Randomize",
                                    command =lambda : self.randomize(wedDinnerLabel))
        wednesdayDinner.addMenuItem("Customize",
                                    command =lambda : self.customize(wedDinnerLabel))
        wednesdayDinner.addMenuItem("Blank",
                                    command =lambda : self.blank(wedDinnerLabel))

        #Thursday
        thuPanel = self.addPanel(row = 0, column = 3, background = "grey")
        thursdayLabel = thuPanel.addLabel(text = "Thursday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        thuLunchLabel = thuPanel.addLabel(text = "Lunch",
                                               row = 1, column = 0,
                                           background = "gray92")
        thuLBar = thuPanel.addMenuBar(row = 2, column = 0)
        thursdayLunch = thuLBar.addMenu(text = "Options")
        thursdayLunch.addMenuItem("Randomize",
                                  command =lambda : self.randomize(thuLunchLabel))
        thursdayLunch.addMenuItem("Customize",
                                  command =lambda : self.customize(thuLunchLabel))
        thursdayLunch.addMenuItem("Blank",
                                  command =lambda : self.blank(thuLunchLabel))
        thuDinnerLabel = thuPanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        thuDBar = thuPanel.addMenuBar(row = 4, column = 0)
        thursdayDinner = thuDBar.addMenu(text = "Options")
        thursdayDinner.addMenuItem("Randomize",
                                   command =lambda : self.randomize(thuDinnerLabel))
        thursdayDinner.addMenuItem("Customize",
                                   command =lambda : self.customize(thuDinnerLabel))
        thursdayDinner.addMenuItem("Blank",
                                   command =lambda : self.blank(thuDinnerLabel))

        #Friday
        friPanel = self.addPanel(row = 0, column = 4)
        fridayLabel = friPanel.addLabel(text = "Friday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        friLunchLabel = friPanel.addLabel(text = "Lunch",
                                               row = 1, column = 0,
                                           background = "gray92")
        friLBar = friPanel.addMenuBar(row = 2, column = 0)
        fridayLunch = friLBar.addMenu(text = "Options")
        fridayLunch.addMenuItem("Randomize",
                                command =lambda : self.randomize(friLunchLabel))
        fridayLunch.addMenuItem("Customize",
                                command =lambda : self.customize(friLunchLabel))
        fridayLunch.addMenuItem("Blank",
                                command =lambda : self.blank(friLunchLabel))
        friDinnerLabel = friPanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        friDBar = friPanel.addMenuBar(row = 4, column = 0)
        fridayDinner = friDBar.addMenu(text = "Options")
        fridayDinner.addMenuItem("Randomize",
                                 command =lambda : self.randomize(friDinnerLabel))
        fridayDinner.addMenuItem("Customize",
                                 command =lambda : self.customize(friDinnerLabel))
        fridayDinner.addMenuItem("Blank",
                                 command =lambda : self.blank(friDinnerLabel))

        #Saturday
        satPanel = self.addPanel(row = 0, column = 5, background = "gray")
        saturdayLabel = satPanel.addLabel(text = "Saturday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        satLunchLabel = satPanel.addLabel(text = "Lunch",
                                               row = 1, column = 0,
                                           background = "gray92")
        satLBar = satPanel.addMenuBar(row = 2, column = 0)
        saturdayLunch = satLBar.addMenu(text = "Options")
        saturdayLunch.addMenuItem("Randomize",
                                  command =lambda : self.randomize(satLunchLabel))
        saturdayLunch.addMenuItem("Customize",
                                  command =lambda : self.customize(satLunchLabel))
        saturdayLunch.addMenuItem("Blank",
                                  command =lambda : self.blank(satLunchLabel))
        satDinnerLabel = satPanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        satDBar = satPanel.addMenuBar(row = 4, column = 0)
        saturdayDinner = satDBar.addMenu(text = "Options")
        saturdayDinner.addMenuItem("Randomize",
                                   command =lambda : self.randomize(satDinnerLabel))
        saturdayDinner.addMenuItem("Customize",
                                   command =lambda : self.customize(satDinnerLabel))
        saturdayDinner.addMenuItem("Blank",
                                   command =lambda : self.blank(satDinnerLabel))

        #Sunday
        sunPanel = self.addPanel(row = 0, column = 6)
        sundayLabel = sunPanel.addLabel(text = "Sunday",
                                             row = 0, column = 0,
                                        background = "seashell3")
        sunLunchLabel = sunPanel.addLabel(text = "Lunch",
                                               row = 1, column = 0,
                                           background = "gray92")
        sunLBar = sunPanel.addMenuBar(row = 2, column = 0)
        sundayLunch = sunLBar.addMenu(text = "Options")
        sundayLunch.addMenuItem("Randomize",
                                command =lambda : self.randomize(sunLunchLabel))
        sundayLunch.addMenuItem("Customize",
                                command =lambda : self.customize(sunLunchLabel))
        sundayLunch.addMenuItem("Blank",
                                command =lambda : self.blank(sunLunchLabel))
        sunDinnerLabel = sunPanel.addLabel(text = "Dinner", row = 3, column = 0,
                                           background = "gray92")
        sunDBar = sunPanel.addMenuBar(row = 4, column = 0)
        sundayDinner = sunDBar.addMenu(text = "Options")
        sundayDinner.addMenuItem("Randomize",
                                 command =lambda : self.randomize(sunDinnerLabel))
        sundayDinner.addMenuItem("Customize",
                                 command =lambda : self.customize(sunDinnerLabel))
        sundayDinner.addMenuItem("Blank",
                                 command =lambda : self.blank(sunDinnerLabel))

        #Randomizes meals on program launch
        MEALS = (monLunchLabel, monDinnerLabel ,tueLunchLabel, tueDinnerLabel,
                 wedLunchLabel, wedDinnerLabel, thuLunchLabel, thuDinnerLabel,
                 friLunchLabel, friDinnerLabel, satLunchLabel, satDinnerLabel,
                 sunLunchLabel, sunDinnerLabel)
        for label in MEALS:
            self.randomize(label)

        #Randomize week, Finalize week, and New Dish buttons
        buttonPanel = self.addPanel(row = 1, column = 0, background = "green", columnspan = 7)
        buttonPanel.addButton(text = "Randomize Week", row = 0, column = 0, command =lambda : self.randomizeWeek(MEALS))
        buttonPanel.addButton(text = "Finalize Week", row = 0, column = 1, command = self.finalizeWeek)
        buttonPanel.addButton(text = "Add New Dish", row = 0, column = 2, command = self.newDish)

    def randomize(self, widget):
        """Randomizes displayed dish name"""
        f = open("dishes.txt", 'r')
        self.dishes = []        
        for line in f:
            self.dishes.append(line)
        f.close()
        randomLabel = random.choice(self.dishes)        
        widget["text"] = randomLabel.strip()

    def customize(self, widget):
        """Allows user to choose a specific dish"""
        customDish = self.prompterBox(title = "Custom Dish", promptString = "Input custom dish:")
        widget["text"] = customDish

    def blank(self, widget):
        """Leaves the displayed dish name blank."""
        widget["text"] = '     '

    def randomizeWeek(self, MEALS):
        """Randomizes every displayed dish name."""
        for label in MEALS:
            self.randomize(label)

    def finalizeWeek(self):
        """Returns a plaintext version of the weekly meal plan."""
        pass

    def newDish(self):
        """Opens prompter box which adds the provided dish name to the dish list."""
        newDish = self.prompterBox(title = "New Dish", promptString = "Input new dish:")
        #Append mode was not heavily explored in class. Was very excited to discover this,
        #eliminated several lines of code!
        f = open("dishes.txt", 'a')
        f.write(newDish + '\n')
        f.close()

        
def main():
    """Instantiate and pop up window."""
    MenuGenerator().mainloop()
        
if __name__ == "__main__":
    main()
