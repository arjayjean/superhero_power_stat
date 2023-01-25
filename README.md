<h1 align="center">SuperHeroAPI ETL</h1>

<h3 align="center">🧰 Languages and Tools</h3>
<p align="center">
<img src="https://user-images.githubusercontent.com/97479656/214640126-fecee2a9-0364-4b9f-ab7a-28560eec360d.png">
</p>
<hr>

### I have created an ETL that:
* **Extract:** Data is extracted from a SuperHero API by [Yoann Cribier](https://akabab.github.io/superhero-api/api/ "SuperHero API")
* **Transform:** It will be transformed in Python from its JSON format into a form that fits the MySQL database
* **Load:** Then loaded into a MySQL database
#

<h3 align="center">⚙ ETL Process</h3>
<p align="center">
<img src="https://user-images.githubusercontent.com/97479656/207793761-9c3a6101-0d2e-4119-a10f-30d89853c562.png">
</p>

### Notes:
* Before I execute the ETL, I need to take more time transforming the data. The data was transformed but I need to replace the redundant data that was loaded. There were entities that were empty values, that needed to be NULL, and names that were repeated in the "alias" and "name" column. This will take time away from analysis that needs to be made. Instead of making those analysis, data cleaning would have to be done before; which is what I have done in MySQL.
