import doctest
import numpy as np
import matplotlib.pyplot as plt


def read_csv(path: str):
    """Read one column from a CSV file with headers into a list of strings.
     """
    # Part-1- read the csv file and make a list 
    data_list = []
    with open(path, 'r') as f:
        lines = [line.rstrip() for line in f]  # skip the '\n' in csv file
    # pseudo code: separate each line by "," and store list in data_list
    for line in lines:
        data_list += line.split(',')

    # Part-2 - convert list of list into dictionary, where key is year
    data_dict = {}
    row_ct = 0
    for row in data_list:
        # pseudo code: store data in dict where key is year (YYYY), value is rainfall (float)
        if row_ct == 0 or row_ct % 2 == 0:
            data_dict.update({int(row[0:4]):float(data_list[row_ct+1])}) # row[0:4] is year without two end chars
            row_ct += 1
        else:
            row_ct += 1

    return data_dict

def average_rainfall(rainfall_values: dict)-> int:
    mean_rainfall = 0
    total_rainfall = 0
    val_ct = 0
    # pseudo code: calculate the average rainfall value
    for key in rainfall_values:
        total_rainfall += rainfall_values[key]
        val_ct += 1
    
    mean_rainfall = round(total_rainfall / val_ct)

    #print('This is the mean of rainfall: ', mean_rainfall)
    return mean_rainfall

def high_rain(rainfall_values: dict, mean_rainfall: int):

    high_rain_years = []
    # pseudo code: find years with more than 1.5 * average rainfall
    for key in rainfall_values:
        if rainfall_values[key] > 1.5 * average_rainfall(rainfall_values):
            high_rain_years += [key]

    print("High rain year: " + str(high_rain_years))
    return high_rain_years
  

def main():
    rainfall_values = read_csv("november_rain.csv")
    result = average_rainfall(rainfall_values)
    high_rain(rainfall_values, result)

    # for plotting the graph
    years = list(rainfall_values.keys())
    values = list(rainfall_values.values())
    mean_rainfall = result
    plt.xlabel('Years')
    plt.ylabel('Precipitation')
    plt.title('Years vs precipitation with Average (red)')
    plt.bar(years, values, width=0.8)
    # csv list long, only couple of years are shown within 10 years interval.
    plt.xticks(np.arange(min(years), max(years), 5), rotation=45)
    plt.axhline(y=mean_rainfall, color='r', linestyle='-')
    plt.show()

if __name__ == "__main__":
    main()
