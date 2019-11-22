# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:44:44 2018

@author: R00050477
"""

import numpy as np

cities = ["Cork", "Belfast", "Dublin", "Galway", "Limerick"]

def primaryMenu():

    print("\n\n======================================")
    print("                Menu")
    print("======================================\n\n")
    print("1. Basic Statistics for Total Rainfall (Millimetres)")
    print("2. Basic Statistics for Most Rainfall in a Day (Millimetres)")
    print("3. Basic Statistics for Number of Rain days (0.2mm or More)")
    print("4. Wettest Location")
    print("5. Percentage of Rain Days")
    print("6. Exit")

    while True:
        try:
            selectedFunction = int(input("Please select one of the above options (1-6): "))
        except ValueError:
            print("Must be 1-6")
            selectedFunction = 0

        if (selectedFunction > 0) or (selectedFunction < 6):
            return selectedFunction
            break
        else:
            print("This is not a valid choice")


def secondaryMenu():
    print("\n\n======================================")
    print("                Menu")
    print("======================================\n\n")
    print("1. Cork")
    print("2. Belfast")
    print("3. Dublin")
    print("4. Galway")
    print("5. Limerick")

    while True:
        try:
            selectedCounty = int(input("Please select a location (1-5): "))
        except ValueError:
            print("Must be 1-5")
            selectedCounty = 0

        if (selectedCounty > 0) or (selectedCounty < 6):
            return selectedCounty
            break
        else:
            print("This is not a valid choice")


def convert(selectedOption):

    if selectedOption == 1:
        county = "Cork"
    if selectedOption == 2:
        county = "Belfast"
    if selectedOption == 3:
        county = "Dublin"
    if selectedOption == 4:
        county = "Galway"
    if selectedOption == 4:
        county = "Limerick"

    return county

# ===================================================================================
#               FUNCTION ONE
# ===================================================================================
def totalRainfallFtn(countyString):

    data = np.genfromtxt(countyString + 'Rainfall.txt', dtype=float, delimiter=' ')
    maxTotalRainfall = np.max(data[:, 2])
    averageRainfall = np.average(data[:, 2])
    # ouputs the answers to 2 decimal space
    print("\n\n" + countyString + ": Max Total Rainfall = " + "%.2f" % maxTotalRainfall + "mm")
    print(countyString + ": Average Total Rainfall = " + "%.2f" % averageRainfall + "mm")


# ===================================================================================
#               FUNCTION TWO
# ===================================================================================
def mostRainfallInADayFtn(countyString):

    data = np.genfromtxt(countyString + 'Rainfall.txt', dtype=float, delimiter=' ')
    maxRainfallInADay = np.max(data[:, 3])
    averageMostRainfall = np.average(data[:, 3])
    # outputs the answers to 2 decimal space
    print("\n\n" + countyString + ": Max Rainfall In a Day= " + "%.2f" % maxRainfallInADay + "mm")
    print(countyString + ": Average Total Rainfall In a Day = " + "%.2f" % averageMostRainfall + "mm")


# ===================================================================================
#               FUNCTION THREE
# ===================================================================================
def numberOfRainyDaysFtn(countyString):

    data = np.genfromtxt(countyString + 'Rainfall.txt', dtype=float, delimiter=' ')
    maxNumberofRainyDay = np.max(data[:, 4])
    averageNumberofRainyDay = np.average(data[:, 4])
    # outputs the answers
    print("\n\n" + countyString + ": Max Number of Rain days " + str(maxNumberofRainyDay))
    print(countyString + ":  Average Number of Rain days " + str(averageNumberofRainyDay))


# ===================================================================================
#               FUNCTION FOUR
# ===================================================================================
def wettestLocation():

    wettest = 0
    number = 0

    for i in cities:
        number += 1
        data = np.genfromtxt(i + 'Rainfall.txt', dtype=float, delimiter=' ')
        total = np.sum(data[:, 2])

        print("\n" + str(number) + ". " + i + " " + "%.2f" % total + "mm")

        if total > wettest:
            wettest = total
            city = i

    print("\nThe wettest location in Ireland is " + city + " with a rainfall figure of " + "%.2f" % wettest + "mm")


# ===================================================================================
#               FUNCTION FIVE
# ===================================================================================
def percentages():
    count = 0
    total = 0
    number = 0

    inputValue = int(input("\nPlease enter maximum threshold value for number of rain days: "))

    print("\nThe following are the percentage of rain days less than or equal to " + str(inputValue) + "\n")

    # loops through the files and opens them
    for i in cities:
        number += 1
        fileObj = open(i + 'Rainfall.txt')
        # reads the lines and while true takes the content of that line
        while True:
            lineContent = fileObj.readline()
            if ("" == lineContent):
                "file finished"
                break;

            # splits up the content of the line and stores the value at the fourth index.
            # then converts the string to an int to be checked
            fileValue = lineContent.split(" ")
            currentValueString = fileValue[4]
            currentValueInt = int(currentValueString)
            total += 1
            #compares the input to the current data and keeps count of valid results
            if currentValueInt <= inputValue:
                count += 1

        # calculates the percentage to be printed
        result = count / total * 100

        # prints results
        print(str(number) + ". " + i + " " + "%.2f" % result + "%\n")

def main():

    selectedFunction = 0

    while selectedFunction != 6:

        # ask for function input and validate it
        # =================================================================
        selectedFunction = primaryMenu()
        while selectedFunction not in range(1, 7):
            print("\n\nInvalid option! Select again:")
            selectedFunction = primaryMenu()

        # if choice is 1 2 or 3 ask for county input and validate it
        # =================================================================
        if selectedFunction == 1 or selectedFunction == 2 or selectedFunction == 3:

            option = secondaryMenu()
            while option not in range(1, 6):
                print("\n\nInvalid option! Select again:")
                option = secondaryMenu()

            # convert the selectedOption (number) into county name
            # =================================================================
            countyString = convert(option)
            # now complete the task
            # =================================================================
            if selectedFunction == 1:
                totalRainfallFtn(countyString)
            # =================================================================
            if selectedFunction == 2:
                mostRainfallInADayFtn(countyString)
             # =================================================================
            if selectedFunction == 3:
               numberOfRainyDaysFtn(countyString)
        # =================================================================
        # if choice is 4
        if selectedFunction == 4:
            wettestLocation()
        # =================================================================
        # if choice is 5
        if selectedFunction == 5:
            percentages()
        # =================================================================
        # if choice is 6 then exit program
        if selectedFunction == 6:
            print("\n\nGood bye... ")
            exit()

main()

