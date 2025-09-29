import csv

# Load data from the CSV files ---

def _load_data():
    movieTitles = {}
    try:
        with open('movies.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                movieId = int(row[0])
                title = row[1]
                movieTitles[movieId] = title
    except FileNotFoundError:
        print("Error: Movies Not Found.")
        return None, None

    userRatings = {}
    try:
        with open('ratings.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                userId = int(row[0])
                movieId = int(row[1])
                rating = float(row[2])
                
                if userId not in userRatings:
                    userRatings[userId] = {}
                
                userRatings[userId][movieId] = rating
    except FileNotFoundError:
        print("Error: Ratings Not Found.")
        return None, None

    return movieTitles, userRatings



# Find the similar user
def _find_similar_user(targetUserId, allRatings):
    if targetUserId not in allRatings:
        return None

    targetUserMovies = {movieId for movieId, rating in allRatings[targetUserId].items() if rating >= 4.0}
    
    matchingUserId = None
    maxCommonMovies = -1

    # Compare the target user with other users
    for otherUserId, ratings in allRatings.items():
        if otherUserId == targetUserId:
            continue
        
        otherUserMovies = {movieId for movieId, rating in ratings.items() if rating >= 4.0}
        
    
        commonMovies = targetUserMovies.intersection(otherUserMovies)
        
        if len(commonMovies) > maxCommonMovies:
            maxCommonMovies = len(commonMovies)
            matchingUserId = otherUserId
            
    return matchingUserId



#  Generate recommendations 
def _get_recommendations(targetUserId, similarUserId, allRatings, movieTitles):

    if similarUserId is None:
        return []

    similarUserMovies = {movieId for movieId, rating in allRatings[similarUserId].items() if rating >= 4.0}
    targetUserWatchedMovies = set(allRatings[targetUserId].keys())
    

    recommendationsIds = similarUserMovies.difference(targetUserWatchedMovies)
    
    recommendedMovieTitles = [movieTitles[movieId] for movieId in recommendationsIds]
    
    return recommendedMovieTitles

# CLI
def main():
  
    print(" Movie Recommendation System Prototype ")
    
    movieTitles, userRatings = _load_data()
    
    if movieTitles is None or userRatings is None:
        return

    availableUsers = sorted(userRatings.keys())
    print(f"\nAvailable User IDs: {availableUsers}")

    while True:
        try:
            userInput = input("\nEnter a User ID to get recommendations (or type 'exit' to quit): ")
            
            if userInput.lower() == 'exit':
                print("Thank you ! ,Have a enjoyble day!")
                break
            
            targetUserId = int(userInput)
            
            if targetUserId not in userRatings:
                print("Error: This User does not exist.")
                continue

            print("\nSearching for a user with similar interest...")
            similarUserId = _find_similar_user(targetUserId, userRatings)

            if similarUserId is None:
                print(f"Could not find a suitable similar user for  this user {targetUserId}.")
                continue
            
            print(f"Found a similar user: User {similarUserId}. Generating recommendations...")
            recommendations = _get_recommendations(targetUserId, similarUserId, userRatings, movieTitles)
            
            if recommendations:
                print(f"\n Recommendations for User {targetUserId}")
                for i, title in enumerate(recommendations[:5]): 
                    print(f"{i+1}. {title}")
            else:
                print(f"\nNo new movies to recommend based on User {similarUserId}'s interest.")

        except ValueError:
            print("Invalid input. Please enter a number for the User ID.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

