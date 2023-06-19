import tkinter as tk
import requests


def get_quote():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': '0H882fFH6xjpapteI9nCrg==6EV5OtG7zk8Jv7rH'})
    if response.status_code == requests.codes.ok:
        quote = response.json()[0]['quote']
        author = response.json()[0]['author']
        quote_label.config(text=quote, fg="#333333")
        author_label.config(text="- " + author, fg="#555555")
    else:
        quote_label.config(text="Error: " + str(response.status_code), fg="#FF0000")


window = tk.Tk()
window.title("Quote App")
window.geometry("936x720")
window.configure(bg="#FDF5E6")


quote_label = tk.Label(window, text="Click the button to get a quote", font=("Arial", 14), bg="#FDF5E6", fg="#333333")
quote_label.pack(pady=10)


author_label = tk.Label(window, text="", font=("Arial", 12, "italic"), bg="#FDF5E6", fg="#555555")
author_label.pack(pady=5)


joke_button = tk.Button(window, text="Get Random Joke", highlightthickness=1, command=get_quote)
joke_button.pack(pady=10)


window.mainloop()
