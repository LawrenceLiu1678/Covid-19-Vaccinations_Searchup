import urllib.request, json
from datetime import datetime, timedelta

VACCINATION_DATA = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json"


def main():
    current_time()
    data = import_vaccination_data()
    search_data(data)


def current_time():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print("The current time is:", time)


def search_data(data):
    # All variables used to store information

    stored_country_abbreviation = ""
    stored_country = ""

    store_date = ""
    store_total_vaccinations = ""
    store_people_vaccinated = ""
    store_people_fully_vaccinated = ""
    store_daily_vaccinations = ""

    today_world_total = 0
    world_total_result = 0
    # ---------------------------------------------------------------------

    # grabs the inputs from the user for the country abbreviation and dates
    while True:

        print("")
        searched_country = searching_country()
        if searched_country == "":
            break

        """
        [
            {
                "country": "Afghanistan",
                "iso_code": "AFG",
                "data": [
                  {
                    "date": "2021-02-22",
                    "total_vaccinations": 0,
                    "people_vaccinated": 0,
                    "total_vaccinations_per_hundred": 0.0,
                    "people_vaccinated_per_hundred": 0.0
                  },
        
        1. Open up the initial information in the primary list                                  (for info in data)
        2. Open up the dictionary using the keys and values                                     (for key, value in info.items())
        3. Open up the second list                                                              (for data_info in info["data"])
        4. Open up the second dictionary                                                        (for key_two, value_two in data_info.items())
        5. Store all values that are related to the information regarding to this program
        6. Print results                                                                        (print_data_result_messages function)
        """
        for info in data:
            for key, value in info.items():
                if value == searched_country:
                    stored_country_abbreviation = value
                    stored_country = info["country"]

                    print("You've inputted {}, which is the abbreviation of {}".format(stored_country_abbreviation,
                                                                                       stored_country))

                    # stores the date in a variable
                    searched_time = searching_date()

                    # provides an empty line
                    print("")

                    for data_info in info["data"]:
                        for key_two, value_two in data_info.items():

                            # searches for a date to match with the user input
                            if value_two == searched_time:
                                """
                                Old Code
                                ________
                                
                                store_date = data_info["date"]
                                store_total_vaccinations = data_info["total_vaccinations"]
                                store_people_vaccinated = data_info["people_vaccinated"]
                                store_people_fully_vaccinated = data_info["people_fully_vaccinated"]
                                store_daily_vaccinations = data_info["daily_vaccinations"]
                                """

                                store_date = data_info.get("date")
                                store_total_vaccinations = data_info.get("total_vaccinations")
                                store_people_vaccinated = data_info.get("people_vaccinated")
                                store_people_fully_vaccinated = data_info.get("people_fully_vaccinated")
                                store_daily_vaccinations = data_info.get("daily_vaccinations")

                                print_data_result_messages(store_date, store_total_vaccinations,
                                                           store_people_vaccinated, store_people_fully_vaccinated,
                                                           store_daily_vaccinations)

                            # goes one day back to grab the latest results
                            elif searched_time.capitalize() == "Yesterday":
                                searched_time = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")

                                if value_two == searched_time:
                                    store_date = data_info.get("date")
                                    store_total_vaccinations = data_info.get("total_vaccinations")
                                    store_people_vaccinated = data_info.get("people_vaccinated")
                                    store_people_fully_vaccinated = data_info.get("people_fully_vaccinated")
                                    store_daily_vaccinations = data_info.get("daily_vaccinations")

                                    print_data_result_messages(store_date, store_total_vaccinations,
                                                               store_people_vaccinated, store_people_fully_vaccinated,
                                                               store_daily_vaccinations)


# prints out the results
def print_data_result_messages(store_date, store_total_vaccinations, store_people_vaccinated,
                               store_people_fully_vaccinated, store_daily_vaccinations):
    print("The date you inputted is: {}".format(store_date))
    print("The total amount of vaccinations up to this date is: {:,}".format(store_total_vaccinations))
    print("The total amount of people that have been vaccinated is: {:,}".format(store_people_vaccinated))
    print("The current amount of people FULLY vaccinated is: {:,}".format(store_people_fully_vaccinated))
    print("The current daily amount of vaccinations administered is: {:,}".format(store_daily_vaccinations))


# searches the country inputted by the user
def searching_country():
    user_input_country = input("What country would you like to search for? (3 letter abbreviations only or press "
                               "ENTER to end the program) ")
    return user_input_country.upper()


# searches the date inputted by the user
def searching_date():
    user_input_date = input("What date would you like to search for? (format: YYYY-MM-DD, or type 'Yesterday') ")
    return user_input_date


# loads the entire json data from the website
def import_vaccination_data():
    # load data from the website
    with urllib.request.urlopen(VACCINATION_DATA) as url:
        data = json.loads(url.read().decode())

    return data


if __name__ == '__main__':
    main()
