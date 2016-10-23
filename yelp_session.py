from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import time

class YelpSession():

    def __init__(self):
        
        #Need to remove if repo becomes public!!!
        auth = Oauth1Authenticator(
            consumer_key='wkTh0MO1eOcU8j1EM9i00w',
            consumer_secret='hdNvm19_2jqeZI-1juut6nJ68Bw',
            token='WGJEF0PW6odBnH0An5lWUWwcgdjzQDzH',
            token_secret='26uZy85QJkEvWDKltoIrF5FK75s'
        )

        self.client = Client(auth)

    def get_total_nearby(self, location, term='restaurants', radius=0):
        params = {'category_filter': term,
                  'lang': 'en',
                  'location': location,
                  'radius': radius
                 }
        return self.client.search(**params).total

    def get_percent_offering_deals(self, location, term='bars', radius=0):
        params = {'category_filter': term,
                  'lang': 'en',
                  'attrs': 'ActiveDeal',
                  'location': location,
                  'radius': radius
                 }
        total_nearby = self.get_total_nearby(location, term, radius)
        total_deals = self.client.search(**params).total
        return float(total_deals) / float(total_nearby)

    def get_business_info(self, business_name, location, radius=5):
        params = {'term': business_name,
                  'location': location,
                  'lang': 'en',
                  'attrs': 'ActiveDeal',
                  'radius': radius
                 }
        return self.client.search(**params)
        response = self.client.search(**params).businesses[0]
        return {'datatime': int(time.time()), 'rating': response.rating, 'total_reviews': response.review_count}

    def get_coordinate_list(self, business_name, location, radius=5):
        params = {'term': business_name,
                  'location': location,
                  'lang': 'en',
                  'attrs': 'ActiveDeal',
                  'radius': radius
                 }
        search = self.client.search(**params)
        response = []
        for business in search.businesses:
            response.append(latitbusiness.location.coordinate.latitude, business.location.coordinate.longitude])
        return response

if __name__ == '__main__':
    """Sample queries"""
    ys = YelpSession()
    search = ys.get_percent_offering_deals('San Jose, CA')
    print search
    search2 = ys.get_business_info('Original Gravity', 'San Jose, CA')
    print search2
    search3 = ys.get_coordinate_list('Original Gravity', 'San Jose, CA')
    print search3
    #import pdb; pdb.set_trace()
