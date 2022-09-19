from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name}"



class Item(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_list")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    img_url = models.CharField(max_length=256, blank=True)
    starting_bid = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.CharField(max_length=24, default='No Category')
    status = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}, {self.description}"

class ItemCategory(models.Model):
    name = models.CharField(max_length=24, blank=False)
    item = models.ForeignKey(Item, blank=True, on_delete=models.CASCADE, related_name="category_list")
    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="user_bid_items", blank=True)
    def __str__(self):
        return f"{self.amount}"
    
class ItemComment(models.Model):
    text = models.TextField(max_length=512, blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="comments_list")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Watchlist(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist_list')

    def __str__(self):
        return f"{self.items}, {self.user}"

class Category(models.Model):
    name = models.CharField(max_length=24, blank=False)
    items = models.ManyToManyField(Item, blank=True, related_name="categories")

    def __str__(self):
        return f"{self.name}"

class AuctionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history_user")
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="items_auction_history")

    def __str__(self):
        return f"{self.user.first_name}, {self.items}"


