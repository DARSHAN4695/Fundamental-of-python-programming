# task_a.py
# Reads a reservation from reservations.txt and prints formatted info

from datetime import datetime

def main():
    # File path
    filename = "reservations.txt"

    # Read the reservation line
    with open(filename, "r", encoding="utf-8") as f:
        line = f.read().strip()

    # Split the line into fields
    reservation = line.split('|')

    # Convert data types
    reservation_number = int(reservation[0])
    booker = reservation[1]
    date = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    start_time = datetime.strptime(reservation[3], "%H:%M").time()
    number_of_hours = int(reservation[4])
    hourly_price = float(reservation[5])
    paid = reservation[6] == "True"
    location = reservation[7]
    phone = reservation[8]
    email = reservation[9]

    # Compute total price
    total_price = number_of_hours * hourly_price

    # Format date and time for Finnish style
    finnish_date = date.strftime("%d.%m.%Y")
    finnish_time = start_time.strftime("%H.%M")
    finnish_hourly_price = f"{hourly_price:,.2f}".replace('.', ',')
    finnish_total_price = f"{total_price:,.2f}".replace('.', ',')

    # Print formatted output
    print(f"Reservation number: {reservation_number}")
    print(f"Booker: {booker}")
    print(f"Date: {finnish_date}")
    print(f"Start time: {finnish_time}")
    print(f"Number of hours: {number_of_hours}")
    print(f"Hourly price: {finnish_hourly_price} €")
    print(f"Total price: {finnish_total_price} €")
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()