	    # IT INVENTORY TRACKER
    #### Video Demo:  <https://youtu.be/tgFN6AejaNM>
    #### Description:

    - INTRODUCTION:
        According to Wikipedia, inventory refers to the goods and materials that a business holds for the ultimate goal of resale, production or utilisation.
        It helps companies to keep track of their assets and also make financial decisions.

        IT INVENTORY TRACKER is a command-line application which allow you to add items to the database, query the data, edit the data,
        view all the data and provides a textbased dashboard for a summary of what the database contains.
    
    - HOW TO USE IT:
        You can run the program with ***python project.py*** with no command-line argument. A menu will be displayed. You can select a menu by pressing the number attached to it.

    The IT INVENTORY TRACKER is robust enough to store information and states about your assists



                                                #### PROJECT.PY


    1. DASHBOARD:
            The dashboard function queries the SQL database and group the sets in 4 groups; CPUs, Monitors, Peripherals and Laptops.
            It colours the data using the colorama module and display the data.
            It takes no argument and returns None

    2. ADD ITEM:
            The add item function takes no argument. It asks the properties of the item to be added from the user
            and create an Inventory object from the Inventory class from inv_utils.
            The attributes of the object are stored in the database. It returns True if the data is saved successfully. Otherwise, False.
    

    3. VIEW ITEMS:
            The view item’s function takes no argument. It also queries the database this time, scrapes everything and tabulate it with the tabulate module.
            It returns a formatted table containing the query result in rows and columns.
            It returns an empty string if no data was found in the database which can be interpreted as False.
    

    4. SEARCH ITEM:
            The search item function searches an item by the model. It fetches all the items with the same model and return them in a table format like how the view items function does.
            It returns an empty string indicating False when no matches were found.
    

    5. EDIT ITEM:
            The edit item queries a device by its serial number which have to be unique for a better result.
            If a match to the serial number is found, it displays a menu showing you what you would like to edit.
            Just like how the 'HOW TO USE IT' above mentioned, you type a number attached to it and change the value. The database will commit the changes and save the data.
            It returns True if the new property is set and saved in the database successfully, otherwise it returns False indicating an error.
    

    6. DELETE ITEM:
            Just like the edit item module, it also searches the data in the database by its serial number.
            It fetches one and if the serial number of that match is same as what the user provided,
            It deletes the item and returns True. Otherwise, it returns False if no match was found or any error is encountered.

    7. EXPORT ITEMS:
            The export items functions render the list of tuples which contained the items read from the database.
            It uses the Pandas library to create a data frame from the list of tuples and export them into a csv fie.
            It returns True if successful, Otherwise False

    8.  QUIT: 
            The quit function exits you out of the program
    

    9. CLEAR:
            The clear function clears the screen for a better user experience
    

                                            #### INV-UTILS.PY

    
    1. INVENTORY:
            Inventory is a class that instantiate an Inventory object called an item with properties such as a model, serial_number, category and location etc.
            It has one method, called the __init__ method.
            The program follows a functional approach rather than an object-oriented approach.
    

    2. GET_DATE:
            The get date function takes in a string or a prompt and asks a user to input a date in a correct format YYYY-MM-DD.
            If the user does not cooperate, it handles the exception and keeps prompting the user until he or she cooperates.
            It returns a string version if the date in correct format which is return by the datetime. date () method.
    

    3. GET_STATUS:
            The get status takes in no argument and returns a str.
            it displays a list of conditions or states in which an item could be.
            The user will enter a number corresponding to that value and it will return that value.
            It will keep prompting the user, so long as they failed to cooperate.
    

    4. GET_CATEGORY:
            The get category takes in no argument and returns a str.
            it displays a list of categories in which an item could belong to.
            The user will enter a number corresponding to that value and it will return that value.
            It will keep prompting the user, so long as they failed to cooperate.           


                                            #### HOW CAN IT BE IMPROVED

    - Incorporating graphical user interfaces for navigation instead of commands

    - Reformatting of the dashboard to use charts and graphs to display the data in a very informative way
