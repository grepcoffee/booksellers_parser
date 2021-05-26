#Project 1 NYT Best Seller
import os
import pandas as pd
import numpy as np
import datetime as dt

def open_file():
    try:
        open_file = open('bestsellers.txt')
        bestsellers = pd.read_csv(open_file, sep="\t", names=["Title", "Author", "Publisher", "Date", "Genre"])
    except:
        print('File not in path')
        exit(1)
    return bestsellers

def display_year(start_year, end_year):
    bestsellers = open_file()
    # Create new row to make filtering easier
    bestsellers['Year'] = pd.DatetimeIndex(bestsellers['Date']).year
    years_filter = [start_year, end_year]
    filtered_year = bestsellers.Year.isin(years_filter)
    # Filter by start year and end year
    filtered_year = bestsellers[(bestsellers['Year']>=start_year) & (bestsellers['Year']<=end_year)]
    return filtered_year

def display_month_year(month, year):
    bestsellers = open_file()
    bestsellers['Date'] = pd.to_datetime(bestsellers['Date'])
    bestsellers['Year'] = pd.DatetimeIndex(bestsellers['Date']).year
    bestsellers['Month'] = pd.DatetimeIndex(bestsellers['Date']).month
    # Filter by start year and end year
    filtered_year_month = bestsellers[(bestsellers['Month']==month) & (bestsellers['Year']==year)]
    return filtered_year_month

def display_author(author):
    bestsellers = open_file()
    filtered_author = bestsellers[bestsellers['Author'].str.contains(author, case=False)]
    return filtered_author

def display_title(title):
    bestsellers = open_file()
    filtered_title = bestsellers[bestsellers['Title'].str.contains(title, case=False)]
    return filtered_title


#### Main ####
print("Welcome to NYT newspaper “best seller” lists indexer\n")
while True:
    try:
        print("1. Look up year range")
        print("2. Look up month/year")
        print("3. Search for author")
        print("4. Search for title")
        print("Q. Quit")
        question=input("What would you like to do? ")
        if question=="1":
            start_year = int(input("Please enter your start year: "))
            end_year = int(input("Please enter your end year: "))
            print(f"All titles between {start_year} and {end_year}:")
            print(display_year(start_year, end_year))
        elif question=="2":
            month = int(input("Please enter your month: "))
            year = int(input("Please enter your year: "))
            print(f"All titles in month {month} of {year}:")
            print(display_month_year(month, year))
        elif question=="3":
            author_name = str(input("Enter an author's name (or part of a name): "))
            print(display_author(author_name))
        elif question=="4":
            title = str(input("Enter a title (or part of a title): "))
            print(display_title(title))
        elif question=='q' or 'Q':
            exit(0) # clean exit
    except ValueError:
        print("\nThe input was not a valid choice. Please select a numerical value\n")