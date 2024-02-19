# Design a program that lets users rate movies on a scale from 1 to 5. Use a dictionary to store 
# movie titles and their average ratings.
movie_ratings = {
    "Inception": 4.5,
    "The Shawshank Redemption": 4.8,
    "The Godfather": 4.7,
    "Pulp Fiction": 4.6,
    "The Dark Knight": 4.9,
    "Dilwale Dulhania Le Jayenge": 4.7, 
    "Bahubali": 4.3  
}

while True:
    print("Movies in the database:")
    for movie in movie_ratings:
        print(movie)
    break
movie = input("Enter the movie you want to rate (or type 'exit' to quit): ")
if movie.lower() == "exit":
        print("Goodbye!")
                   
if movie in movie_ratings:
        rating = float(input("Enter your rating for the movie (from 1 to 5): "))
        if 1 <= rating <= 5:
            movie_ratings[movie] = rating
            print(f"Rating for {movie} updated to {rating}.")
        else:
            print("Invalid rating! Rating should be between 1 and 5.")
else:
        print("Movie not found in the database. Please enter a valid movie.")