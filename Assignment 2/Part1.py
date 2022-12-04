#<------------------------- PART 1 -------------------------->
#1.
'''This function uses the index and min function to check for the position of the desired number in the list'''
def min_index(minlist):
    return minlist.index(min(minlist))
##------Test Case------##
print(min_index([40, 50, 10, 90, 100, 70]))

#2.
'''This function uses the index and max function to check for the position of the desired number in the list'''
def max_index(maxlist):
    return maxlist.index(max(maxlist))
##------Test Case------##
print(max_index([40, 50, 10, 90, 100, 70]))

#3.
'''This function uses a loop to compare the index of the smaller number 
in the first list to the second list and then appends '''
def smaller_indices(firstlist, secondlist):
    the_indexes = []
    for each_number in range(len(firstlist)):
        if firstlist[each_number] < secondlist[each_number]:
            the_indexes.append(each_number)
    return the_indexes
##------Test Case------##
print(smaller_indices([40, 50, 10, 90, 100, 70],[60, 20, 19, 95, 30, 20]))

#4.
'''This function uses a loop to calculate the product for each number 
in the first list and second list before appending to the list'''
def pairwise_product(firstlist, secondlist):
    the_index = []
    for each_number in range(len(firstlist)):
        final_product = firstlist[each_number] * secondlist[each_number] #Multiplies first list numbers with second list numbers
        the_index.append(final_product)
    return the_index
##------Test Case------##
print(pairwise_product([40, 50, 10, 90] ,[6, 2, 2, 5]))

#5.
'''This function uses a loop to calculate the ratio of the numbers in the first list to 
that of the second list before appending to the final list '''
def pairwise_ratio(firstlist, secondlist):
    the_index = []
    for each_number in range(len(firstlist)):
        final_product = round((firstlist[each_number] / secondlist[each_number]), 3)
        the_index.append(final_product)
    return the_index
##------Test Case------##
print(pairwise_ratio([40, 50, 10, 90] ,[60, 20, 19, 95]))

#<-------------------------------------------PART 2------------------------------------->
#1.
#Opens the file and read the lines
file = open('CountryData.csv')
file.readline()
#The lists for the information required from the CSV file
country_names = []
population = []
literacy = []
mobile = []
internet = []
electricity_production = []
electricity_consumption = []
#Creates a dictionary for indexing
country_dictionary = dict()
#Loops through the file and appends the data from each required column into the respective lists defined outside the loop
for line in file:
    the_data = line.strip()
    the_data = the_data.split(',')
    country_names.append(the_data[0])
    #Data from CSV files are all strings, even the numbers, therefore all numbers are to be converted to strings before manipulation
    population.append(int(the_data[1]))
    literacy.append(int(the_data[2]))
    mobile.append(int(the_data[3]))
    internet.append(int(the_data[4]))
    electricity_production.append(int(the_data[5]))
    electricity_consumption.append(int(the_data[6]))
    country_dictionary[the_data[0]] = country_names.index(the_data[0])
file.close()

#2.
#Requests information of country from user in order to check the information through indexing
country = input("What country would you like to get information on: ").capitalize()
#This function uses the country name and follows the position to check for 
# the information of each country in the list created in the function above
def lookup_country(country):
    if country in country_dictionary:
        the_position = country_dictionary[country]
        name_of_country = country_names[the_position]   #The position here refers to the index of the country
        the_population = population[the_position]       #The position here refers to the index of the country
        literacy_level = literacy[the_position]         #The position here refers to the index of the country
        the_mobile = mobile[the_position]               #The position here refers to the index of the country
        the_internet = internet[the_position]           #The position here refers to the index of the country
        the_electricity_production = electricity_production[the_position]
        the_electricity_consumption = electricity_consumption[the_position]
        print(f"{name_of_country} has a population of {the_population:,d} and a literacy rate of {literacy_level}%.The estimate of the number of mobile subscriptions is {the_mobile:,d}, while that of internet users is {the_internet:,d}. {name_of_country} produces {the_electricity_production} billion KWh of electricity annually, while it consumes {the_electricity_consumption} billion KWh of electricity.")
    else:
        print("Country not found")
##------Test Case ------##
lookup_country(country)

#The two lists below contains data from the function definition below which stores the 
# calculated values from the mobile subscription and internet user per capita
mobile_subscription_per_capita_list = []
internet_users_per_capita_list = []

#3.
def newdata():
    data_file = open('calculated.txt', 'w')
    data_file.write("{:^33} {:^33} {:^33}\n".format("Country","Mobile Subscription","Internet Users"))
    all_data = []
    for country in country_names:
        if country in country_dictionary:
            the_position = country_dictionary[country]
            the_population = population[the_position]
            the_mobile = mobile[the_position]
            the_internet = internet[the_position]
            #The calculation for the mobile subscription and internet users per capita for each country
            mobile_subscription_per_capita = round((the_mobile / the_population), 3)
            internet_users_per_capita = round((the_internet / the_population),3)
            #The two lists below are created to avoid duplicates in solving the question in number 4
            mobile_subscription_per_capita_list.append(mobile_subscription_per_capita)
            internet_users_per_capita_list.append(internet_users_per_capita)
            all_data.append("{:^33} {:^33} {:^33}".format(country, mobile_subscription_per_capita, internet_users_per_capita))
    #This loops through the list and writes all data that is appended unto a new line
    for line in all_data:
        data_file.write(line + '\n')
newdata()

#This prints the data in the text file created after performing the required calculation
open_data = open('calculated.txt', 'r')
for lines in open_data:
    print(lines)

#4. 
#This function displays the data by making use of the functions defined from the above functions
def all_population_data():
    print(f"The total population of Africa is {sum(population):,d}")
    print(f"{country_names[max_index(population)]} is the most populated country with population of {max(population):,d}")
    print(f"{country_names[min_index(population)]} is the least populated country with population of {min(population):,d}")
    print(f"{country_names[max_index(literacy)]} has the highest literacy of {max(literacy)}")
    print(f"{country_names[min_index(literacy)]} has the lowest literacy of {min(literacy)}")
    average_literacy = (sum(pairwise_product(literacy, population)))/sum(population)
    print(f"The average literacy rate in Africa is {(average_literacy):.3f}")
    print(f"{country_names[max_index(mobile_subscription_per_capita_list)]} has the highest mobile subscriptions per capita {max(mobile_subscription_per_capita_list)}")
    print(f"{country_names[min_index(internet_users_per_capita_list)]} has the lowest mobile subscription per capita {min(internet_users_per_capita_list)}")
    print("\n")
    electricity_exporters = smaller_indices(electricity_consumption,electricity_production)
    print("The countries that produce more electricity than they consume (electricity exporters)")
    for exporters in electricity_exporters:
        print(country_names[exporters])
    print("\n")
    electricity_importers = smaller_indices(electricity_production,electricity_consumption)
    print("The countries that consume more electricity than they produce (electricity importers)")
    for importers in electricity_importers:
        print(country_names[importers])

all_population_data()
