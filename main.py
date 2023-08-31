import extract
import transform
import extract
import datetime
import os

def main():
		start_date = datetime.datetime(2020, 12, 12, 11)
		end_date = start_date + datetime.timedelta(hours=3)
		
		while start_date <= end_date:
				start_date += datetime.timedelta(hours=1)
				date_str = start_date.strftime("%Y-%m-%d-%H")
				if os.path.exists(f"./csv/insights.github_events.{date_str.replace('-', '')}.csv"):
					print(date_str, " already exists, skipping...")
					continue
				else:
					print(date_str, "Downloading archive for: ", date_str)


if __name__ == "__main__":
    main()
