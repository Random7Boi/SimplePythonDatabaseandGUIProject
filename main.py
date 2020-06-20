#region imports and modules

from GUI import *
from Database import *
import operator
import os

#endregion

#region class

class main():

    ''' This function will go through the database table and find the individual
    with the most/least profits, as well as calculate any losses incurred through
    by calculating the differences between sum of expenses and tax to the difference 
    between income and revenue'''
    def findRichest(self):
        
        # list variables that will be assigned the output of plotshow function
        name = []
        email = []
        income = []
        expense = []
        rev = []
        tax = []

        # lists used to make calculations based on info from the tables
        profitLoss = []
        losses = []
        differ = []
        unknownLoss = []

        # integers that store the index values of the values we seek to find names
        cMIndex = 0
        cmIndex = 0
        uMIndex = 0
        umIndex = 0

        # assign outputs from database to first 6 lists
        name, email, income, expense, rev, tax = plotShow()

        # check if lists are empty
        if len(name) == 0:
            return
            
        # else run the rest of this function
        else:

            # create copy lists to be edited while preserving original outputs for financial data lists
            copyIncome = income.copy()
            copyRev = rev.copy()
            copyExp = expense.copy()
            copyTax = tax.copy()

            # calculate profit losses by finding the difference between revenue and income, and print it
            profitLoss = list(map(operator.sub, copyRev, copyIncome))
            print('profit losses are: ' + str(profitLoss))

            # calculate losses by adding expenses and taxes for each row from database, and print results
            losses = list(map(operator.add, copyExp, copyTax))
            print('losses: ' + str(losses))

            # find profits by calculating difference between income and losses, print results
            differ = list(map(operator.sub, copyIncome, losses))
            print('profits are: ' + str(differ))

            # calculate unidentified losses by subtracting profit losses and losses, print results
            unknownLoss = list(map(operator.sub, profitLoss, losses))
            print('unaccounted losses are: ' + str(unknownLoss))

            # create copy of the profits list in a new list
            differ2 = differ.copy()
            # sort the new list from least to greatest
            differ2.sort()
            # create and set two variables to 0, one to store highest profit, other the least
            copyMax = copyMin = 0
            # copyMax is set to the element with the highest profit at the end of the sorted list
            copyMax = differ2[-1]
            # copyMin is set to the element with the lowest profit at the start of the sorted list
            copyMin = differ2[0]
            # clear the copy list for re-use
            differ2.clear()

            # repeat above 6 steps for unidentified losses list
            unknownLoss2 = unknownLoss.copy()
            unknownLoss2.sort()
            copyUM = copyum = 0
            copyUM = unknownLoss2[-1]
            copyum = unknownLoss2[0]
            unknownLoss2.clear()

            #print(copyMin, copyMax, copyUM, copyum)

            # loop through profits list, if an elements is equal to the highest profit value, find it's index and set cMIndex to it
            for Icos in differ:
                if Icos == copyMax:
                    cMIndex = differ.index(Icos)
                
                # same as above, but now for lowest profit value, find it's index value and assign it to cmIndex
                if Icos == copyMin:
                    cmIndex = differ.index(Icos)
            
            # same steps as above two, but for unidentified losses, find the index values and place them in uMindex, umIndex
            for ems in unknownLoss:
                if ems == copyUM:
                    uMIndex = unknownLoss.index(ems)
                
                if ems == copyum:
                    umIndex = unknownLoss.index(ems)

            # print results in terminal
            print('The person with the least profit is ' + name[cmIndex] + ' with contact email being ' + email[cmIndex])
            print('The person with the highest profit is ' + name[cMIndex]+ ' with contact email being ' + email[cMIndex])
            print('The person with the least unaccounted loss is ' + name[umIndex]+ ' with contact email being ' + email[umIndex])
            print('The person with the highest unaccounted loss is ' + name[uMIndex]+ ' with contact email being ' + email[uMIndex])       

    # this function will call the main class when a varaible is assigned this class
    def __init__(self):

        os.system('cls') # clears the terminal from code, use 'clear' on linux/Mac

        # create database so findRichest doesn't give an error
        createDatabase()

        # run findRichest function
        self.findRichest()

        # run the GUI from Ktinker
        root.mainloop()

#endregion

#region init

# call main by variable assignment
A = main()

#endregion



