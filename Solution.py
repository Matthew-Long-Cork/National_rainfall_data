# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 20:44:44 2018

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
            selected_function = int(input("Please select one of the above options (1-6): "))
        except ValueError:
            print("Must be 1-6")
            selected_function = 0

        if (selected_function > 0) or (selected_function < 6):
            return selected_function
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
            selected_county = int(input("Please select a location (1-5): "))
        except ValueError:
            print("Must be 1-5")
            selected_county = 0

        if (selected_county > 0) or (selected_county < 6):
            return selected_county
            break
        else:
            print("This is not a valid choice")


def convert(selected_option):

    if selected_option == 1:
        county = "Cork"
    if selected_option == 2:
        county = "Belfast"
    if selected_option == 3:
        county = "Dublin"
    if selected_option == 4:
        county = "Galway"
    if selected_option == 4:
        county = "Limerick"

    return county

# ===================================================================================
#               FUNCTION ONE
# ===================================================================================
def totalRainfallFtn(county_string):

    data = np.genfromtxt(county_string + 'Rainfall.txt', dtype=float, delimiter=' ')
    max_total_rainfall = np.max(data[:, 2])
    average_rainfall = np.average(data[:, 2])
    # outputs the answers to 2 decimal space
    print("\n\n" + county_string + ": Max total rainfall recorded = " + "%.2f" % max_total_rainfall + "mm")
    print(county_string + ": Average total rainfall recorded = " + "%.2f" % average_rainfall + "mm")


# ===================================================================================
#               FUNCTION TWO
# ===================================================================================
def mostRainfallInADayFtn(county_string):

    data = np.genfromtxt(county_string + 'Rainfall.txt', dtype=float, delimiter=' ')
    max_rainfall_in_a_day = np.max(data[:, 3])
    average_most_rainfall = np.average(data[:, 3])
    # outputs the answers to 2 decimal space
    print("\n\n" + county_string + ": Max rainfall in a day= " + "%.2f" % max_rainfall_in_a_day + "mm")
    print(county_string + ": Average total rainfall in a day = " + "%.2f" % average_most_rainfall + "mm")


# ===================================================================================
#               FUNCTION THREE
# ===================================================================================
def numberOfRainyDaysFtn(county_string):

    data = np.genfromtxt(county_string + 'Rainfall.txt', dtype=float, delimiter=' ')
    max_umber_of_rainy_day = np.max(data[:, 4])
    average_number_of_rainy_day = np.average(data[:, 4])
    # outputs the answers
    print("\n\n" + county_string + ": Max number of rainy days = " + "%.0f" % max_umber_of_rainy_day)
    print(county_string + ": Average number of rainy days = " + "%.2f" % average_number_of_rainy_day)

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

    input_value = int(input("\nPlease enter maximum threshold value for number of rain days: "))

    print("\nThe following are the percentage of rain days less than or equal to " + str(input_value) + "\n")

    # loops through the files and opens them
    for i in cities:
        number += 1
        file_obj = open(i + 'Rainfall.txt')
        # reads the lines and while true takes the content of that line
        while True:
            line_content = file_obj.readline()
            if ("" == line_content):
                "file finished"
                break;

            # splits up the content of the line and stores the value at the fourth index.
            # then converts the string to an int to be checked
            file_value = line_content.split(" ")
            current_value_string = file_value[4]
            current_value_int = int(current_value_string)
            total += 1
            # compares the input to the current data and keeps count of valid results
            if current_value_int <= input_value:
                count += 1

        # calculates the percentage to be printed
        result = count / total * 100

        # prints results
        print(str(number) + ". " + i + " " + "%.2f" % result + "%\n")


def main():

    selected_function = 0

    while selected_function != 6:

        # ask for function input and validate it
        # =================================================================
        selected_function = primaryMenu()
        while selected_function not in range(1, 7):
            print("\n\nInvalid option! Select again:")
            selected_function = primaryMenu()

        # if choice is 1 2 or 3 ask for county input and validate it
        # =================================================================
        if selected_function == 1 or selected_function == 2 or selected_function == 3:

            option = secondaryMenu()
            while option not in range(1, 6):
                print("\n\nInvalid option! Select again:")
                option = secondaryMenu()

            # convert the selectedOption (number) into county name
            # =================================================================
            county_string = convert(option)
            # now complete the task
            # =================================================================
            if selected_function == 1:
                totalRainfallFtn(county_string)
            # =================================================================
            if selected_function == 2:
                mostRainfallInADayFtn(county_string)
            # =================================================================
            if selected_function == 3:
                numberOfRainyDaysFtn(county_string)
        # =================================================================
        # if choice is 4
        if selected_function == 4:
            wettestLocation()
        # =================================================================
        # if choice is 5
        if selected_function == 5:
            percentages()
        # =================================================================
        # if choice is 6 then exit program
        if selected_function == 6:
            print("\n\nGood bye... ")
            exit()


main()

