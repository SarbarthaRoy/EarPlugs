from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.imdb.com/chart/top/"
toprated=requests.get(url)
url2="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc&view=simple"
action=requests.get(url2)
url3="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=user_rating,desc&view=simple"
adventure=requests.get(url3)
url4="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=animation&sort=user_rating,desc&view=simple"
animation=requests.get(url4)
url5="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=biography&sort=user_rating,desc&view=simple"
biography=requests.get(url5)
url6="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=comedy&sort=user_rating,desc&view=simple"
comedi=requests.get(url6)
url7="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=crime&sort=user_rating,desc&view=simple"
crime=requests.get(url7)
url8="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=user_rating,desc&view=simple"
drama=requests.get(url8)
url9="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=family&sort=user_rating,desc&view=simple"
family=requests.get(url9)
url10="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=fantasy&sort=user_rating,desc&view=simple"
fantasy=requests.get(url10)
url11="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=film-noir&sort=user_rating,desc&view=simple"
film_noir=requests.get(url11)
url12="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=history&sort=user_rating,desc&view=simple"
history=requests.get(url12)
url13="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc&view=simple"
horror=requests.get(url13)
url14="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=music&sort=user_rating,desc&view=simple"
music=requests.get(url14)
url15="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=musical&sort=user_rating,desc&view=simple"
musical=requests.get(url15)
url16="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=mystery&sort=user_rating,desc&view=simple"
mystery=requests.get(url16)
url17="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=romance&sort=user_rating,desc&view=simple"
romance=requests.get(url17)
url18="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sci-fi&sort=user_rating,desc&view=simple"
sci_fi=requests.get(url18)
url19="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sport&sort=user_rating,desc&view=simple"
sport=requests.get(url19)
url20="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=thriller&sort=user_rating,desc&view=simple"
thriller=requests.get(url20)
url21="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=war&sort=user_rating,desc&view=simple"
war=requests.get(url21)
url22="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=western&sort=user_rating,desc&view=simple"
western=requests.get(url22)

soup=BeautifulSoup(toprated.content,"html.parser")

soup2=BeautifulSoup(action.content,"html.parser")

soup3=BeautifulSoup(adventure.content,"html.parser")

soup4=BeautifulSoup(animation.content,"html.parser")

soup5=BeautifulSoup(biography.content,"html.parser")

soup6=BeautifulSoup(comedi.content,"html.parser")

soup7=BeautifulSoup(crime.content,"html.parser")

soup8=BeautifulSoup(drama.content,"html.parser")

soup9=BeautifulSoup(family.content,"html.parser")

soup10=BeautifulSoup(fantasy.content,"html.parser")

soup11=BeautifulSoup(film_noir.content,"html.parser")

soup12=BeautifulSoup(history.content,"html.parser")

soup13=BeautifulSoup(horror.content,"html.parser")

soup14=BeautifulSoup(music.content,"html.parser")

soup15=BeautifulSoup(musical.content,"html.parser")

soup16=BeautifulSoup(mystery.content,"html.parser")

soup17=BeautifulSoup(romance.content,"html.parser")

soup18=BeautifulSoup(sci_fi.content,"html.parser")

soup19=BeautifulSoup(sport.content,"html.parser")

soup20=BeautifulSoup(thriller.content,"html.parser")

soup21=BeautifulSoup(war.content,"html.parser")

soup22=BeautifulSoup(western.content,"html.parser")




action_ratings=soup2.find_all('div',class_="col-imdb-rating")
adventure_ratings=soup3.find_all('div',class_='col-imdb-rating')
animation_ratings=soup4.find_all('div',class_='col-imdb-rating')
biography_ratings=soup5.find_all('div',class_='col-imdb-rating')
comedy_ratings=soup6.find_all('div',class_='col-imdb-rating')
crime_ratings=soup7.find_all('div',class_='col-imdb-rating')
drama_ratings=soup8.find_all('div',class_='col-imdb-rating')
family_ratings=soup9.find_all('div',class_='col-imdb-rating')
fantasy_ratings=soup10.find_all('div',class_='col-imdb-rating')
filmnoir_ratings=soup11.find_all('div',class_='col-imdb-rating')
history_ratings=soup12.find_all('div',class_='col-imdb-rating')
horror_ratings=soup13.find_all('div',class_='col-imdb-rating')
music_ratings=soup14.find_all('div',class_='col-imdb-rating')
musical_ratings=soup15.find_all('div',class_='col-imdb-rating')
mystery_ratings=soup16.find_all('div',class_='col-imdb-rating')
romance_ratings=soup17.find_all('div',class_='col-imdb-rating')
scifi_ratings=soup18.find_all('div',class_='col-imdb-rating')
sports_ratings=soup19.find_all('div',class_='col-imdb-rating')
thriller_ratings=soup20.find_all('div',class_='col-imdb-rating')
war_ratings=soup21.find_all('div',class_='col-imdb-rating')
western_ratings=soup22.find_all('div',class_='col-imdb-rating')


ratings_action=[]
for rating in action_ratings[:10]:
    rating=rating.get_text().replace('\n',"")
    rating=rating.strip(" ")
    ratings_action.append(rating)


ratings_adventure=[]
for rating in adventure_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_adventure.append(rating)
ratings_animation=[]
                             
for rating in animation_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_animation.append(rating)




ratings_biography=[]
for rating in biography_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_biography.append(rating)




ratings_comedy=[]
for rating in comedy_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_comedy.append(rating)




ratings_crime=[]
for rating in crime_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_crime.append(rating)




ratings_drama=[]
for rating in drama_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_drama.append(rating)




ratings_family=[]
for rating in family_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_family.append(rating)




ratings_fantasy=[]
for rating in fantasy_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_fantasy.append(rating)




ratings_filmnoir=[]
for rating in filmnoir_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_filmnoir.append(rating)




ratings_history=[]
for rating in history_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_history.append(rating)




ratings_horror=[]
for rating in horror_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_horror.append(rating)




ratings_music=[]
for rating in music_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_music.append(rating)




ratings_musical=[]
for rating in musical_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_musical.append(rating)




ratings_mystery=[]
for rating in mystery_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_mystery.append(rating)




ratings_romance=[]
for rating in romance_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_romance.append(rating)




ratings_scifi=[]
for rating in scifi_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_scifi.append(rating)




ratings_sports=[]
for rating in sports_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_sports.append(rating)




ratings_thriller=[]
for rating in thriller_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_thriller.append(rating)




ratings_war=[]
for rating in war_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_war.append(rating)




ratings_western=[]
for rating in western_ratings[:10]:
    rating=rating.get_text().replace('\n','')
    rating=rating.strip(" ")
    ratings_western.append(rating)




scrapped_genre=soup.find_all('li',class_='subnav_item_main')


def movie_genre():
    genres=[]
    for genre in scrapped_genre:
        genre=genre.get_text().replace('\n','')
        genres.append(genre)
    data1=pd.DataFrame(index=[i for i in range(1,len(genres)+1)])
    data1['Genre']=genres
    print(data1.head(21))




scrapped_action=soup2.find_all('div',class_='col-title')




action_movies=[]
for movie in scrapped_action[:10]:
    movie=movie.get_text().replace('\n','')
    action_movies.append(movie)




scrapped_adventure=soup3.find_all('div',class_='col-title')




scrapped_animation=soup4.find_all('div',class_='col-title')




scrapped_biography=soup5.find_all('div',class_='col-title')




scrapped_comedy=soup6.find_all('div',class_='col-title')




scrapped_crime=soup7.find_all('div',class_='col-title')




scrapped_drama=soup8.find_all('div',class_='col-title')




scrapped_family=soup9.find_all('div',class_='col-title')




scrapped_fantasy=soup10.find_all('div',class_='col-title')




scrapped_film_noir=soup11.find_all('div',class_='col-title')




scrapped_history=soup12.find_all('div',class_='col-title')




scrapped_horror=soup13.find_all('div',class_='col-title')




scrapped_music=soup14.find_all('div',class_='col-title')




scrapped_musical=soup15.find_all('div',class_='col-title')




scrapped_mystery=soup16.find_all('div',class_='col-title')




scrapped_romance=soup17.find_all('div',class_='col-title')




scrapped_sci_fi=soup18.find_all('div',class_='col-title')




scrapped_sport=soup19.find_all('div',class_='col-title')




scrapped_thriller=soup20.find_all('div',class_='col-title')




scrapped_war=soup21.find_all('div',class_='col-title')




scrapped_western=soup22.find_all('div',class_='col-title')




adventure_movies=[]
for movie in scrapped_adventure[:10]:
    movie=movie.get_text().replace('\n','')
    adventure_movies.append(movie)




animation_movies=[]
for movie in scrapped_animation[:10]:
    movie=movie.get_text().replace('\n','')
    animation_movies.append(movie)




biography_movies=[]
for movie in scrapped_biography[:10]:
    movie=movie.get_text().replace('\n','')
    biography_movies.append(movie)




comedy_movies=[]
for movie in scrapped_comedy[:10]:
    movie=movie.get_text().replace('\n','')
    comedy_movies.append(movie)




crime_movies=[]
for movie in scrapped_crime[:10]:
    movie=movie.get_text().replace('\n','')
    crime_movies.append(movie)




family_movies=[]
for movie in scrapped_family[:10]:
    movie=movie.get_text().replace('\n','')
    family_movies.append(movie)




drama_movies=[]
for movie in scrapped_drama[:10]:
    movie=movie.get_text().replace('\n','')
    drama_movies.append(movie)




fantasy_movies=[]
for movie in scrapped_fantasy[:10]:
    movie=movie.get_text().replace('\n','')
    fantasy_movies.append(movie)




filmnoir_movies=[]
for movie in scrapped_film_noir[:10]:
    movie=movie.get_text().replace('\n','')
    filmnoir_movies.append(movie)




history_movies=[]
for movie in scrapped_history[:10]:
    movie=movie.get_text().replace('\n','')
    history_movies.append(movie)




horror_movies=[]
for movie in scrapped_horror[:10]:
    movie=movie.get_text().replace('\n','')
    horror_movies.append(movie)




music_movies=[]
for movie in scrapped_music[:10]:
    movie=movie.get_text().replace('\n','')
    music_movies.append(movie)




musical_movies=[]
for movie in scrapped_musical[:10]:
    movie=movie.get_text().replace('\n','')
    musical_movies.append(movie)




mystery_movies=[]
for movie in scrapped_mystery[:10]:
    movie=movie.get_text().replace('\n','')
    mystery_movies.append(movie)




romance_movies=[]
for movie in scrapped_romance[:10]:
    movie=movie.get_text().replace('\n','')
    romance_movies.append(movie)




scifi_movies=[]
for movie in scrapped_sci_fi[:10]:
    movie=movie.get_text().replace('\n','')
    scifi_movies.append(movie)




sport_movies=[]
for movie in scrapped_sport[:10]:
    movie=movie.get_text().replace('\n','')
    sport_movies.append(movie)




thriller_movies=[]
for movie in scrapped_thriller[:10]:
    movie=movie.get_text().replace('\n','')
    thriller_movies.append(movie)




war_movies=[]
for movie in scrapped_war[:10]:
    movie=movie.get_text().replace('\n','')
    war_movies.append(movie)




western_movies=[]
for movie in scrapped_western[:10]:
    movie=movie.get_text().replace('\n','')
    western_movies.append(movie)



def action():
    data2=pd.DataFrame(index=action_movies)
    data2['Ratings']=ratings_action
    print(data2.head(21))



def adventure():
    data2=pd.DataFrame(index=adventure_movies)
    data2['Ratings']=ratings_adventure
    data2.head(21)
    print(data2.head(21))

    
def animation():
    data2=pd.DataFrame(index=animation_movies)
    data2['Ratings']=ratings_animation
    data2.head(21)
    print(data2.head(21))

    
def biography():
    data2=pd.DataFrame(index=biography_movies)
    data2['Ratings']=ratings_biography
    data2.head(21)
    print(data2.head(21))

    
def comedy():
    data2=pd.DataFrame(index=comedy_movies)
    data2['Ratings']=ratings_comedy
    data2.head(21)
    print(data2.head(21))

    
def crime():
    data2=pd.DataFrame(index=crime_movies)
    data2['Ratings']=ratings_crime
    data2.head(21)
    print(data2.head(21))

    
def drama():
    data2=pd.DataFrame(index=drama_movies)
    data2['Ratings']=ratings_drama
    data2.head(21)
    print(data2.head(21))

    
def family():
    data2=pd.DataFrame(index=family_movies)
    data2['Ratings']=ratings_family
    data2.head(21)
    print(data2.head(21))

    
def fantasy():
    data2=pd.DataFrame(index=fantasy_movies)
    data2['Ratings']=ratings_fantasy
    data2.head(21)
    print(data2.head(21))

    
def film_noir():
    data2=pd.DataFrame(index=filmnoir_movies)
    data2['Ratings']=ratings_filmnoir
    data2.head(21)
    print(data2.head(21))

    
def history():
    data2=pd.DataFrame(index=history_movies)
    data2['Ratings']=ratings_history
    data2.head(21)
    print(data2.head(21))

    
def horror():
    data2=pd.DataFrame(index=horror_movies)
    data2['Ratings']=ratings_horror
    data2.head(21)
    print(data2.head(21))

    
def music():
    data2=pd.DataFrame(index=music_movies)
    data2['Ratings']=ratings_music
    data2.head(21)
    print(data2.head(21))

    
def musical():
    data2=pd.DataFrame(index=musical_movies)
    data2['Ratings']=ratings_musical
    data2.head(21)
    print(data2.head(21))

    
def mystery():
    data2=pd.DataFrame(index=mystery_movies)
    data2['Ratings']=ratings_mystery
    data2.head(21)
    print(data2.head(21))

def romance():
    data2=pd.DataFrame(index=romance_movies)
    data2['Ratings']=ratings_romance
    data2.head(21)
    print(data2.head(21))


def scifi():
    data2=pd.DataFrame(index=scifi_movies)
    data2['Ratings']=ratings_scifi
    data2.head(21)
    print(data2.head(21))



def sports():
    data2=pd.DataFrame(index=sport_movies)
    data2['Ratings']=ratings_sports
    print(data2.head(21))
    
def thriller():
    data2=pd.DataFrame(index=thriller_movies)
    data2['Ratings']=ratings_thriller
    data2.head(21)
    print(data2.head(21))


def war():
    data2=pd.DataFrame(index=war_movies)
    data2['Ratings']=ratings_war
    data2.head(21)
    print(data2.head(21))


def western():
    data2=pd.DataFrame(index=western_movies)
    data2['Ratings']=ratings_western
    data2.head(21)
    print(data2.head(21))
