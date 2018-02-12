import fresh_tomatoes
import media

# created 1st movie instance
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )


# created 2nd movie instance
high_school_musical = media.Movie(
    "High School Musical",
    "Love stroy of a school boy and girl",
    "https://upload.wikimedia.org/wikipedia/en/a/a5/HSMposter.jpg",  # noqa
    "https://www.youtube.com/watch?v=ukDLkkvZYFk"    # noqa
    )


# created 3rd movie instance
dangal = media.Movie(
    "Dangal",
    "Story of a father who trained his daughters for the "
    "Commonwealth Games despite societal pressures.",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=x_7YlGv9u1g"  # noqa
    )


# created 4th movie instance
finding_nemo = media.Movie(
    "Finding Nemo",
    "A story of a fish who gets lost",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",  # noqa
    "https://www.youtube.com/watch?v=wZdpNglLbt8"  # noqa
    )

# created 5th movie instance
sairat = media.Movie(
    "Sairat",
    "Story of College friends Archi and Parshya, "
    "who have contrasting personalities and belong "
    "to different castes, fall in love. However, their "
    "relationship falls prey to the stringent "
    "practice of casteism.",
    "https://upload.wikimedia.org/wikipedia/en/a/a1/Sairat_Marathi_Film_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=X8Z73ce9Vbo"  # noqa
    )

# created 6th movie instance
queen = media.Movie(
    "Queen", "A homely girl who decides to "
    "go on her honeymoon alone when her fiance "
    "call off the wedding",
    "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",  # noqa
    "https://www.youtube.com/watch?v=KGC6vl3lzf0"  # noqa
    )

# array of movies
movies = [
    toy_story,
    high_school_musical,
    dangal,
    finding_nemo,
    sairat,
    queen
    ]

# opening movie page for movies using fresh.tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
