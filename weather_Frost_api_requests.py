"""
Description:
Module for aid with requests with the Frost API, i.e. the API service for meterological data from MET Norway (the institute behind YR (www.yr.no)).
The module is based on the example Python code given by MET Norway on the Frost API webpage [https://frost.met.no/python_example.html].


Written by: Marius Dobbe Klemetsen (GitHub-usr: TheBioinformaticalGardener)
Date: 2025-06-16
"""

import requests


def foo(main_parameter: str, parameters: dict, client_id: str):
    base_url = "https://frost.met.no"
    endpoint = "/".join(
        (
            base_url,
            main_parameter,  # "observations/availableTimeSeries/v0.jsonld"  # TODO make a function argument for this
        )
    )

    # parameters = {
    #     # "sources": STATION_ID,  #'SN18700,SN90450',
    #     # 'elements': 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)',
    #     # 'referencetime': '2025-06-15/2025-06-16',
    # }

    # Issue an HTTP GET request
    r = requests.get(endpoint, parameters, auth=(client_id, ""))

    # Extract JSON data
    json = r.json()

    # Check if the request worked, print out any errors
    if r.status_code == 200:
        print("Data retrieved from frost.met.no!")
        return json
    else:
        print("Error! Returned status code %s" % r.status_code)
        print("Message: %s" % json["error"]["message"])
        print("Reason: %s" % json["error"]["reason"])
        # raise IOError('Problem with request')


def main():
    client_id = input("Give Frost API client ID number:\t")

    data = foo(
        main_parameter="observations/availableTimeSeries/v0.jsonld",
        parameters={"sources": "SN90450"},
        client_id=client_id,
    )

    print(data)


if __name__ == "__main__":
    main()
