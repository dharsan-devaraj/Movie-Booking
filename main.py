import datetime
import random
import csv


def menu(title, options):
    while True:
        print("\n" + "=" * 35)
        print(title.upper())
        print("=" * 35)

        for key in options:
            print(f"{key}. {options[key]}")

        choice = input("\nEnter choice ➤ ").strip()

        if choice in options:
            return options[choice]

        print("❌ Invalid choice. Please try again.")


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
        day = int(input("Enter day (DD): "))
        month = int(input("Enter month (MM): "))
        year = today.year

        show_time = datetime.datetime.strptime(
            f"{day}/{month}/{year} {time_selected}",
            "%d/%m/%Y %H:%M"
        )

        if show_time < today:
            print("⚠️ Show time already passed.")
            return select_show_time()

        return show_time

    except ValueError:
        print("❌ Invalid date.")
        return select_show_time()


def select_seat_type():
    return menu("Select Seat Type", {
        "1": "Silver",
        "2": "Gold",
        "3": "Platinum"
    })


def payment(seat_type):
    while True:
        seats = int(input("Number of seats: "))
        if seats > 0:
            break
        print("❌ Seats must be greater than 0")

    price_chart = {
        "Silver": 200,
        "Gold": 300,
        "Platinum": 450
    }

    price_per_seat = price_chart[seat_type]
    total = seats * price_per_seat

    if seats >= 5:
        discount = total * 0.10
        total -= discount
        print(f"🎉 Bulk Booking Discount Applied: ₹{int(discount)}")

    print(f"\n💺 Seat Type: {seat_type}")
    print(f"💰 Ticket Price: ₹{price_per_seat}")
    print(f"💳 Total Amount: ₹{int(total)}")

    mode = menu("Payment Method", {
        "1": "Cash",
        "2": "Card"
    })

    if mode == "Card":
        input("Enter card number: ")
        input("Enter CVV: ")
        otp = random.randint(1000, 9999)
        print("📩 OTP sent:", otp)

        user_otp = input("Enter OTP: ")
        if user_otp != str(otp):
            print("❌ Invalid OTP. Payment Failed.")
            return payment(seat_type)

        print("✅ Payment Successful!")

    return seats, int(total)


# -------- MAIN FLOW --------

print("\n🎬 WELCOME TO MOVIE TICKET BOOKING SYSTEM 🎬")

ticket_id = random.randint(100000, 999999)

city = select_city()
language = select_language()
genre = select_genre(language)
movie = select_movie(language, genre)
theatre = select_theatre()
screen = select_screen()
show_time = select_show_time()
seat_type = select_seat_type()
seats, amount = payment(seat_type)

print("\n" + "=" * 45)
print("🎟️ TICKET CONFIRMATION")
print("=" * 45)
print("Ticket ID  :", ticket_id)
print("City       :", city)
print("Language   :", language)
print("Movie      :", movie)
print("Theatre    :", theatre)
print("Screen     :", screen)
print("Seat Type  :", seat_type)
print("Show Time  :", show_time.strftime("%d-%m-%Y %H:%M"))
print("Seats      :", seats)
print("Amount Paid: ₹", amount)
print("=" * 45)

with open("tickets.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        ticket_id, city, language, movie,
        theatre, screen, seat_type,
        show_time.strftime("%d-%m-%Y %H:%M"),
        seats, amount,
        datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    ])

print("📁 Ticket saved successfully!")
