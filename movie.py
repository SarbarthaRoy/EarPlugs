from sdds import MovieRecom as mr
class Movie:
    def __init__(self):
        print("")
    def movie_categories(self):
        mr.movie_genre()
    def movie_action(self):
        mr.action()
    def movie_adventure(self):
        mr.adventure()
    def movie_animation(self):
        mr.animation()
    def movie_biography(self):
        mr.biography()
    def movie_comedy(self):
        mr.comedy()
    def movie_crime(self):
        mr.crime()
    def movie_drama(self):
        mr.drama()
    def movie_family(self):
        mr.family()
    def movie_fantasy(self):
        mr.fantasy()
    def movie_filmnoir(self):
        mr.film_noir()
    def movie_history(self):
        mr.history()
    def movie_horror(self):
        mr.horror()
    def movie_music(self):
        mr.music()
    def movie_musical(self):
        mr.musical()
    def movie_mystery(self):
        mr.mystery()
    def movie_romance(self):
        mr.romance()
    def movie_scifi(self):
        mr.scifi()
    def movie_sport(self):
        mr.sports()
    def movie_thriller(self):
        mr.thriller()
    def movie_war(self):
        mr.war()
    def movie_western(self):
        mr.western()
if __name__=='__main__':
    m=Movie()
    c=1
    print("The genres are:\n")
    m.movie_categories()
    while(c==1):
        choice=input("Enter your choice:\n").lower()
        if choice=='action':
            m.movie_action()
        elif choice=='adventure':
            m.movie_adventure()
        elif choice=='animation':
            m.movie_animation()
        elif choice=='biography':
            m.movie_biography()
        elif choice=='comedy':
            m.movie_comedy()
        elif choice=='crime':
            m.movie_crime()
        elif choice=='drama':
            m.movie_drama()
        elif choice=='family':
            m.movie_family()
        elif choice=='fantasy':
            m.movie_fantasy()
        elif choice=='filmnoir':
            m.movie_filmnoir()
        elif choice=='history':
            m.movie_history()
        elif choice=='horror':
            m.movie_horror()
        elif choice=='music':
            m.movie_music()
        elif choice=='musical':
            m.movie_musical()
        elif choice=='mystery':
            m.movie_mystery()
        elif choice=='romance':
            m.movie_romance()
        elif choice=='sport':
            m.movie_sport()
        elif choice=='scifi':
            m.movie_scifi()
        elif choice=='thriller':
            m.movie_thriller()
        elif choice=='war':
            m.movie_war()
        elif choice=='western':
            m.movie_western()
        else:
            print("Wrong choice\n")
        print("Do you want to try again?(1/0)\n")
        c=int(input())
    print("THANK YOU")
