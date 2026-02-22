# Copyright (c) 2025 Darshan
# License: MIT

from datetime import datetime, date
from typing import List, Dict
import csv

CSV_FILE = "2025.csv"


def read_data(filename: str) -> List[Dict]:
    """Reads CSV file and returns a list of dicts with datetime, consumption, production, temperature."""
    data: List[Dict] = []

    with open(filename, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            timestamp_str = row[0]
            consumption_str = row[1]
            production_str = row[2]
            temperature_str = row[3]

            timestamp = datetime.fromisoformat(timestamp_str)
            consumption = float(consumption_str.replace(",", "."))
            production = float(production_str.replace(",", "."))
            temperature = float(temperature_str.replace(",", "."))

            data.append({
                "datetime": timestamp,
                "date": timestamp.date(),
                "consumption": consumption,
                "production": production,
                "temperature": temperature
            })
    return data


def format_date(d: date) -> str:
    """Formats a date as dd.mm.yyyy."""
    return f"{d.day}.{d.month}.{d.year}"


def format_number(value: float) -> str:
    """Formats a number with two decimals and comma as decimal separator."""
    return f"{value:.2f}".replace(".", ",")


def show_main_menu() -> str:
    """Displays the main menu and returns the user's choice."""
    print("\nChoose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary")
    print("3) Full year 2025 summary")
    print("4) Exit")
    return input("Enter choice: ").strip()


def show_post_menu() -> str:
    """Displays the post-report menu and returns the user's choice."""
    print("\nWhat would you like to do next?")
    print("1) Write report to report.txt")
    print("2) Create a new report")
    print("3) Exit")
    return input("Enter choice: ").strip()


def create_daily_report(data: List[Dict]) -> List[str]:
    """Builds a daily summary report for a user-specified date range."""
    start_str = input("Enter start date (dd.mm.yyyy): ")
    end_str = input("Enter end date (dd.mm.yyyy): ")
    start_date = datetime.strptime(start_str, "%d.%m.%Y").date()
    end_date = datetime.strptime(end_str, "%d.%m.%Y").date()

    total_consumption = 0.0
    total_production = 0.0
    temperatures: List[float] = []

    for entry in data:
        if start_date <= entry["date"] <= end_date:
            total_consumption += entry["consumption"]
            total_production += entry["production"]
            temperatures.append(entry["temperature"])

    avg_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0

    lines = [
        "-----------------------------------------------------",
        f"Report for the period {format_date(start_date)}–{format_date(end_date)}",
        f"- Total consumption: {format_number(total_consumption)} kWh",
        f"- Total production: {format_number(total_production)} kWh",
        f"- Average temperature: {format_number(avg_temperature)} °C"
    ]
    return lines


def create_monthly_report(data: List[Dict]) -> List[str]:
    """Builds a monthly summary report for a user-specified month."""
    month = int(input("Enter month number (1–12): "))

    total_consumption = 0.0
    total_production = 0.0
    temperatures: List[float] = []

    for entry in data:
        if entry["date"].month == month:
            total_consumption += entry["consumption"]
            total_production += entry["production"]
            temperatures.append(entry["temperature"])

    avg_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0
    month_name = date(2025, month, 1).strftime("%B")

    lines = [
        "-----------------------------------------------------",
        f"Report for the month: {month_name}",
        f"- Total consumption: {format_number(total_consumption)} kWh",
        f"- Total production: {format_number(total_production)} kWh",
        f"- Average temperature: {format_number(avg_temperature)} °C"
    ]
    return lines


def create_yearly_report(data: List[Dict]) -> List[str]:
    """Builds a full-year summary report for 2025."""
    total_consumption = sum(entry["consumption"] for entry in data)
    total_production = sum(entry["production"] for entry in data)
    temperatures = [entry["temperature"] for entry in data]
    avg_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0

    lines = [
        "-----------------------------------------------------",
        "Report for the year: 2025",
        f"- Total consumption: {format_number(total_consumption)} kWh",
        f"- Total production: {format_number(total_production)} kWh",
        f"- Average temperature: {format_number(avg_temperature)} °C"
    ]
    return lines


def print_report_to_console(lines: List[str]) -> None:
    """Prints report lines to the console."""
    for line in lines:
        print(line)


def write_report_to_file(lines: List[str]) -> None:
    """Writes report lines to report.txt."""
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
    print("Report written to report.txt")


def main() -> None:
    """Main program controlling menu and report generation."""
    data = read_data(CSV_FILE)
    print(f"CSV file '{CSV_FILE}' loaded. {len(data)} rows processed.")

    while True:
        choice = show_main_menu()

        if choice == "1":
            report = create_daily_report(data)
        elif choice == "2":
            report = create_monthly_report(data)
        elif choice == "3":
            report = create_yearly_report(data)
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        print_report_to_console(report)

        while True:
            post_choice = show_post_menu()
            if post_choice == "1":
                write_report_to_file(report)
            elif post_choice == "2":
                break
            elif post_choice == "3":
                print("Program ended.")
                return
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()