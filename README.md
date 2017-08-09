# Zomatopy
A Python wrapper for the Zomato API v2.1

## Installation
```
pip install zomatopy
```
(Not yet uploaded to Pypi - will not work)

## Getting Started
### Python Version
This wrapper was written for Python 3 and might not work well with Python 2.

### Adding Zomatopy to your application
For use with only user based authentication we can create the following configuration:

```python
from Zomatopy import zomatopy

config={
  "user_key"="ZOMATO_API_KEY"
}
    
zomato = zomatopy.initialize_app(config)
```
## Methods
### Common
#### Getting all Category IDs and the category names
- Takes no inputs.
- Returns a dictionary of Category IDs and corresponding Category Names.
```python
category_dictionary = zomato.get_categories()
```

#### Getting ID for a particular city
- Takes City Name as input.
- Returns the City ID of the city.
- Can raise ```InvalidCityName``` exception.
```python
#city_name must be a string without numbers or special characters.

city_ID = zomato.get_city_ID(city_name)
```

#### Getting Name for a particular City ID
- Takes City ID as input.
- Returns name of the city with that ID.
- Can raise ```InvalidCityId``` exception.
```python
#city_ID must be an integer.

city_name = zomato.get_city_name(city_ID)
```

#### Getting the Zomato Collections in a city
- Takes City ID and number of collections as input.
- If number of collections is not specified, returns all Zomato Collections.
- Returns a dictionary of Collection Name and Collection URL.
- Can raise ```InvalidCityId``` and ```LimitNotInteger``` exceptions.
```python
#city_ID must be an integer.
#limit must be an integer.

# Returns all the Zomato Collections in a city
collections_dictionary = zomato.get_collections(city_ID)

#Returns 'limit' number of collections.
collections_dictionary = zomato.get_collections(city_ID, limit=number_of_collections)
```

#### Getting the cuisines in a city
- Takes City ID as input.
- Returns a dictionary of Cuisine ID and corresponding Cuisine Names.
- Can raise ```InvalidCityId```
```python
#city_ID must be an integer.

cuisine_dictionary = get_cuisines(city_ID)
```

#### Getting all establishment types in a city.
- Takes City ID as input.
- Returns a dictionary of Establishment Type ID and corresponding Establishment Type Name.
- Can raise ```InvalidCityId```
```python
#city_ID must be an integer.

establishment_types_dictionary = get_establishment_types(city_ID)
```
### Restaurant
#### Getting the daily menu of a restaurant
- Takes Restaurant ID as input.
- Can raise ```InvalidRestaurantId``` exception.
## Exceptions

#### InvalidKey
- If the key is not a valid Zomato API Key.
```
ValueError: InvalidKey
```
#### InvalidCityId
- If the City ID contains an alphabet or special characters.
- If the City ID is not present in the Zomato database.
```
ValueError: InvalidCityId
```
#### InvalidCityName
- If the City Name consists of numbers or special characters.
- If the City Name is not present in the Zomato database.
```
ValueError: InvalidCityName
```
#### InvalidRestaurantId
- If the Restaurant ID consists of alphabets or special characters.
- If the Restaurant ID is not present in the Zomato database.
```
ValueError: InvalidRestaurantId
```
#### LimitNotInteger
- If the limit parameter provided for the ```get_collections()``` method is not an integer.
```
ValueError: LimitNotInteger
```
#### ApiLimitExceeded
- If the daily call limit of the API Key is exceeded.
```
Exception: ApiLimitExceeded
```
