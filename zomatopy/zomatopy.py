import requests
import ast

base_url = "https://developers.zomato.com/api/v2.1/"


def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key =config["user_key"]


    def get_categories(self):
        """
        Returns a dictionary of IDs and their respective category names.
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "categories", headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        categories = {}
        for category in a['categories']:
            categories.update({category['categories']['id'] : category['categories']['name']})

        return categories


    def get_city_ID(self, city_name):
        """
        Returns the ID for the city given as input.
        """
        if city_name.isalpha() == False:
            raise ValueError('InvalidCityName')
        city_name = city_name.split(' ')
        city_name = '%20'.join(city_name)
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?q=" + city_name, headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        if len(a['location_suggestions']) == 0:
            raise Exception('InvalidCityId')
        elif 'name' in a['location_suggestions'][0]:
            city_name = city_name.replace('%20', ' ')
            if str(a['location_suggestions'][0]['name']).lower() == str(city_name).lower():
                return a['location_suggestions'][0]['id']


    def get_city_name(self, city_ID):
        """
        Returns the name of the city ID given as input.
        """
        city_ID = str(city_ID)
        if city_ID.isnumeric() == False:
            raise ValueError('InvalidCityId')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?city_ids=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        if a['location_suggestions'][0]['country_name'] == "":
            raise ValueError('InvalidCityId')
        else:
            temp_city_ID = a['location_suggestions'][0]['id']
            if temp_city_ID == str(city_ID):
                return a['location_suggestions'][0]['name']
            else:
                raise ValueError('InvalidCityId')



    def get_collections(self, city_ID, limit=None):
        """
        Returns dictionary of Zomato restaurant collections in a city and their respective URLs.
        limit parameter is optional and must be an integer.
        """
        city_ID = str(city_ID)
        if city_ID.isnumeric() == False:
            raise ValueError('InvalidCityId')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        if limit == None:
            r = (requests.get(base_url + "collections?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        else:
            if str(limit).isalpha() == True:
                raise ValueError('LimitNotInteger')
            else:
                r = (requests.get(base_url + "collections?city_id=" + str(city_ID) + "&count=" + str(limit), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        collections = {}
        for collection in a['collections']:
            collections.update({collection['collection']['title'] : collection['collection']['url']})

        return collections



    def get_cuisines(self, city_ID):
        """
        Returns a sorted dictionary of all cuisine IDs and their respective cuisine names.
        """
        city_ID = str(city_ID)
        if city_ID.isnumeric() == False:
            raise ValueError('InvalidCityId')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cuisines?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        if len(a['cuisines']) == 0:
            raise ValueError('InvalidCityId')
        temp_cuisines = {}
        cuisines = {}
        for cuisine in a['cuisines']:
            temp_cuisines.update({cuisine['cuisine']['cuisine_id'] : cuisine['cuisine']['cuisine_name']})

        for cuisine in sorted(temp_cuisines):
            cuisines.update({cuisine : temp_cuisines[cuisine]})

        return cuisines



    def get_establishment_types(self, city_ID):
        """
        Returns a sorted dictionary of all establishment type IDs and their respective establishment type names.
        """
        city_ID = str(city_ID)
        if city_ID.isnumeric() == False:
            raise ValueError('InvalidCityId')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "establishments?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        temp_establishment_types = {}
        establishment_types = {}
        if 'establishments' in a:
            for establishment_type in a['establishments']:
                temp_establishment_types.update({establishment_type['establishment']['id'] : establishment_type['establishment']['name']})

            for establishment_type in sorted(temp_establishment_types):
                establishment_types.update({establishment_type : temp_establishment_types[establishment_type]})

            return establishment_types
        else:
            raise ValueError('invalid_city_id')



    def get_daily_menu(self, restaurant_ID):
        """
        """
        pass



    def is_key_invalid(self, a):
        """
        Checks if the API key provided is valid or invalid.
        If invalid, throws a invalid_key Exception.
        """
        if 'code' in a:
            if a['code'] == 403:
                raise ValueError('InvalidKey')



    def is_rate_exceeded(self, a):
        """
        Checks if the request limit for the API key is exceeded or not.
        If exceeded, throws a API_limit_exceeded Exception.
        """
        if 'code' in a:
            if a['code'] == 440:
                raise Exception('ApiLimitExceeded')
