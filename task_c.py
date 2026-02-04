from datetime import datetime

HEADERS = [
    "reservationId",
    "name",
    "email",
    "phone",
    "reservationDate",
    "reservationTime",
    "durationHours",
    "price",
    "confirmed",
    "reservedResource",
    "createdAt",
]


def convert_reservation_data(row):
    """
    Convert each reservation field to the correct data type.
    Strips whitespace/newlines to avoid parsing errors.
    """
    row = [x.strip() for x in row]  # Remove spaces/newlines

    return [
        int(row[0]),  # reservationId
        row[1],       # name
        row[2],       # email
        row[3],       # phone
        datetime.strptime(row[4], "%Y-%m-%d").date(),  # reservationDate
        datetime.strptime(row[5], "%H:%M").time(),     # reservationTime
        int(row[6]),  # durationHours
        float(row[7]),# price
        row[8].strip().lower() == "true",  # confirmed -> FIXED
        row[9],       # reservedResource
        datetime.strptime(row[10], "%Y-%m-%d %H:%M:%S")  # createdAt
    ]


def fetch_reservations(reservation_file):
    """
    Read reservations from file and convert them.
    """
    reservations = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.split("|")
            reservations.append(convert_reservation_data(fields))
    return reservations


# ---------------- PART B FUNCTIONS ----------------

def confirmed_reservations(reservations):
    print("1) Confirmed Reservations")
    for r in reservations:
        if r[8]:  # confirmed == True
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {r[9]}, {date_str} at {time_str}")
    print()


def long_reservations(reservations):
    print("2) Long Reservations (≥ 3 h)")
    for r in reservations:
        if r[6] >= 3:  # durationHours >= 3
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {date_str} at {time_str}, duration {r[6]} h, {r[9]}")
    print()


def confirmation_statuses(reservations):
    print("3) Reservation Confirmation Status")
    for r in reservations:
        status = "Confirmed" if r[8] else "NOT Confirmed"
        print(f"{r[1]} → {status}")
    print()


def confirmation_summary(reservations):
    confirmed_count = sum(1 for r in reservations if r[8])
    not_confirmed_count = len(reservations) - confirmed_count
    print("4) Confirmation Summary")
    print(f"- Confirmed reservations: {confirmed_count} pcs")
    print(f"- Not confirmed reservations: {not_confirmed_count} pcs")
    print()


def total_revenue(reservations):
    total = sum(r[7] * r[6] for r in reservations if r[8])  # price * duration for confirmed
    amount_str = f"{total:.2f}".replace(".", ",")
    print("5) Total Revenue from Confirmed Reservations")
    print(f"Total revenue from confirmed reservations: {amount_str} €")
    print()


# ---------------- MAIN ----------------

def main():
    reservations = fetch_reservations("reservations.txt")

    # PART B outputs
    confirmed_reservations(reservations)
    long_reservations(reservations)
    confirmation_statuses(reservations)
    confirmation_summary(reservations)
    total_revenue(reservations)

if __name__ == "__main__":
    main()
