import datetime
import random
import csv


def menu(title, options):
    while True:
        print("\n" + title)
        for key in options:
            print(f"{key}. {options[key]}")

        choice = input("Enter choice: ").strip()

        if choice in options:
            return options[choice]
        print("Invalid choice. Try again.")


def select_city():
    return menu("Select City", {
        "1": "Chennai",
        "2": "Mumbai",
        "3": "Bangalore"
    })


def select_language():
    return menu("Select Language", {
        "1": "Tamil",
        "2": "English",
        "3": "Hindi"
    })


MOVIES = {
    "Tamil": {
        "Action": ["Master", "Karnan", "Teddy"],
        "Family": ["Doctor", "Annaatthe"],
        "Horror": ["Maya", "Aranmanai"],
        "SciFi": ["24", "Enthiran"]
    },
    "English": {
        "Action": ["Venom", "Tenet"],
        "Family": ["Shrek", "Onward"],
        "Horror": ["The Conjuring", "The Nun"],
        "SciFi": ["Inception", "Interstellar"]
    },
    "Hindi": {
        "Action": ["URI", "Radhe"],
        "Family": ["English Vinglish", "The Lunchbox"],
        "Horror": ["Bulbbul"],
        "SciFi": ["Mission Mangal"]
    }
}


def select_genre(language):
    genre_list = {}
    i = 1
    for genre in MOVIES[language]:
        genre_list[str(i)] = genre
        i += 1

    return menu("Select Genre", genre_list)


def select_movie(language, genre):
    movie_list = {}
    for i in range(len(MOVIES[language][genre])):
        movie_list[str(i + 1)] = MOVIES[language][genre][i]

    return menu("Select Movie", movie_list)


def select_theatre():
    return menu("Select Theatre", {
        "1": "INOX",
        "2": "ICON",
        "3": "FOX"
    })


def select_screen():
    return menu("Select Screen", {
        "1": "Screen 1",
        "2": "Screen 2",
        "3": "Screen 3"
    })


def select_show_time():
    timings = {
        "1": "10:00",
        "2": "13:10",
        "3": "16:20",
        "4": "19:30"
    }

    time_selected = menu("Select Show Time", timings)
    today = datetime.datetime.now()

    try:
        day = int(input("Enter day (dd): "))
        month = int(input("Enter month (mm): "))
        year = today.year

        show_time = datetime.datetime.strptime(
            f"{day}/{month}/{year} {time_selected}",
            "%d/%m/%Y %H:%M"
        )

        if show_time < today:
            print("Show time already passed.")
            return select_show_time()

        return show_time

    except ValueError:
        print("Invalid date format.")
        return select_show_time()


def payment():
    seats = int(input("Number of seats: "))
    total = seats * 300

    print(f"Total amount: Rs. {total}")

    mode = menu("Payment Method", {
        "1": "Cash",
        "2": "Card"
    })

    if mode == "Card":
        input("Enter card number: ")
        input("Enter CVV: ")
        otp = random.randint(1000, 9999)
        print("OTP:", otp)
        input("Enter OTP: ")
        print("Payment successful")

    return seats, total


# -------- MAIN FLOW --------

print("\nMOVIE TICKET BOOKING SYSTEM")

city = select_city()
language = select_language()
genre = select_genre(language)
movie = select_movie(language, genre)
theatre = select_theatre()
screen = select_screen()
show_time = select_show_time()
seats, amount = payment()

print("\n------ TICKET DETAILS ------")
print("City:", city)
print("Language:", language)
print("Movie:", movie)
print("Theatre:", theatre)
print("Screen:", screen)
print("Show Time:", show_time)
print("Seats:", seats)
print("Amount Paid:", amount)
print("----------------------------")

with open("tickets.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        city, language, movie, theatre,
        screen, show_time, seats, amount
    ])

print("Ticket stored successfully.")