print("Hello World")

counties=['Arapahoe','Denver','Jefferson']
if counties[1]=='Denver':
    print(counties[1])
counties=['Arapahoe','Denver','Jefferson']
if 'El Paso' in counties:
    print('El Paso is in the list of counties')
else:
    print('El Paso is not the list of counties')

# Checking if Arapahor and El Paso are in the list
if 'Arapahoe' in counties and 'El Paso' in counties:
    print('Arapahoe and El Paso are in the list of counties')
else:
    print('Arapahoe or El Paso is not in the list of counties')
# Checking if either one is in the list
if 'Arapahoe' in counties or 'El Paso' in counties:
    print('Arapahoe or El Paso is in the list of counties')
else:
    print('Arapahoe and El Paso are not in the list of counties')

# Checking if Arapahoe is in but El Paso is not 
if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties')

# Adding data for counties and registered voters:
counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}

# Making loop to list out all counties and amount of registered voters, then adding them into an output sentence
for key,value in counties_dict.items():
    print(str(key) + " " + "county has" + " " + str(value) + " " + "registered voters.")

#re-formatting the sentence to account for use of f-strings, and adding the comma at the thousandths place
for key,value in counties_dict.items():
    print(f'{key} county has {value:,} registered voters.')

voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
                {'county':'Denver', 'registered_voters': 463353},
                {'county':'Jefferson', 'registered_voters': 432438}]

# Using range function to iterate over list of dictionaries and print the counties
for i in range(len(voting_data)):
    print(voting_data[i])

#Retrieving values of voters and counties from each dictionary in the list as NESTED FOR LOOP
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Creating a second nested for loop to retrieve number of registered voters 
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#same can be done with the county
for county_dict in voting_data:
    print(county_dict['county'])

#Using voting_data to print each county and registered voter from the dictionary. Output should include comma in the thounsandths place
for data in voting_data:
    for county, voters in data.items():
        print(f'{county} county has {voters} registered voters.')