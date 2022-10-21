"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Bangalore'] = {'India' : ['Asia']}
locations['Atlanta'] = {'USA' : ['North America']}
locations['Cairo'] = {'Egypt' : ['Africa']}
locations['Shanghai'] = {'China' : ['Asia']}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
#1
print(1)
usa_cities = []
for key,value in locations.items():
    for country in value.keys():
        if country == 'USA':
            usa_cities.append(key)

usa_cities= sorted(usa_cities)
for a in usa_cities:
    print(a)
#2
print(2)
asia_cities = {}
for key,value in locations.items():
    for country in value.keys():
        if value[country][0] == 'Asia':
            asia_cities[key] = country
asia_keys = sorted(asia_cities.keys())
for k in asia_keys:
    print(k + ' - ' + asia_cities[k])

