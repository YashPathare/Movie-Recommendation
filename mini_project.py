import tkinter as tk
from tkinter import ttk
import sqlite3
class MovieRecommendationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")
        self.create_database()
        labels = ['Select Actor:', 'Select Actress:', 'Select Genre:', 'Select IMDb Rating(more than):']
        
        for i, label_text in enumerate(labels):
            label = tk.Label(root, text=label_text)
            label.grid(row=0, column=i, padx=20, pady=5)
            
        self.actors = self.create_combobox(root, self.get_actor_names(), 1, 0)
        self.actresses = self.create_combobox(root, self.get_actress_names(), 1, 1)
        self.genres = self.create_combobox(root, self.get_genre_names(), 1, 2)
        self.imdb_rating = self.create_combobox(root, ('9', '8', '7', '6', '5', 'All'), 1, 3)
        self.text_widget = tk.Text(root, height=10, width=40)
        self.text_widget.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.text_widget.config(state=tk.DISABLED)
        fetch_button = tk.Button(root, text="Fetch Recommendations", command=self.fetch_recommendations)
        fetch_button.grid(row=3, column=1, columnspan=2, pady=10)
        
    def create_database(self):
        conn = sqlite3.connect('movies_database.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS movies')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies
            (
                title TEXT,
                actor TEXT,
                actress TEXT,
                genre TEXT,
                imdb_rating REAL,
                ott TEXT
            )
        ''')
        conn.commit()
        movies_data = [
            ('Krrish 3', 'Hrithik Roshan', 'Priyanka Chopra', 'Sci-Fi', 5.3, 'Netflix'),
            ('Rocket Singh: Salesman of the Year', 'Ranbir Kapoor', 'Gauahar Khan', 'Comedy', 7.5, 'Hulu'),
            ('Kal Ho Naa Ho', 'Shah Rukh Khan', 'Preity Zinta', 'Drama', 7.9, 'Amazon Prime'),
            ('Kuch Kuch Hota Hai', 'Shah Rukh Khan', 'Kajol', 'Romance', 7.6, 'Netflix'),
            ('Dil To Pagal Hai', 'Shah Rukh Khan', 'Madhuri Dixit', 'Musical', 7.0, 'Amazon Prime'),
            ('Hum Aapke Hain Koun..!', 'Salman Khan', 'Madhuri Dixit', 'Musical', 7.6, 'Netflix'),
            ('Kabhi Khushi Kabhie Gham', 'Shah Rukh Khan', 'Kajol', 'Drama', 7.4, 'Netflix'),
            ('Koi... Mil Gaya', 'Hrithik Roshan', 'Preity Zinta', 'Sci-Fi', 7.1, 'Amazon Prime'),
            ('Hum Dil De Chuke Sanam', 'Salman Khan', 'Aishwarya Rai', 'Romance', 7.5, 'Amazon Prime'),
            ('Devdas', 'Shah Rukh Khan', 'Aishwarya Rai', 'Romance', 7.6, 'Netflix'),
            ('Black', 'Amitabh Bachchan', 'Rani Mukerji', 'Drama', 8.2, 'Amazon Prime'),
            ('Dil Se..', 'Shah Rukh Khan', 'Manisha Koirala', 'Romance', 7.6, 'Netflix'),
            ('Kabhi Alvida Naa Kehna', 'Shah Rukh Khan', 'Rani Mukerji', 'Drama', 6.1, 'Netflix'),
            ('Jab Tak Hai Jaan', 'Shah Rukh Khan', 'Katrina Kaif', 'Romance', 6.7, 'Amazon Prime'),
            ('Dilwale Dulhania Le Jayenge', 'Shah Rukh Khan', 'Kajol', 'Drama', 8.1, 'Hulu'),
            ('Shubh Mangal Zyada Saavdhan', 'Ayushmann Khurrana', 'Neena Gupta', 'Comedy', 6.9, 'Amazon Prime'),
            ('My Name Is Khan', 'Shah Rukh Khan', 'Kajol', 'Drama', 8.0, 'Amazon Prime'),
            ('Chennai Express', 'Shah Rukh Khan', 'Deepika Padukone', 'Action', 6.0, 'Netflix'),
            ('Dear Zindagi', 'Shah Rukh Khan', 'Alia Bhatt', 'Drama', 7.6, 'Amazon Prime'),
            ('Kabir Singh', 'Shahid Kapoor', 'Kiara Advani', 'Drama', 7.1, 'Netflix'),
            ('Haider', 'Shahid Kapoor', 'Tabu', 'Crime', 8.1, 'Netflix'),
            ('Udta Punjab', 'Shahid Kapoor', 'Alia Bhatt', 'Crime', 7.8, 'Netflix'),
            ('Padmaavat', 'Shahid Kapoor', 'Deepika Padukone', 'Drama', 7.0, 'Amazon Prime'),
            ('Bajirao Mastani', 'Ranveer Singh', 'Deepika Padukone', 'Drama', 7.2, 'Netflix'),
            ('Goliyon Ki Raasleela Ram-Leela', 'Ranveer Singh', 'Deepika Padukone', 'Drama', 6.3, 'Netflix'),
            ('Simmba', 'Ranveer Singh', 'Sara Ali Khan', 'Action', 5.8, 'Amazon Prime'),
            ('Tanu Weds Manu', 'R. Madhavan', 'Kangana Ranaut', 'Romance', 6.7, 'Hulu'),
            ('Queen', 'Rajkummar Rao', 'Kangana Ranaut', 'Adventure', 8.1, 'Amazon Prime'),
            ('Judgementall Hai Kya', 'Rajkummar Rao', 'Kangana Ranaut', 'Comedy', 6.1, 'Netflix'),
            ('Kahaani', 'Parambrata Chatterjee','Vidya Balan', 'Mystery', 8.1, 'Amazon Prime'),
            ('Barfi!', 'Ranbir Kapoor', 'Priyanka Chopra', 'Romance', 8.1, 'Amazon Prime'),
            ('Yeh Jawaani Hai Deewani', 'Ranbir Kapoor', 'Deepika Padukone', 'Romance', 7.1, 'Netflix'),
            ('Wake Up Sid', 'Ranbir Kapoor', 'Konkona Sen Sharma', 'Comedy', 7.6, 'Hulu'),
            ('Rockstar', 'Ranbir Kapoor', 'Nargis Fakhri', 'Music', 7.7, 'Amazon Prime'),
            ('Sanju', 'Ranbir Kapoor', 'Manisha Koirala', 'Biography', 7.7, 'Netflix'),
            ('Gully Boy', 'Ranveer Singh', 'Alia Bhatt', 'Drama', 8.1, 'Amazon Prime'),
            ('Dil Dhadakne Do', 'Ranveer Singh', 'Priyanka Chopra', 'Drama', 6.7, 'Netflix'),
            ('Bajrangi Bhaijaan', 'Salman Khan', 'Kareena Kapoor', 'Drama', 8.0, 'Amazon Prime'),
            ('Sultan', 'Salman Khan', 'Anushka Sharma', 'Action', 7.0, 'Amazon Prime'),
            ('Tiger Zinda Hai', 'Salman Khan', 'Katrina Kaif', 'Action', 6.0, 'Netflix'),
            ('Dabangg', 'Salman Khan', 'Sonakshi Sinha', 'Action', 6.3, 'Hulu'),
            ('Bharat', 'Salman Khan', 'Katrina Kaif', 'Action', 5.3, 'Amazon Prime'),
            ('Kabhi Haan Kabhi Naa', 'Shah Rukh Khan', 'Suchitra Krishnamoorthi', 'Comedy', 7.8, 'Netflix'),
            ('Andaz Apna Apna', 'Aamir Khan', 'Raveena Tandon', 'Comedy', 8.2, 'Amazon Prime'),
            ('Dil Chahta Hai', 'Aamir Khan', 'Preity Zinta', 'Drama', 8.1, 'Amazon Prime'),
            ('Lagaan', 'Aamir Khan', 'Gracy Singh', 'Drama', 8.1, 'Netflix'),
            ('Mughal-E-Azam', 'Prithviraj Kapoor', 'Madhubala', 'Drama', 8.2, 'Amazon Prime'),
            ('Sholay', 'Dharmendra', 'Hema Malini', 'Action', 8.2, 'Netflix'),
            ('Chak De! India', 'Shah Rukh Khan', 'Vidya Malvade', 'Drama', 8.2, 'Amazon Prime'),
            ('Dangal', 'Aamir Khan', 'Sakshi Tanwar', 'Biography', 8.4, 'Netflix'),
            ('PK', 'Aamir Khan', 'Anushka Sharma', 'Comedy', 8.1, 'Amazon Prime'),
            ('Kapoor & Sons', 'Sidharth Malhotra', 'Alia Bhatt', 'Drama', 7.7, 'Netflix'),
            ('Piku', 'Irrfan Khan', 'Deepika Padukone', 'Drama', 7.6, 'Amazon Prime'),
            ('Badhaai Ho', 'Ayushmann Khurrana', 'Sanya Malhotra', 'Comedy', 8.0, 'Netflix'),
            ('Article 15', 'Ayushmann Khurrana', 'Isha Talwar', 'Crime', 8.1, 'Amazon Prime'),    
        ]
        cursor.executemany('''
            INSERT INTO movies (title, actor, actress, genre, imdb_rating, ott)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', movies_data)
        conn.commit()
        conn.close()
        
    def create_combobox(self, parent, values, row, column):
        combobox = ttk.Combobox(parent, textvariable=tk.StringVar(), state='readonly', values=values)
        combobox.set('All')
        combobox.grid(row=row, column=column, padx=10, pady=10)
        return combobox

    def fetch_recommendations(self):
        actor = self.actors.get()
        actress = self.actresses.get()
        genre = self.genres.get()
        imdb_rating = self.imdb_rating.get()
        conn = sqlite3.connect('movies_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT title, actor, actress, genre, imdb_rating, ott
            FROM movies
            WHERE (actor=? OR ?='All')
            AND (actress=? OR ?='All')
            AND (genre=? OR ?='All')
            AND (imdb_rating >= ? OR ?='All')
            ORDER BY imdb_rating DESC  -- Order by IMDb rating from best to worst
        ''', (actor, actor, actress, actress, genre, genre, imdb_rating, imdb_rating))

        movies = cursor.fetchall()
        conn.close()
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        if not movies:
            message = "Sorry, no movies found.\nTry changing some conditions."
            self.text_widget.insert(tk.END, message)
        else:
            for movie in movies:
                formatted_movie = (
                    f"Title: {movie[0]}\nActor: {movie[1]}\nActress: {movie[2]}\nGenre: {movie[3]}\nIMDb Rating: {movie[4]}\nOTT: {movie[5]}\n\n"
                )
                self.text_widget.insert(tk.END, formatted_movie)
        self.text_widget.config(state=tk.DISABLED)

    def get_actor_names(self):
        conn = sqlite3.connect('movies_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT actor FROM movies')
        actors = [row[0] for row in cursor.fetchall()]
        conn.close()
        return ['All'] + actors

    def get_actress_names(self):
        conn = sqlite3.connect('movies_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT actress FROM movies')
        actresses = [row[0] for row in cursor.fetchall()]
        conn.close()
        return ['All'] + actresses

    def get_genre_names(self):
        conn = sqlite3.connect('movies_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT genre FROM movies')
        genres = [row[0] for row in cursor.fetchall()]
        conn.close()
        return ['All'] + genres


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommendationSystem(root)
    root.mainloop()
    
