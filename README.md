# Scraping Otomoto Into Google Spreadsheet
 A project that scrapes the Otomoto website for car details using python and scrappy and stores the data in csv file that get imported into a Google spreadsheet using the google spreadsheet API and Node it also stores the extracted data into a mongodb DataBase and exposes endpoints using nodess and Express to be used in a front end application.



# Otomoto Scraping



Otomoto Scraping to provied endpoints to scraped data in json or csv fromat by accessing the links : 
    - localhost:5005/scraping/
  - localhost:5005/scraping/otomoto
 
  

# Otomoto.py Explained :
In order to scrape the data for the otomoto website i had to use the python library scrapy then save the data extracted automatically to the mongodb data base by activating the pipeline and linking the items to the data base. 

Otomoto.js is made using scrapy and is a standalone file that can used to get the data from otomoto website on any other porject and can also be used to generate a csv file.
### Back End : Using Nodejs Express Mongoose
### Models : Otomoto.js

Using mongoose i created a schema model for the otomoto data in order to store the data extracted using the scraper.js file the model fields are : 

* [brand] - is the brand 
* [model] - is the car model 
* [year] - is the year the car was made 
* [mileage] - is the migeagle of the car 
* [capacity] - is obviously the capacity of the car
* [phone_number] - is the phone number 
* [fuel_type] - is the fuel type of the car
* [horse_power] - is how much horse power a car has
* [type] - is the type of the car 
* [number_of_doors] - is the number of doors of the car 
* [price] - is the price of the car 
and other fileds of data 
the model is then exported to the server ( server.js) file

### Routers : server.js

on the service.js file that handles routes we have 2 middlewares : 
    - / : first middleware that handles all requests comming from /scraping and sends them a message response like this : " Use /scraping/otomoto  to get the json "
    - /:allegro : second middleware handles all requests comming from /scraping/otomoto and in the same time gets the data extracted and stored on the mongodb data and displays it - 
### connection.js

Used to connect to the data on "mongodb://localhost:27017/scraping" and store the extracted data in the collection named otomoto and expose a port "5005" in my case (can be changed) to listen to the comming requests

### main.js :  Connecting the csv files to google sheet 
the main.js contains credentials and authentification information used in order to connect to the google sheet api and store the data extrated using (scrapy otomoto.py) inside the a google sheet document that can be accessed from a public link.


### Installation :  
To start get access the endpoints first we have to install a few dependencies : 
    - scrapy : by using pip install scrapy and then using the command scrapy crawl otomoto
    - "body-parser": "^1.19.0",
    - "exceljs": "^4.0.1",
    - "express": "^4.17.1",
    - "fs": "0.0.1-security",
    - "google-spreadsheet": "^3.0.11",
    - "googleapis": "^39.2.0",
    - "mongoose": "^5.9.18",
    - "nodemon": "^2.0.4",
    - "readline": "^1.3.0",
    - "request": "^2.88.2"
all of these dependencies are inside the package.json file so only use the command : "npm install" to get going.
note : the scraper project using scrapy is a standalone project that can be used on other projects to get started install scrapy and then use the command scrapy crawl otomoto ( can be used to generate either json or csv data )

