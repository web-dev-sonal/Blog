from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"subhash",
        "date": date(2005,5,15),
        "title":"mountain hiking",
        "excerpt":"simple paragraph containing some text",
        "content":"""
            Hi , i am hacker
        """
    },
    {
        "slug":"tech",
        "image":"mountains.jpeg",
        "author":"subhash",
        "date": date(2006,5,15),
        "title":"mountain hiking",
        "excerpt":"simple paragraph containing some text",
        "content":"""
            Hi , i am hacker
        """
    },
    {
        "slug":"laptop",
        "image":"mountains.jpeg",
        "author":"subhash",
        "date": date(2012,5,15),
        "title":"mountain hiking",
        "excerpt":"simple paragraph containing some text",
        "content":"""
            Hi , i am hacker
        """
    },
    {
        "slug":"hike-in-the-mountas",
        "image":"mountains.jpeg",
        "author":"subhash",
        "date": date(2022,5,15),
        "title":"mountain hiking",
        "excerpt":"simple paragraph containing some text",
        "content":"""
            Hi , i am hacker
        """
    },
    {
        "slug":"hike-in-the-untains",
        "image":"mountains.jpeg",
        "author":"subhash",
        "date": date(2020,5,15),
        "title":"mountain hiking",
        "excerpt":"simple paragraph containing some text",
        "content":"""
            Hi , i am hacker
        """
    },
    {
        "slug":"hike-in-the-motains",
        "image":"mountains.jpeg",
        "author":"subhash",
        "date": date(2021,5,15),
        "title":"mountain hiking",
        "excerpt":"simple paragraph containing some text",
        "content":"""
            Hi , i am hacker
        """
    },
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        posts: latest_posts,
    })

def posts(request):
    return render(request, 'blog/al-posts.html',{
        posts: all_posts,
    })

def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-details.html', {
        'post': identified_post,
    })