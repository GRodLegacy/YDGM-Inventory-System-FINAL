from django.conf.urls import url
from .views import index, display_Electronics, display_Apparel, display_Equipment, display_Toys, display_Footwear, add_Electronics, add_Apparel, add_Equipment, add_Toys, add_Footwear, edit_Electronics, edit_Apparel, edit_Equipment, edit_Toys, edit_Footwear, delete_Electronics, delete_Apparel, delete_Equipment, delete_Toys, delete_Footwear
from .models import Electronics, Apparel, Equipment, Toys, Footwear

urlpatterns =[

    url(r'^$', index, name='index'),

    url(r'^display_Electronics$', display_Electronics, name='display_Electronics'),
    url(r'^display_Apparel$', display_Apparel, name='display_Apparel'),
    url(r'^display_Equipment$', display_Equipment, name='display_Equipment'),
    url(r'^display_Toys$', display_Toys, name='display_Toys'),
    url(r'^display_Footwear$', display_Footwear, name='display_Footwear'),

    url(r'^add_Electronics$', add_Electronics, name='add_Electronics'),
    url(r'^add_Apparel$', add_Apparel, name='add_Apparel'),
    url(r'^add_Equipment$', add_Equipment, name='add_Equipment'),
    url(r'^add_Toys$', add_Toys, name='add_Toys'),
    url(r'^add_Footwear$', add_Footwear, name='add_Footwear'),

    url(r'^edit_Electronics/(?P<pk>\d+)$', edit_Electronics, name='edit_Electronics'),
    url(r'^edit_Apparel/(?P<pk>\d+)$', edit_Apparel, name='edit_Apparel'),
    url(r'^edit_Equipment/(?P<pk>\d+)$', edit_Equipment, name='edit_Equipment'),
    url(r'^edit_Toys/(?P<pk>\d+)$', edit_Toys, name='edit_Toys'),
    url(r'^edit_Footwear/(?P<pk>\d+)$', edit_Footwear, name='edit_Footwear'),

    url(r'^delete_Electronics/(?P<pk>\d+)$',delete_Electronics, name='delete_Electronics'),
    url(r'^delete_Apparel/(?P<pk>\d+)$', delete_Apparel, name='delete_Apparel'),
    url(r'^delete_Equipment/(?P<pk>\d+)$', delete_Equipment, name='delete_Equipment'),
    url(r'^delete_Toys/(?P<pk>\d+)$', delete_Toys, name='delete_Toys'),
    url(r'^delete_Footwear/(?P<pk>\d+)$', delete_Footwear, name='delete_Footwear')

]