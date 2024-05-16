'''
    Define the Artist class with a constructor to initialize an artist's information and a print_info() method.
    The constructor should by default initialize the artist's name to "unknown" and the years of
    birth and death to -1.
    print_info() displays "Artist:", then a space, then the artist's name, then another space,
    then the birth and death dates in one of three formats:
        (XXXX to YYYY) if both the birth and death years are nonnegative
        (XXXX to present) if the birth year is nonnegative and the death year is negative
        (unknown) otherwise

    Define the Artwork class with a constructor to initialize an artwork's information and a print_info() method.
    The constructor should by default initialize the title to "unknown", the year created to -1,
    and the artist to use the Artist default constructor parameter values.
    ex:
        input:
            Pablo Picasso
            1881
            1973
            Three Musicians
            1921
        output:
            Artist: Pablo Picasso (1881 to 1973)
            Title: Three Musicians, 1921
'''


class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year


    def print_info(self):
        printing_string = f'Artist: {self.name}'
        if self.birth_year >= 0 and self.death_year >= 0:
            printing_string += f' ({self.birth_year} to {self.death_year})'
        elif self.birth_year >= 0 and self.death_year < 0:
            printing_string += f' ({self.birth_year} to present)'
        else:
            printing_string += f' (unknown)'
        print(printing_string)


class Artwork:
    def __init__(self, title="unknown",year_created=-1, artist=None):
        if artist is None:
            artist = Artist()
        self.title = title
        self.year_created = year_created


    def print_info(self):
        printing_string = f'Title: {self.title}, {self.year_created}'
        print(printing_string)


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
    user_artist.print_info()

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()