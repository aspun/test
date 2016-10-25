import media
import fresh_tomatoes
toystory=media.Movie('Toy Story',
                     'A story of a boy whose toys came back to life',
                     'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                     'https://www.youtube.com/watch?v=4KPTXpQehio'
                     )
zootopia=media.Movie('Zootopia',
                     'A story of a rabbit to become first police officer',
                     'https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg',
                     'https://www.youtube.com/watch?v=bY73vFGhSVk')
frozen=media.Movie('Frozen',
                    'A story about a snow queen and her sister plus a snowman',
                    'https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg',
                    'https://www.youtube.com/watch?v=TbQm5doF_Uc')

movies=[toystory,zootopia,frozen]
fresh_tomatoes.open_movies_page(movies) #open the movies_page using the fresh_tomatoes.py html file
