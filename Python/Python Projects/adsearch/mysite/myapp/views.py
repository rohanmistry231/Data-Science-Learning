from posixpath import commonpath
import re
from django.shortcuts import render, redirect
from .models import Tag, Advert
import requests
from bs4 import BeautifulSoup as bsoup
from rake_nltk import Rake
import nltk
import collections
import difflib
import pyshorteners

# need to be run only once to download stopwords
# nltk.download("stopwords")
# nltk.download('punkt')

   

def index(request):
    if request.method ==  'POST':
        url = request.POST.get('url')
        print(url)
        res = requests.get(url=url)
        soup = bsoup(res.content, 'html.parser')
        all_text = ""
        for para in soup.find_all('p'):
            all_text += str(para.get_text())
        

        rake_keywords = Rake()
        rake_keywords.extract_keywords_from_text(all_text)
        ranked_keywords = rake_keywords.get_ranked_phrases()

        commontags = []
        adtags = []
        tags = Tag.objects.all()

        for tag in tags:
            adtags.append(tag.tagname)

        keywords_set = set(ranked_keywords)
        adtags_set = set(adtags)

        try:
            if (keywords_set & adtags_set):
                commontags = list(keywords_set & adtags_set)
            print(commontags)
        except:
            print("found nothing")

        relevant_ads  = []
        for advert in Advert.objects.all():
            for tag in advert.tags.all():
                if tag.tagname in commontags:
                    relevant_ads.append(advert)
                    relevant_ads = set(relevant_ads)
                    relevant_ads = list(relevant_ads)
                    
                    

        print(relevant_ads)
        
       
        context = {'relevant_ads':relevant_ads,
                    'commontags':commontags,
                    'blog_url':url}

        return render(request,'myapp/index.html', context)
        
        


    return render(request,'myapp/index.html')


