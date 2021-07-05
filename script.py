# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
# the usage of function, control flow, and string slicing
conversion = {"M": 1000000,
              "B": 1000000000}
damage = ""
def update_damages(damage):
    if damage[-1] == "M":
      return float(damage[:-1]) * conversion["M"]
    elif damage[-1] == "B":
      return float(damage[:-1]) * conversion["B"]
    else:
      return "Damages not recorded"
# test function by updating damages
print(update_damages("Damages not recorded"))
print(update_damages("100M"))
print(update_damages("6.2B"))


# 2 
# Create a Table
# Parameter = [Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death]
# the usage of string.index(), dictionary formatting

Name = ""
def hurricane_data(Name):
  index = names.index(Name)
  return {Name: {"Name" : names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected" : areas_affected[index], "Damage": damages[index], "Death" : deaths[index]}}

  
# Create and view the hurricanes dictionary
print(hurricane_data("Cuba I"))
print(hurricane_data("Michael"))

# 3
# Organizing by Year
# the usage of function, control flow, list comprehensions, list.append(), dictionary formatting
def hurricane_data_by_year(Year):
  if Year in years:
    year_index =  [i for i, e in enumerate(years) if e == Year]
    print(year_index)
    list = []
    for j in year_index:
      list.append({"Name" : names[j], "Month": months[j], "Year": Year, "Max Sustained Wind": max_sustained_winds[j], "Areas Affected" : areas_affected[j], "Damage": damages[j], "Death":deaths[j]})
    return {Year: list}
  else:
    return "There is no year record"  


  

# create a new dictionary of hurricanes with year and key
print(hurricane_data_by_year(1932))
print(hurricane_data_by_year(2005))
print(hurricane_data_by_year(2020))

# 4
# Counting Damaged Areas
# the usage of function, control flow, list.append(), zip(), building dictionary with key:value pairs
def occurances_of_hurricanes(area):
  count = 0
  for region in areas_affected:
    if area in region: 
        count += 1
  return count  
print(occurances_of_hurricanes("Florida"))
print(occurances_of_hurricanes("United States Gulf Coast (especially Florida Panhandle)"))
print(occurances_of_hurricanes("Texas"))

# create dictionary of areas to store the number of hurricanes involved in
unique_areas_affected = []
region = []
area = ""
for region in areas_affected:
  for area in region:
    if not area in unique_areas_affected: 
      unique_areas_affected.append(area) 
print(unique_areas_affected)
  
unique_areas_affected_occurances = []
for area in unique_areas_affected:
  times = occurances_of_hurricanes(area)
  unique_areas_affected_occurances.append(times)
print(unique_areas_affected_occurances)

dict_area_occurance = {key: value for (key, value) in zip(unique_areas_affected, unique_areas_affected_occurances)}
print(dict_area_occurance)


# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
# the usage of function, control flow, dict.values(), list slicing, max(), range(), len(), string formatting
def most_hurricanes():
  hurricane_count = dict_area_occurance.values()  
  hurricane_count_list = list(hurricane_count)
  largest_count = max(hurricane_count_list)
  i = 0
  area_affected = list(dict_area_occurance) 
  for i in list(range(len(hurricane_count_list))):
      if hurricane_count_list[i] == largest_count:
          return ("The area affected by the most hurricanes is  " + area_affected[i] + " , and it was hit by " + str(largest_count) + " times.")
print(most_hurricanes())

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
# the usage of function, control flow, dict.values(), list slicing, range(), len(), string formatting
def deadliest_hurricane():
  largest_death_count = max(deaths)
  for i in list(range(len(deaths))):
    if deaths[i] == largest_death_count:
      return ("The hurricanes caused the greatest number of death is  " + names[i] + " , and the number of deaths is " + str(largest_death_count) +".")
print(deadliest_hurricane())



# 7
# Rating Hurricanes by Mortality
# the usage of function, control flow, list slicing, dict.update()
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
i = 0

for i in list(range(len(deaths))):
  if deaths[i] <= 100:
    list1.append(names[i])
  elif deaths[i] > 100 and deaths[i] <= 500:
    list2.append(names[i])
  elif deaths[i] > 500 and deaths[i] <= 1000:
    list3.append(names[i])
  elif deaths[i] > 1000 and deaths[i] <= 10000:
    list4.append(names[i])
  else:
    list5.append(names[i])

def rate_by_mortality(rate):
  if rate == 1:
    return {rate: list1}
  elif rate == 2:
    return {rate: list2}
  elif rate == 3:
    return {rate: list3}
  elif rate == 4:
    return {rate: list4}
  else:
    return {rate: list5}

print(rate_by_mortality(1))
print(rate_by_mortality(5))

# categorize hurricanes in new dictionary with mortality severity as key
dict_whole_by_mortality = {}
dict_whole_by_mortality.update(rate_by_mortality(1))
dict_whole_by_mortality.update(rate_by_mortality(2))
dict_whole_by_mortality.update(rate_by_mortality(3))
dict_whole_by_mortality.update(rate_by_mortality(4))
dict_whole_by_mortality.update(rate_by_mortality(5))
print(dict_whole_by_mortality )


# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
# the usage of function, control flow, list slicing, list.append(), max(), range(), len(), string formatting
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

numeric_damages_list = []
conversion = {"M": 1000000,
              "B": 1000000000}
def most_damaged_hurricane():
  for damage in damages:
    if damage[-1] == "M":
      numeric_damages_list.append(float(damage[:-1]) * conversion["M"])
    elif damage[-1] == "B":
      numeric_damages_list.append(float(damage[:-1]) * conversion["B"])
    else:
       numeric_damages_list.append(0)
  most_damages = max(numeric_damages_list)
  for i in list(range(len(numeric_damages_list))):
    if numeric_damages_list[i] == most_damages:
      return ("The hurricane that caused the greatest damage is " + names[i] + " and it costs " + str(most_damages) + ".")
print(most_damaged_hurricane())



# 9
# Rating Hurricanes by Damage
# the usage of function, control flow, list slicing, list.append(), dict.update()
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']  

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
i = 0

for i in list(range(len(numeric_damages_list))):
  if numeric_damages_list[i] <= 100000000:
    list1.append(names[i])
  elif numeric_damages_list[i] > 100000000 and numeric_damages_list[i] <= 1000000000:
    list2.append(names[i])
  elif numeric_damages_list[i] > 1000000000 and numeric_damages_list[i] <= 10000000000:
    list3.append(names[i])
  elif numeric_damages_list[i] > 10000000000 and numeric_damages_list[i] <= 50000000000:
    list4.append(names[i])
  else:
    list5.append(names[i])

def rate_by_damages(rate):
  if rate == 1:
    return {rate: list1}
  elif rate == 2:
    return {rate: list2}
  elif rate == 3:
    return {rate: list3}
  elif rate == 4:
    return {rate: list4}
  elif rate == 5:
    return {rate: list5}

print(rate_by_damages(2))
print(rate_by_damages(3))

# categorize hurricanes in new dictionary with damage severity as key
dict_whole_by_damages = {}
i = 1
def dict_by_damages():
  for i in list(range(1,6)):
    dict_whole_by_damages.update(rate_by_damages(i))
    i += 1
  return dict_whole_by_damages
print(dict_by_damages())

