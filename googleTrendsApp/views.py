from django.shortcuts import render
from datetime import datetime
import requests
from pytrends.request import TrendReq
from django.conf import settings
import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify
from article.models import Article_table


# Your NewsAPI key
NEWS_API_KEY = settings.NEWS_API_KEY


def Daily_News_Update_Jobs_function():
    countries = [
        'bangladesh', 'united_states', 'canada', 'united_kingdom', 'australia', 'india',
        'germany', 'france', 'italy', 'spain', 'brazil',
        'japan', 'south_korea', 'russia', 'mexico', 'netherlands',
        'sweden', 'turkey', 'south_africa', 'china', 'indonesia'
    ]
    categories = {
        "All": 0,
        "Business": 12,
        "Entertainment": 3,
        "Health": 45,
        "Science/Tech": 19,
        "Sports": 20,
        "Technology": 5,
        "Travel": 67
    }

    for country in countries:
        try:
            print(country)
            topics = get_trending_topics(country)
            print(topics)
            for topic in topics:
                news_articles = fetch_news_for_topic(topic)
                print('news_articles')
                print(news_articles)
                for article in news_articles:
                    print('---------------------')
                    print('article')
                    print(article)
                    # print(article['content'])
                    if article.get('description', ''):
                        full_content = scrape_full_content(article['url']) if len(article.get('description', '')) < 50 else article['description']
                    else:
                        full_content = scrape_full_content(article['url'])
                    # print(full_content)
                    print('---------------------')

                    save_article(article['title'], None, article['content'], full_content, article['urlToImage'])
        except Exception as exc:
            print(exc)


def save_article(title, category_name, Short_Description, description, image_url=None):
    # Find or create the category
    # category, created = article_category.objects.get_or_create(name=category_name)

    # Create a new article instance
    article = Article_table(
        Title=title,
        # slug=slugify(title),  # Automatically generate a slug from the title
        Category=category_name,
        Short_Description=Short_Description,  # Truncate to 150 chars for a short description
        Description=description,
        image=image_url,  # Assuming you have an image URL or a local file path
    )
    article.save()  # Save to the database
    print(f"Article '{title}' saved successfully!")



def fetch_news_for_topic(topic):
    API_KEY = settings.NEWS_API_KEY
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    return []




def get_trending_topics(country):
    if country == 'bangladesh':
        # Fetch trends for Bangladesh using interest over time
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(kw_list=[''], geo='BD', timeframe='now 1-d')
        trends = pytrends.interest_over_time()
        return trends.index.tolist()  # List of trending keywords (if available)
    else:
        # Fetch trends using trending_searches for supported countries
        pytrends = TrendReq(hl='en-US', tz=360)
        trending_searches = pytrends.trending_searches(pn=country)
        return trending_searches[0].tolist()



def scrape_full_content(article_url):
    try:
        response = requests.get(article_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Attempt to extract main content (may vary by website structure)
            paragraphs = soup.find_all('p')
            return ' '.join(p.get_text() for p in paragraphs)
    except Exception as e:
        print(f"Error scraping {article_url}: {e}")
    return None

