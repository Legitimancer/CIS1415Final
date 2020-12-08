import random
from breezypythongui import *


class MenuGenerator(EasyFrame):
    """Displays a randomized weekly meal plan with drop down options."""

    def __init__(self):
        """Sets up window and widgets."""
        #Days of the Week
        EasyFrame.__init__(self, title = "Weekly Meal Plan")

        daysPanel = self.addPanel(row = 0, column = 0,
                                  background = "gray", columnspan = 7)
        self.mondayLabel = daysPanel.addLabel(text = "Monday",
                                         row = 0, column = 0)
        self.tuesdayLabel = daysPanel.addLabel(text = "Tuesday",
                                         row = 0, column = 1)
        self.wednesdayLabel = daysPanel.addLabel(text = "Wednesday",
                                         row = 0, column = 2)
        self.thursdayLabel = daysPanel.addLabel(text = "Thursday",
                                         row = 0, column = 3)
        self.fridayLabel = daysPanel.addLabel(text = "Friday",
                                         row = 0, column = 4)
        self.saturdayLabel = daysPanel.addLabel(text = "Saturday",
                                         row = 0, column = 5)
        self.sundayLabel = daysPanel.addLabel(text = "Sunday",
                                         row = 0, column = 6)
        
        #Daily Lunch with dropdown menu
        lunchPanel = self.addPanel(row = 1, column = 0, background = "navy", columnspan = 7)

        monBar = lunchPanel.addMenuBar(row = 0, column = 0, columnspan = 1)
        mondayLunch = monBar.addMenu(text = "Lunch")
        mondayLunch.addMenuItem("Randomize", command = self.randomize)
        mondayLunch.addMenuItem("Customize", command = self.customize)
        mondayLunch.addMenuItem("Blank", command = self.blank)

        tuesBar = lunchPanel.addMenuBar(row = 0, column = 1, columnspan = 1)
        tuesdayLunch = tuesBar.addMenu(text = "Lunch")
        tuesdayLunch.addMenuItem("Randomize", command = self.randomize)
        tuesdayLunch.addMenuItem("Customize", command = self.customize)
        tuesdayLunch.addMenuItem("Blank", command = self.blank)

        wedBar = lunchPanel.addMenuBar(row = 0, column = 2, columnspan = 1)
        wednesdayLunch = wedBar.addMenu(text = "Lunch")
        wednesdayLunch.addMenuItem("Randomize", command = self.randomize)
        wednesdayLunch.addMenuItem("Customize", command = self.customize)
        wednesdayLunch.addMenuItem("Blank", command = self.blank)

        thursBar = lunchPanel.addMenuBar(row = 0, column = 3, columnspan = 1)
        thursdayLunch = thursBar.addMenu(text = "Lunch")
        thursdayLunch.addMenuItem("Randomize", command = self.randomize)
        thursdayLunch.addMenuItem("Customize", command = self.customize)
        thursdayLunch.addMenuItem("Blank", command = self.blank)

        friBar = lunchPanel.addMenuBar(row = 0, column = 4, columnspan = 1)
        fridayLunch = friBar.addMenu(text = "Lunch")
        fridayLunch.addMenuItem("Randomize", command = self.randomize)
        fridayLunch.addMenuItem("Customize", command = self.customize)
        fridayLunch.addMenuItem("Blank", command = self.blank)

        satBar = lunchPanel.addMenuBar(row = 0, column = 5, columnspan = 1)
        saturdayLunch = satBar.addMenu(text = "Lunch")
        saturdayLunch.addMenuItem("Randomize", command = self.randomize)
        saturdayLunch.addMenuItem("Customize", command = self.customize)
        saturdayLunch.addMenuItem("Blank", command = self.blank)
        
        sunBar = lunchPanel.addMenuBar(row = 0, column = 6, columnspan = 1)
        sundayLunch = sunBar.addMenu(text = "Lunch")
        sundayLunch.addMenuItem("Randomize", command = self.randomize)
        sundayLunch.addMenuItem("Customize", command = self.customize)
        sundayLunch.addMenuItem("Blank", command = self.blank)

        #Daily dinner with dropdown menu
        dinnerPanel = self.addPanel(row = 2, column = 0, background = "red", columnspan = 7)
                    
        monDBar = dinnerPanel.addMenuBar(row = 0, column = 0)
        mondayDinner = monDBar.addMenu(text = "Dinner")
        mondayDinner.addMenuItem("Randomize", command = self.randomize)
        mondayDinner.addMenuItem("Customize", command = self.customize)
        mondayDinner.addMenuItem("Blank", command = self.blank)
        
        tuesDBar = dinnerPanel.addMenuBar(row = 0, column = 1)
        tuesdayDinner = tuesDBar.addMenu(text = "Dinner")
        tuesdayDinner.addMenuItem("Randomize", command = self.randomize)
        tuesdayDinner.addMenuItem("Customize", command = self.customize)
        tuesdayDinner.addMenuItem("Blank", command = self.blank)

        wedDBar = dinnerPanel.addMenuBar(row = 0, column = 2)
        wednesdayDinner = wedDBar.addMenu(text = "Dinner")
        wednesdayDinner.addMenuItem("Randomize", command = self.randomize)
        wednesdayDinner.addMenuItem("Customize", command = self.customize)
        wednesdayDinner.addMenuItem("Blank", command = self.blank)
        
        thuDBar = dinnerPanel.addMenuBar(row = 0, column = 3)
        thursdayDinner = thuDBar.addMenu(text = "Dinner")
        thursdayDinner.addMenuItem("Randomize", command = self.randomize)
        thursdayDinner.addMenuItem("Customize", command = self.customize)
        thursdayDinner.addMenuItem("Blank", command = self.blank)
        
        friDBar = dinnerPanel.addMenuBar(row = 0, column = 4)
        fridayDinner = friDBar.addMenu(text = "Dinner")
        fridayDinner.addMenuItem("Randomize", command = self.randomize)
        fridayDinner.addMenuItem("Customize", command = self.customize)
        fridayDinner.addMenuItem("Blank", command = self.blank)

        satDBar = dinnerPanel.addMenuBar(row = 0, column = 5)
        saturdayDinner = satDBar.addMenu(text = "Dinner")
        saturdayDinner.addMenuItem("Randomize", command = self.randomize)
        saturdayDinner.addMenuItem("Customize", command = self.customize)
        saturdayDinner.addMenuItem("Blank", command = self.blank)

        sunDBar = dinnerPanel.addMenuBar(row = 0, column = 6)
        sundayDinner = sunDBar.addMenu(text = "Dinner")
        sundayDinner.addMenuItem("Randomize", command = self.randomize)
        sundayDinner.addMenuItem("Customize", command = self.customize)
        sundayDinner.addMenuItem("Blank", command = self.blank)
        
        #Buttons
        buttonPanel = self.addPanel(row = 3, column = 0, background = "green", columnspan = 7)
        buttonPanel.addButton(text = "Randomize Week", row = 0, column = 0, command = self.randomizeWeek)
        buttonPanel.addButton(text = "Finalize Week", row = 0, column = 1, command = self.finalizeWeek)
        buttonPanel.addButton(text = "Add New Dish", row = 0, column = 2, command = self.newDish)



    def randomize(self):
        """Randomizes displayed dish name"""

    def customize(self):
        """Allows user to choose a specific dish"""
        pass

    def blank(self):
        """Leaves the displayed dish name blank."""
        pass

    def randomizeWeek(self):
        """Randomizes every displayed dish name."""
        pass

    def finalizeWeek(self):
        """Opens a ."""
        pass

    def newDish(self):
        """Opens prompter box which adds the provided dish name to the dish list."""
        newDish = self.prompterBox(title = "New Dish", promptString = "Input new dish:")
        f = open("dishes.txt", 'r')


        self.dishes = []
        
        for line in f:
            self.dishes.append(line)

        f.close()

        self.dishes.append(newDish)

        f = open("dishes.txt", 'w')

        for dish in self.dishes:
            f.write(dish + '\n')
        f.close()



        
def main():
    """Instantiate and pop up window."""
    MenuGenerator().mainloop()
        
if __name__ == "__main__":
    main()
