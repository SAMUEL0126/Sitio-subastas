import os
import sys
from auctions.models import Item, User

def get_items():
    ''' 
    Get all active auction listings
    '''
    items = Item.objects.all()
    if len(items) != 0:
        items_list = [item for item in items]        
        return items_list
    else:
        return None

def get_users_with_items():
    '''
    Get all registered users 
    '''
    distinct_users = User.objects.filter(item_list__user__isnull=False).distinct()
    if len(distinct_users) != 0:
        users_dict = {}
        for user in distinct_users:
            users_dict[user.username] = user.pk
        return users_dict
    else: 
        None


    
