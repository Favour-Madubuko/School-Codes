def allfiles(filename):
    open_file = open(filename)
    open_file.readline()
    the_dates = []
    the_rates = []
    the_difference = []
    for lines in open_file:
        the_data = lines.strip()
        the_data = the_data.split('\t')
        the_dates.append(the_data[0])
        the_rates.append(the_data[1])
        the_difference = (float(the_rates[-1]) - float(the_rates[0]))
    open_file.close()
    return the_difference
print(allfiles('exchange rates.txt'))
