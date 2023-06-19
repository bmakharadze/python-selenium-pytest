import requests
import tkinter as tk
from PIL import ImageTk, Image
import io

api_key = "3fd2be6f0c70a2a598f084ddfb75487c"
api_url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}&page=1"


def get_movies():
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        movie_data = response.json()
        movies = movie_data["results"]

        canvas = tk.Canvas(window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(window, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        poster_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=poster_frame, anchor=tk.NW)

        for movie in movies:
            title = movie["title"]
            vote_average = movie["vote_average"]
            poster_url = f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{movie['poster_path']}"

            response = requests.get(poster_url)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((200, 300))  # Resize the image if needed
            photo = ImageTk.PhotoImage(image)

            poster_label = tk.Label(poster_frame, image=photo)
            poster_label.image = photo
            poster_label.pack(pady=10)

            title_label = tk.Label(poster_frame, text=title)
            title_label.pack()
            vote_average = tk.Label(poster_frame, text=vote_average)
            vote_average.pack()

        poster_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    else:
        error_label = tk.Label(window, text=f"Error: {response.status_code}")
        error_label.pack()


window = tk.Tk()
window.title("Movie App")
window.geometry("800x600")

window.eval('tk::PlaceWindow . center')

get_movies()

window.mainloop()
