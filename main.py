import datetime
import random
import csv


# UTILITY FUNCTION

def choose_option(title, options):
    while True:
        print(f"\n{title}")
        for key, value in options.items():
            print(f"{key}. {value}")

        choice = input("Enter choice: ")

        if choice in options:
            return options[choice]
        else:
            print("❌ Wrong choice. Try again.")


# CITY

def choose_city():
    cities = {
        "1": "Chennai",
        "2": "Mumbai",
        "3": "Bangalore"
    }
    return choose_option("Choose City", cities)



# LANGUAGE

def choose_language():
    languages = {
        "1": "Tamil",
        "2": "English",
        "3": "Hindi"
    }
    return choose_option("Choose Language", languages)



# GENRE & MOVIES

movies = {
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


def choose_genre(language):
    genres = {str(i+1): g for i, g in enumerate(movies[language].keys())}
    return choose_option("Choose Genre", genres)


def choose_movie(language, genre):
    movie_list = movies[language][genre]
    options = {str(i+1): movie for i, movie in enumerate(movie_list)}
    return choose_option("Choose Movie", options)



# THEATRE & SCREEN

def choose_theatre():
    theatres = {
        "1": "Inox Theatre",
        "2": "Icon Theatre",
        "3": "Fox Theatre"
    }
    return choose_option("Choose Theatre", theatres)


def choose_screen():
    screens = {
        "1": "Screen 1",
        "2": "Screen 2",
        "3": "Screen 3"
    }
    return choose_option("Choose Screen", screens)



# TIME SLOT

def choose_time():
    times = {
        "1": "10:00",
        "2": "13:10",
        "3": "16:20",
        "4": "19:30"
    }
    chosen = choose_option("Choose Time Slot", times)

    today = datetime.datetime.now()
    date = int(input("Enter date (dd): "))
    month = int(input("Enter month (mm): "))
    year = today.year

    booking_time = datetime.datetime.strptime(
        f"{date}/{month}/{year} {chosen}",
        "%d/%m/%Y %H:%M"
    )

    if booking_time < today:
        print("❌ Slot expired. Choose again.")
        return choose_time()

    return booking_time



# PAYMENT

def payment():
    seats = int(input("\nHow many seats? "))
    total = seats * 300

    print("Total Cost: Rs.", total)

    mode = choose_option(
        "Choose Payment Method",
        {"1": "Cash", "2": "Card"}
    )

    if mode == "Card":
        card = input("Enter 12-digit card number: ")
        cvv = input("Enter CVV: ")
        otp = random.randint(1000, 9999)
        print("OTP:", otp)
        print("Transaction Successful ✅")

    return seats, total



# MAIN FLOW

print("\n🎬 WELCOME TO MOVIE TICKET BOOKING 🎬")

city = choose_city()
language = choose_language()
genre = choose_genre(language)
movie = choose_movie(language, genre)
theatre = choose_theatre()
screen = choose_screen()
time_slot = choose_time()
seats, total_cost = payment()


# TICKET PRINT

print("\n🎟️ TICKET DETAILS 🎟️")
print("----------------------------------")
print("City:", city)
print("Language:", language)
print("Movie:", movie)
print("Theatre:", theatre)
print("Screen:", screen)
print("Time:", time_slot)
print("Seats:", seats)
print("Amount Paid: Rs.", total_cost)
print("----------------------------------")
print("ENJOY YOUR MOVIE 🍿")


# STORE TO CSV

with open("tickets.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Language", "Movie", "Theatre", "Screen", "Time", "Seats", "Cost"])
    writer.writerow([city, language, movie, theatre, screen, time_slot, seats, total_cost])
