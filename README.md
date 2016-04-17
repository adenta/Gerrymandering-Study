# Project Structure
- **Spreadsheets:** directory of the raw data, xls from [this](http://www.fec.gov/pubrec/electionresults.shtml) website.

- **ElectionResults:** directory of the results for each state. Result files are saved for each year that we have data for, named YEAR.csv in the proper directory. Each record in the CSV has the properties:
  - distID *(what number the district is)*
  - demCount *(How many votes the democrats obtained)*
  - repubCount *(How many votes the republicans obtained)*
  - otherCount *(How many votes everyone else obtained)*

The project is structured in this way to make it easier to look at states independently of one another.
## reading json
    import yaml

    with open("test.json") as json_file:
        json_data = yaml.safe_load(json_file)
        print json_data
