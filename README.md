 # Simple Movie Recommendation System

This is a simple command-line prototype for a movie recommendation system, created for the ICT 2233 Data Structures and Algorithms assignment.

## Description

The program suggests movies to a user based on the ratings of another user with similar tastes. This is a basic implementation of **User-Based Collaborative Filtering**.

The main data structure used is a **Dictionary (acting as a Hash Table)** to store and quickly access user ratings and movie titles. The algorithm also uses **Sets** for efficient comparison

## How to Run

1. Ensure that you have Python 3.
2. Make sure that the files are in the same directory as the recommend.py, movies.csv and ratings.csv.
3. Fire up a terminal or command prompt in the project.
4. Execute the script by the following command:

```bash
    python recommend.py
    ```

5. Do what there is on the screen. You will be requested to input a User ID that is listed on a list of available users.
6. type exit to terminate the program.

## Algorithm Explained

1. **Load Data: This program loads all the data in the .csv files into dictionaries where all data can be accessed rapidly.
2. **Find Similar User: As you type in your User ID, the program will compare your movies that you have rated (rating greater or equal to 4.0) to all other users. It matches you with the single user, who has the most movies liked by you.
3. **Recommendation: The application then picks up the likes of this similar user, eliminates the movies you have already watched and suggests the rest.


