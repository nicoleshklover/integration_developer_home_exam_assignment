import requests

def GregorianToHebrew(gregorian_date: str) -> str:
    """
    converts a Gregorian date to a Hebrew date, with the Hebrew Date Converter REST API.
    link to API documentation: https://www.hebcal.com/home/219/hebrew-date-converter-rest-api

    input: 
        gregorian_date (string): A Gregorian date in the format of YYYY-MM-DD or gy=YYYY&gm=MM&gd=DD.
        (gy - Gregorian year, gm - Gregorian month (1=January, 12=December) Leading 0 is optional, gd-Gregorian day of month Leading 0 is optional)


    output: 
        hebrew_date (string): A Hebrew date.

    """

    try:
        # send get request
        response = requests.get(f"https://www.hebcal.com/converter?cfg=json&date={gregorian_date}&g2h=1&strict=1")

        # raise exceptions if the status code is not 200 (http errors)
        response.raise_for_status()

        # convert string response to json, extract hebrew date and reverse it so it would be from right to left
        hebrew_date = response.json()["hebrew"]

        # # prints for debugging
        # print(response.status_code)
        # print(hebrew_date)

        # # for debugging - write the date to a text file to ensure its valid
        # with open("hebrew_date.txt", "w", encoding="utf-8") as file:
        #     file.write(hebrew_date)

        return hebrew_date

    except requests.exceptions.RequestException as e:
        print(f" An erorr has occurred: {e}")

    

