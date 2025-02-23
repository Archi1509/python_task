
def movie_rating(data):
    movie_rate = {movie: rate for movie, rate in
                  sorted(movie_ratings_data.items(), key=lambda ele: ele[1], reverse=True)}
    highest_rated_movie = (list(movie_rate.items())[:1])
    top_three_movie = dict(list(movie_rate.items())[:3])
    print(highest_rated_movie)
    print(top_three_movie)
    count=0
    sum=0
    temp={}
    for movie,rate in movie_ratings_data.items():
        if movie not in temp :
            count+=1
            sum+=rate
    avg=round(sum/count,2)
    print(f"Average Rating: {avg}")


movie_ratings_data = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}
movie_rating(movie_ratings_data)
