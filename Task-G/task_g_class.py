from datetime import datetime


class Reservation:
    def __init__(self, reservation_id, name, email, phone,
                 date, time, duration, price,
                 confirmed, resource, created):

        self.reservation_id = reservation_id
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date
        self.time = time
        self.duration = duration
        self.price = price
        self.confirmed = confirmed
        self.resource = resource
        self.created = created

    def is_confirmed(self) -> bool:
        return self.confirmed

    def is_long(self) -> bool:
        return self.duration >= 3

    def total_price(self) -> float:
        return self.duration * self.price


def convert_reservation(data: list[str]) -> Reservation:
    return Reservation(
        reservation_id=int(data[0]),
        name=data[1],
        email=data[2],
        phone=data[3],
        date=datetime.strptime(data[4], "%Y-%m-%d").date(),
        time=datetime.strptime(data[5], "%H:%M:%S").time(),
        duration=int(data[6]),
        price=float(data[7]),
        confirmed=data[8].strip().lower() == "true",
        resource=data[9],
        created=datetime.strptime(data[10], "%Y-%m-%d %H:%M:%S")
    )


def fetch_reservations(filename: str) -> list[Reservation]:
    reservations = []

    with open(filename, "r", encoding="utf-8") as file:
        next(file)

        for line in file:
            data = line.strip().split("|")
            reservation = convert_reservation(data)
            reservations.append(reservation)

    return reservations


def print_confirmed(reservations: list[Reservation]) -> None:
    print("Confirmed reservations:")
    for reservation in reservations:
        if reservation.is_confirmed():
            print(
                f"- {reservation.name}, "
                f"{reservation.resource}, "
                f"{reservation.date.strftime('%d.%m.%Y')} at "
                f"{reservation.time.strftime('%H.%M')}"
            )


def print_long_reservations(reservations: list[Reservation]) -> None:
    print("\nLong reservations (>= 3 hours):")
    for reservation in reservations:
        if reservation.is_long():
            print(
                f"- {reservation.name} ({reservation.duration} hours)"
            )


def calculate_total_revenue(reservations: list[Reservation]) -> float:
    total = 0
    for reservation in reservations:
        if reservation.is_confirmed():
            total += reservation.total_price()
    return total


def main():
    reservations = fetch_reservations("reservations.txt")

    print_confirmed(reservations)
    print_long_reservations(reservations)

    total_revenue = calculate_total_revenue(reservations)
    print(f"\nTotal revenue from confirmed reservations: {total_revenue:.2f} €")


if __name__ == "__main__":
    main()