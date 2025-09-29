# A Simple Movie Recommendation System.

It is a basic command line example of a movie recommendation system, which is written as part of the ICT 2233 Data Structures and Algorithms assignment.

## Description

The program recommends films to a user depending on the ratings of another user sharing the same tastes. It is a simplistic application of User-Based Collaborative Filtering.

The primary data structure is a ** Dictionary (that is a Hash Table) in which user rating and movie titles are stored and accessed very fast. The comparison is also done efficiently in the algorithm using Sets.

## How to Run

1.  Ensure that you have Python 3.
2.  Ensure that they also lie in the same directory as the recommend.py, movies.csv and ratings.csv.
3.  Fire up a terminal or command prompt in the project.
4.  Execute the script by the following command:
    ```bash
    python recommend.py
    ```
5.  Do what there is on the screen. You will be requested to input a User ID that is listed on a list of available users.
6.  type `exit` to terminate the program.

## Algorithm Explained

1.  **Load Data:** This program reads all data stored in the.csv files and then loads all data into dynamically named dictionaries where all information can be found quickly.
2.  **Find Similar User:** As you type in your User ID, the program will compare your movies that you have rated (rating greater or equal to 4.0) to all other users. It matches you with the single user, who has the most movies liked by you.
3.  **Recommendation:** The application then picks up the likes of this similar user, eliminates the movies you have already watched and suggests the rest.# Movie Recommendation System Simple.

It is a basic command line example of a movie recommendation system, which is written as part of the ICT 2233 Data Structures and Algorithms assignment.

## Description

The program recommends films to a user depending on the ratings of another user sharing the same tastes. It is a simplistic application of User-Based Collaborative Filtering.

The primary data structure is a ** Dictionary (that is a Hash Table) in which user rating and movie titles are stored and accessed very fast. The comparison is also done efficiently in the algorithm using Sets.

## How to Run

1.  Ensure that you have Python 3.
2.  Ensure that they also lie in the same directory as the recommend.py, movies.csv and ratings.csv.
3.  Fire up a terminal or command prompt in the project.
4.  Execute the script by the following command:
    ```bash
    python recommend.py
    ```
5.  Do what there is on the screen. You will be requested to input a User ID that is listed on a list of available users.
6.  type `exit` to terminate the program.

## Algorithm Explained

1.  **Load Data:** This program reads all data stored in the.csv files and then loads all data into dynamically named dictionaries where all information can be found quickly.
2.  **Find Similar User:** As you type in your User ID, the program will compare your movies that you have rated (rating greater or equal to 4.0) to all other users. It matches you with the single user, who has the most movies liked by you.
3.  **Recommendation:** The application then picks up the likes of this similar user, eliminates the movies you have already watched and suggests the rest.