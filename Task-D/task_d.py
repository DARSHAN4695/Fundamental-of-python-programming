from datetime import datetime, date
from typing import List, Dict

def read_data(filename: str) -> List[Dict]:
    """
    Reads the CSV file and returns a list of dictionaries with proper types.
    """
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)  # skip header
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split(",")
            ts_str, c1, c2, c3, p1, p2, p3 = parts
            dt = datetime.fromisoformat(ts_str)
            row = {
                "date": dt.date(),
                "consumption": [int(c1)/1000, int(c2)/1000, int(c3)/1000],
                "production": [int(p1)/1000, int(p2)/1000, int(p3)/1000]
            }
            data.append(row)
    return data

def main() -> None:
    """
    Main function: reads data, computes daily totals, and prints the report.
    """
    data = read_data("week42.csv")
    
    # Group by date
    daily = {}
    for row in data:
        d = row["date"]
        if d not in daily:
            daily[d] = {"consumption":[0,0,0], "production":[0,0,0]}
        for i in range(3):
            daily[d]["consumption"][i] += row["consumption"][i]
            daily[d]["production"][i] += row["production"][i]

    weekdays_fi = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    print("Week 42 electricity consumption and production (kWh, by phase)\n")
    print(f"{'Day':<12}{'Date':<12}{'Consumption [kWh]':<30}{'Production [kWh]'}")
    print(f"{'':<12}{'(dd.mm.yyyy)':<12}{'v1':>6}{'v2':>6}{'v3':>6}{'':6}{'v1':>6}{'v2':>6}{'v3':>6}")
    print("-"*70)
    
    for d in sorted(daily.keys()):
        weekday_name = weekdays_fi[d.weekday()]
        date_str = d.strftime("%d.%m.%Y")
        cons = [f"{v:.2f}".replace(".", ",") for v in daily[d]["consumption"]]
        prod = [f"{v:.2f}".replace(".", ",") for v in daily[d]["production"]]
        print(f"{weekday_name:<12}{date_str:<12}{cons[0]:>6}{cons[1]:>6}{cons[2]:>6}      {prod[0]:>6}{prod[1]:>6}{prod[2]:>6}")

if __name__ == "__main__":
    main()
