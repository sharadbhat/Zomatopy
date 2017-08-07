import requests
import ast

base_url = "https://developers.zomato.com/api/v2.1/"


def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key =config["user_key"]
        self.check_API_key()


    def check_API_key(self):
        """
        Does a random API call to check if the API Key is a valid key or not.
        Returns "Invalid Key" if the key is invalid.
        Does not return anything if the key is valid.
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = requests.head(base_url + "categories", headers=headers)
        if r.status_code == 403:
            raise Exception('invalid_key')


    def get_categories(self):
        """
        Returns a dictionary of IDs and their respective category names.
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "categories", headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        categories = {}
        for category in a['categories']:
            categories.update({category['categories']['id'] : category['categories']['name']})

        return categories


    def get_city_ID(self, city_name):
        """
        Returns the ID for the city given as input.
        """
        city_name = city_name.split(' ')
        city_name = '%20'.join(city_name)
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?q=" + city_name, headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        if len(a['location_suggestions']) == 0:
            raise Exception('invalid_city_name')
        elif 'name' in a['location_suggestions'][0]:
            city_name = city_name.replace('%20', ' ')
            if str(a['location_suggestions'][0]['name']).lower() == str(city_name).lower():
                return a['location_suggestions'][0]['id']


    def get_city_name(self, city_ID):
        """
        Returns the name of the city ID given as input.
        """
        try:
            city_ID = int(city_ID)
        except:
            raise Exception('invalid_city_id')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?city_ids=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        if a['location_suggestions'][0]['country_name'] == "":
            raise Exception('invalid_city_id')
        else:
            temp_city_ID = a['location_suggestions'][0]['id']
            if temp_city_ID == str(city_ID):
                return a['location_suggestions'][0]['name']


    def get_collections(self, city_ID):
        pass


    def get_cuisines(self, city_ID):
        """
        Returns a sorted dictionary of all cuisine IDs and their respective cuisine names.
        """
        try:
            city_ID = int(city_ID)
        except:
            raise Exception('invalid_city_id')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cuisines?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        if len(a['cuisines']) == 0:
            raise Exception('invalid_city_id')
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
        try:
            city_ID = int(city_ID)
        except:
            raise Exception('invalid_city_id')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "establishments?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        temp_establishment_types = {}
        establishment_types = {}
        if 'establishments' in a:
            for establishment_type in a['establishments']:
                temp_establishment_types.update({establishment_type['establishment']['id'] : establishment_type['establishment']['name']})

            for establishment_type in sorted(temp_establishment_types):
                establishment_types.update({establishment_type : temp_establishment_types[establishment_type]})

            return establishment_types
        else:
            raise Exception('invalid_city_id')
