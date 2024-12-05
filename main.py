import requests

def GregorianToHebrew(gregorian_date: str) -> str:
    """
    Converts a Gregorian date to a Hebrew date, with the Hebrew Date Converter REST API.
    link to API documentation: https://www.hebcal.com/home/219/hebrew-date-converter-rest-api

    input: 
        gregorian_date (string): A Gregorian date in the format of YYYY-MM-DD or gy=YYYY&gm=MM&gd=DD.
        (gy - Gregorian year, gm - Gregorian month (1=January, 12=December) Leading 0 is optional, gd-Gregorian day of month Leading 0 is optional)


    output: 
        hebrew_date (string): A Hebrew date.

    """

    try:

        # check which format was inserted
        if gregorian_date[0] == "g":
            date_format = gregorian_date
        else:
            date_format = "date=" + gregorian_date

        # send get request
        response = requests.get(f"https://www.hebcal.com/converter?cfg=json&{date_format}&g2h=1&strict=1")

        # raise exceptions if the status code is not 200 (http errors)
        response.raise_for_status()

        # convert string response to json, extract hebrew date and reverse it so it would be from right to left
        hebrew_date = response.json()["hebrew"]

        return hebrew_date

    except requests.exceptions.RequestException as e:
        print(f" An erorr has occurred: {e}")

