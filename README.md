# Stock Information Lookup
Provides ability to lookup stock information based on the company's ticker symbol. Also provides ability to create a stock "portfolio" where you can add and remove stocks of interest.


# How to run
## Start server
In directory with manage.py file
- `python manage.py runserver`
## Connect to server
In browser
- `localhost:8000/`

### Note
Currently the ticker needs to be entered in all lowercase for the delete functionality to work correctly. Looking into ability to type ticker as desired and then have the database only save it as all lowercase to solve this.