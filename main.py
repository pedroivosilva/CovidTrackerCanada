import covid19_tracker_calls as covid_can

"""Created by Pedro Ivo de Oliveira Silva on 10/24/2021
This application checks the entire Canada COVID cases summary 
in country, in British Columbia and Vancouver metropolitan area.

It makes usage of api.covid19tracker.ca to retrieve data."""

if __name__ == '__main__':
    print("\nThis app makes usage of api.covid19tracker.ca to retrieve all data.\n")
    covid_can.print_all_table()