file = open("movies.txt", "w")
movie_titles = ["Skazani na Shawshank", "Nietykalni", "Zielona mila", "Ojciec chrzestny", "Dwunastu gniewnych ludzi"]
for i in movie_titles:
    file.write(i+"\n")
file.close()