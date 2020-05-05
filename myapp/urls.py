#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_book$', views.add_book, ),url(r'show_books$', views.show_books, ),]

if __name__ == '__main__':
    pass