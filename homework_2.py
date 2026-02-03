ratings = {
 "Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
 "Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
 "Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
 "Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
 "Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}

print(f"===Movie Statistics===")

for user, movies in ratings.items():
    num_rated = len(movies)
    avg_rating = sum(movies.values()) / num_rated
    highest_rated = max(movies, key=movies.get)
    
    print(f"{user}: {num_rated} movies, average rating: {avg_rating:.2f}, highest rated movie was: {highest_rated} with the score of {movies [highest_rated]}")
    print("\n")
    print(f"===Movie Ratings===")
    movie_stats = {}
    for user, movies in ratings.items(): 
        for movie, score in movies.items():
            if movie not in movie_stats:
                
             movie_stats[movie] = {"ratings": []}
              
            movie_stats[movie]["ratings"].append(score)
            

for movie, data in movie_stats.items():
    scores = data["ratings"]
    data["count"] = len(scores)
    data["avg"] = sum(scores) / len(scores)
    
sorted_movies = sorted(movie_stats.items(), key=lambda x: x[1]["avg"], reverse=True)

for movie, data in sorted_movies:
    print(f"{movie}: {data['avg']:.2f} avg ({data['count']}) reviews")

    
