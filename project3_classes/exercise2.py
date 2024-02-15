class Book:
    def __init__(self, title, author,ratings):
        self.title = title
        self.author = author
        self.ratings = ratings
    
    def average_rating(self):
        average_of_ratings = sum(self.ratings)/len(self.ratings)
        # print(f"Srednia z ocen to {average_of_ratings}")
        return average_of_ratings
    
    def display_info(self):
        avg = self.average_rating()
        print(f"Ksiazka ma tytul {self.title}, napisana przez {self.author} a srednia ocen to {avg}")

    def add_rating(self, new_rate):
        self.ratings.append(new_rate)


ksiazka1 = Book("Latarnik", "Henryk Sienkiewicz", [2, 4, 5, 1])
ksiazka1.display_info()
ksiazka1.add_rating(5)
ksiazka1.display_info()


