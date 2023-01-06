# SuperHeroAPI ETL

### I have created an ETL that:
* **Extract:** Data is extracted from a SuperHero API by [Yoann Cribier](https://akabab.github.io/superhero-api/api/ "SuperHero API")
* **Transform:** It will be transformed in Python from its JSON format into a form that fits the MySQL database
* **Load:** Then loaded into a MySQL database

### Purpose:
* This project was my introduction into learning how to implement an ETL process with Python. My goal was to find out who was the best super hero and super villain in their respected universe and overall. In order to do so, I needed to take the stats for each individual character, that was provided, and calculate them into an overall rating.     

### ETL Process:
1. Request access to the API
2. Dump the API data into a JSON file, in order to have the data locally
3. Transform and prepare the data to be loaded into the MySQL database
4. Connect to the MySQL database
5. Load the data into the MySQL database

![ETL Process](https://user-images.githubusercontent.com/97479656/207793761-9c3a6101-0d2e-4119-a10f-30d89853c562.png)

### Requirements:
* Python
* SQL Alchemy
* MySQL

### Notes:
* Before I execute the ETL, I need to take more time transforming the data. The data was transformed but I need to replace the redundant data that was loaded. There were entities that were empty values, that needed to be NULL, and names that were repeated in the "alias" and "name" column. This will take time away from analysis that needs to be made. Instead of making those analysis, data cleaning would have to be done before; which is what I have done in MySQL.
