
# Movie Recommendation System




## Introduction
Movie recommendation system is a system that has been designed in such a way that it shows the top rated movies of a particular genre at the top of the list and goes down in descending order.

## Resources :
Here we have used some python libraries such as :

1> pandas :- It is used to create a dataframe.

2> BeautifulSoup :- It is used for web scraping purposes to pull the data out of HTML files.
It helps to create a parse tree that can be used to extract data in a hierarchical and more readable manner.





## Methods Used :

request :- It is a method that helps to make HTTP request to the specified URL using GET function from the request module.
## Variables used :

Variable used :- Here we have used a Variable named as 'url' that helps to store the HTML link of the movies from the IMDB website through the Beautiful Soup library.

### Process of execution :
Following are the steps to be used to execute the code :

1> First we have to import the movie recommendation system code as a package into the main program named as 'MovieRecom'

2> Now, we have to use the beautiful soup library to seek the URL link of each genres of the movies using the   requests.get()  method.

3> After that we have to use the .find_all() method to get the ratings and names of the top 10 movies. 

4> Now, we have to use the DataFrame provided by the pandas module to get the list of the movies in an organized tabular form.

### Time Complexity :
Since we haven't used a very compact way to implement this code, the time Complexity is a bit higher than expected.However, we are working on optimizing the Complexity as much as possible.

