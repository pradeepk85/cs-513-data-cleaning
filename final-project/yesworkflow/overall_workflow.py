'''
@begin CS_513_FinalProject 
@in Menu.csv @uri file:/raw_input/Menu.csv
@in Dish.csv @uri file:/raw_input/Dish.csv
@in MenuItem.csv @uri file:/raw_input/MenuItem.csv
@in MenuPage.csv @uri file:/raw_input/MenuPage.csv


    @begin Menu File @desc Load the csv file in OpenRefine for cleaning
    @in Menu.csv @uri file:/raw_input/Menu.csv
    @out NYPL-Menu.csv @uri file:/OpenRefine/Cleaned_data/NYPL-Menu.csv
    @end Menu
    
    @begin Dish File @desc Load the csv file in OpenRefine for cleaning
    @in Dish.csv @uri file:/raw_input/Dish.csv
    @out NYPL-Dish.csv @uri file:/OpenRefine/Cleaned_data/NYPL-Dish.csv
    @end Dish
    
    @begin MenuItem File @desc Load the csv file in OpenRefine for cleaning
    @param Python_SplitColumns_code
    @in MenuItem.csv @uri file:/raw_input/MenuItem.csv
    @out NYPL-MenuItem.csv @uri file:/OpenRefine/Cleaned_data/NYPL-MenuItem.csv
    @end MenuItem
    
    @begin MenuPage File @desc Load the csv file in OpenRefine for cleaning
    @in MenuPage.csv @uri file:/raw_input/MenuPage.csv
    @out NYPL-MenuPage.csv @uri file:/OpenRefine/Cleaned_data/NYPL-MenuPage.csv
    @end MenuPage
    
    @begin SQLite  @desc SQLite to create schema, define constraint and load the data in database
    @param SQL-Load_CreateTable_CheckandLoad_Data
    @in NYPL-Menu.csv @uri file:/OpenRefine/Cleaned_data/NYPL-Menu.csv
    @out Menu_SQlite @uri file:/SQLite/Menu_SQLite.csv
    @end SQLite
    
    @begin SQLite @desc SQLite to create schema, define constraint and load the data in database
    @param SQL-Load_CreateTable_CheckandLoad_Data
    @in NYPL-Dish.csv @uri file:/OpenRefine/Cleaned_data/NYPL-Dish.csv
    @out Dish_SQlite @uri file:/SQLite/Dish_SQLite.csv
    @end SQLite
    
    @begin SQLite @desc SQLite to create schema, define constraint and load the data in database
    @param SQL-Load_CreateTable_CheckandLoad_Data
    @in NYPL-MenuItem.csv @uri file:/OpenRefine/Cleaned_data/NYPL-MenuItem.csv
    @out MenuItem_SQlite @uri file:/SQLite/MenuItem_SQLite.csv
    @end SQLite
    
    @begin SQLite @desc Use SQLite for Developing the Relational Database Schema and Checking Coonstrains 
    @param SQL-Load_CreateTable_CheckandLoad_Data
    @in NYPL-MenuPage.csv @uri file:/OpenRefine/Cleaned_data/NYPL-MenuPage.csv
    @out MenuPage_SQlite @uri file:/SQLite/MenuPage_SQLite.csv
    @end SQLite
    
@out Menu_SQlite @uri file:/SQLite/Menu_SQLite.csv
@out Dish_SQlite @uri file:/SQLite/Dish_SQLite.csv
@out MenuItem_SQlite @uri file:/SQLite/MenuItem_SQLite.csv
@out MenuPage_SQlite @uri file:/SQLite/MenuPage_SQLite.csv
    
@end CS_513_FinalProject
'''