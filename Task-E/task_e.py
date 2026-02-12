import pandas as pd

# list of CSV files for weeks
files = ["week40.csv", "week41.csv", "week42.csv"]

for file in files:
    df = pd.read_csv(file, parse_dates=['timestamp'])

    print(f"\n--- Data from {file} ---\n")

    # print header
    print("Time   Cons1  Cons2  Cons3")
    
    for idx, row in df.iterrows():
        cons = row[['consumption1', 'consumption2', 'consumption3']].tolist()
        time = row['timestamp'].strftime("%H:%M")
        print(f"{time}   {cons[0]:>6.2f} {cons[1]:>6.2f} {cons[2]:>6.2f}")

    # calculate weekly averages
    avg = df[['consumption1', 'consumption2', 'consumption3']].mean().tolist()
    print(f"\nWeekly average: {avg[0]:.2f}, {avg[1]:.2f}, {avg[2]:.2f}\n")
