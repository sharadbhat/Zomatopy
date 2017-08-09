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
import zomatopy

config={
  "user_key"="ZOMATO_API_KEY"
}
    
zomato = zomatopy.initialize_app(config)
```

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
#### ApiLimitExceeded
- If the daily call limit of the API Key is exceeded.
```
Exception: ApiLimitExceeded
```
