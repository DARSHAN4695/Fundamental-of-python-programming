from datetime import datetime

# -----------------------------
# Functions for each field
# -----------------------------

def print_reservation_number(reservation: list):
    """Print the reservation number"""
    print(f"Reservation number: {reservation[0]}")

def print_booker(reservation: list):
    """Print the booker's name"""
    print(f"Booker: {reservation[1]}")

def print_date(reservation: list):
    """Print the reservation date in dd.mm.yyyy format"""
    date_obj = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    print(f"Date: {date_obj.strftime('%d.%m.%Y')}")

def print_start_time(reservation: list):
    """Print the start time in hh.mm format"""
    time_obj = datetime.strptime(reservation[3], "%H:%M").time()
    print(f"Start time: {time_obj.strftime('%H.%M')}")

def print_hours(reservation: list):
    """Print number of hours"""
    print(f"Number of hours: {reservation[4]}")

def print_hourly_rate(reservation: list):
    """Print the hourly rate in € with comma"""
    price = float(reservation[5])
    print(f"Hourly price: {price:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

def print_total_price(reservation: list):
    """Print total price = hours * hourly rate"""
    total = int(reservation[4]) * float(reservation[5])
    print(f"Total price: {total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

def print_paid(reservation: list):
    """Print Yes/No for paid status"""
    paid = reservation[6].strip().lower() == "true"
    print(f"Paid: {'Yes' if paid else 'No'}")

def print_venue(reservation: list):
    """Print the resource/location"""
    print(f"Location: {reservation[7]}")

def print_phone(reservation: list):
    """Print phone number"""
    print(f"Phone: {reservation[8]}")

def print_email(reservation: list):
    """Print email"""
    print(f"Email: {reservation[9]}")

# -----------------------------
# Main program
# -----------------------------

def main():
    # Open the reservations file
    with open("reservations.txt", "r") as file:
        for line in file:
            # Split the line by |
            reservation = line.strip().split("|")

            # Call all print functions
            print_reservation_number(reservation)
            print_booker(reservation)
            print_date(reservation)
            print_start_time(reservation)
            print_hours(reservation)
            print_hourly_rate(reservation)
            print_total_price(reservation)
            print_paid(reservation)
            print_venue(reservation)
            print_phone(reservation)
            print_email(reservation)
            print("-" * 40)  # separator between reservations

# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    main()