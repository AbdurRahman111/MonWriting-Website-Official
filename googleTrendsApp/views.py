# from django.shortcuts import render
# from datetime import datetime
# import requests
# from pytrends.request import TrendReq
# from django.conf import settings
# import requests
# from bs4 import BeautifulSoup
# from django.utils.text import slugify
# from article.models import Article_table
# import time



# # Your NewsAPI key
# NEWS_API_KEY = settings.NEWS_API_KEY


# def Daily_News_Update_Jobs_function():
#     countries = [
#         'bangladesh', 'united_states', 'canada', 'united_kingdom', 'australia', 'india',
#         'germany', 'france', 'italy', 'spain', 'brazil',
#         'japan', 'south_korea', 'russia', 'mexico', 'netherlands',
#         'sweden', 'turkey', 'south_africa', 'china', 'indonesia'
#     ]
    
#     for country in countries:
#         try:
#             print(country)
#             topics = get_trending_topics(country)
#             print(topics)
#             for topic in topics:
#                 news_articles = fetch_news_for_topic(topic)
#                 print('news_articles')
#                 print(news_articles)
#                 for article in news_articles:
#                     print('---------------------')
#                     print('article')
#                     print(article)
#                     # print(article['content'])
#                     if article.get('description', ''):
#                         full_content = scrape_full_content(article['url']) if len(article.get('description', '')) < 50 else article['description']
#                     else:
#                         full_content = scrape_full_content(article['url'])
#                     # print(full_content)
#                     print('---------------------')

#                     save_article(article['title'], None, article['content'], full_content, article['urlToImage'])
#         except Exception as exc:
#             print(exc)



# def save_article(title, category_name, Short_Description, description, image_url=None):
#     # Find or create the category
#     # category, created = article_category.objects.get_or_create(name=category_name)

#     # Create a new article instance
#     article = Article_table(
#         Title=title,
#         # slug=slugify(title),  # Automatically generate a slug from the title
#         Category=category_name,
#         Short_Description=Short_Description,  # Truncate to 150 chars for a short description
#         Description=description,
#         image=image_url,  # Assuming you have an image URL or a local file path
#     )
#     article.save()  # Save to the database
#     print(f"Article '{title}' saved successfully!")



# def fetch_news_for_topic(topic):
#     API_KEY = settings.NEWS_API_KEY
#     time.sleep(10)  # Wait 10 seconds between requests
#     url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json().get('articles', [])
#     return []




# def get_trending_topics(country):
#     # categories = {
#     #     "All": 0,
#     #     "Business": 12,
#     #     "Entertainment": 3,
#     #     "Health": 45,
#     #     "Science/Tech": 19,
#     #     "Sports": 20,
#     #     "Technology": 5,
#     #     "Travel": 67
#     # }

#     if country == 'bangladesh':
#         # Fetch trends for Bangladesh using interest over time
#         pytrends = TrendReq(hl='en-US', tz=360)
#         pytrends.build_payload(kw_list=[''], geo='BD', timeframe='now 1-d')
#         trends = pytrends.interest_over_time()
#         return trends.index.tolist()  # List of trending keywords (if available)
#     else:
#         # Fetch trends using trending_searches for supported countries
#         try:
#             pytrends = TrendReq(hl='en-US', tz=360)
#             trending_searches = pytrends.trending_searches(pn=country)
#             # print('trending_searches')
#             # print(trending_searches)

#             time.sleep(10)  # Wait 10 seconds between requests

#             if not trending_searches.empty:
#                 return trending_searches[0].tolist()  # Return the first column of trends
#             else:
#                 print(f"No trending searches data available for {country}")
#                 return []
#         except Exception as e:
#             print(f"Error fetching trending searches for {country}: {e}")
#             return []


#         # pytrends = TrendReq(hl='en-US', tz=360)
#         # trending_data = []
#         # for category_name, category_id in categories.items():
#         #     try:
#         #         # Fetch trends based on category for the country
#         #         pytrends.build_payload(kw_list=[''], geo='US', cat=category_id, timeframe='now 1-d')
#         #         interest_over_time = pytrends.interest_over_time()

#         #         if not interest_over_time.empty:
#         #             # Extract trending topics
#         #             trending_topics = interest_over_time.index.tolist()
#         #             for topic in trending_topics:
#         #                 trending_data.append({
#         #                     "country": country,
#         #                     "category": category_name,
#         #                     "topic": topic
#         #                 })
#         #                 print(trending_data)
                
#         #         time.sleep(1)  # Avoid hitting rate limits
#         #     except Exception as e:
#         #         print(f"Error fetching data for {country} - {category_name}: {e}")
#         # return trending_data



# def scrape_full_content(article_url):
#     try:
#         response = requests.get(article_url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # Attempt to extract main content (may vary by website structure)
#             paragraphs = soup.find_all('p')
#             return ' '.join(p.get_text() for p in paragraphs)
#     except Exception as e:
#         print(f"Error scraping {article_url}: {e}")
#     return None


from django.shortcuts import render
from datetime import datetime
import requests
from pytrends.request import TrendReq
from bs4 import BeautifulSoup
from django.utils.text import slugify
from django.conf import settings
from article.models import Article_table
import time
import feedparser

# Global to track if NewsAPI limit is reached
news_api_limit_reached = False


def Daily_News_Update_Jobs_function():
    """
    Main function to update news daily by fetching data from NewsAPI, Guardian API, and RSS feeds.
    """
    countries = [
        'bangladesh', 'united_states', 'canada', 'united_kingdom', 'australia', 'india',
        'germany', 'france', 'italy', 'spain', 'brazil',
        'japan', 'south_korea', 'russia', 'mexico', 'netherlands',
        'sweden', 'turkey', 'south_africa', 'china', 'indonesia'
    ]

    for country in countries:
        try:
            print(f"Fetching data for country: {country}")
            topics = get_trending_topics(country)
            print(f"Trending topics for {country}: {topics}")

            for topic in topics:
                # Fetch articles with fallback logic
                news_articles = fetch_articles_with_fallback(topic)
                for article in news_articles:
                    if 'source' in article:  # NewsAPI articles
                        save_newsapi_article(article)
                    elif 'webTitle' in article:  # The Guardian API articles
                        save_guardian_article(article)

            # Fetch RSS articles
            rss_articles = fetch_rss_articles()
            for article in rss_articles:
                save_rss_article(article)

        except Exception as exc:
            print(f"Error processing country {country}: {exc}")


def fetch_articles_with_fallback(topic):
    """
    Fetch articles using NewsAPI first, and fallback to The Guardian API if the limit is reached.
    """
    global news_api_limit_reached

    if not news_api_limit_reached:
        # Try NewsAPI first
        news_articles = fetch_news_for_topic(topic)
        if news_articles:
            return news_articles
        else:
            # If the limit is reached or another error occurs, mark NewsAPI as unavailable
            news_api_limit_reached = True
            print("NewsAPI limit reached. Switching to The Guardian API.")

    # Fallback to The Guardian API
    guardian_articles = fetch_guardian_articles(topic)
    return guardian_articles


def fetch_news_for_topic(topic):
    """
    Fetch articles for a given topic using NewsAPI.
    """
    API_KEY = settings.NEWS_API_KEY
    time.sleep(1)  # Avoid hitting rate limits
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    return None


def fetch_guardian_articles(topic):
    """
    Fetch articles for a given topic using The Guardian API.
    """
    API_KEY = settings.GUARDIAN_API_KEY
    url = f"https://content.guardianapis.com/search?q={topic}&api-key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('response', {}).get('results', [])
    return []


def fetch_rss_articles():
    """
    Fetch articles from an RSS feed.
    """
    rss_url = "https://rss.cnn.com/rss/edition.rss"  # Example RSS feed URL
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.get('title', 'No Title'),
            'link': entry.get('link', ''),
            'description': entry.get('description', ''),
        })
    return articles


def get_trending_topics(country):
    """
    Fetch trending topics for a given country using Google Trends.
    """
    if country == 'bangladesh':
        # Fetch trends for Bangladesh using interest over time
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(kw_list=[''], geo='BD', timeframe='now 1-d')
        trends = pytrends.interest_over_time()
        return trends.index.tolist()  # List of trending keywords (if available)
    else:
        # Fetch trends using trending_searches for supported countries
        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            trending_searches = pytrends.trending_searches(pn=country)
            time.sleep(10)  # Wait 10 seconds between requests
            if not trending_searches.empty:
                return trending_searches[0].tolist()  # Return the first column of trends
            else:
                print(f"No trending searches data available for {country}")
                return []
        except Exception as e:
            print(f"Error fetching trending searches for {country}: {e}")
            return []


def scrape_full_content(article_url):
    """
    Scrape the full content of an article from its URL.
    """
    try:
        response = requests.get(article_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            return ' '.join(p.get_text() for p in paragraphs)
    except Exception as e:
        print(f"Error scraping {article_url}: {e}")
    return None


def save_newsapi_article(article):
    """
    Save an article from NewsAPI to the database.
    """
    title = article.get('title', 'No Title')
    short_description = article.get('description', '')[:150]
    content = scrape_full_content(article['url']) or article.get('content', '')
    image_url = article.get('urlToImage', None)

    article_instance = Article_table(
        Title=title,
        Short_Description=short_description,
        Description=content,
        image=image_url,
    )
    article_instance.save()
    print(f"NewsAPI Article '{title}' saved successfully!")


def save_guardian_article(article):
    """
    Save an article from The Guardian API to the database.
    """
    title = article.get('webTitle', 'No Title')
    content = scrape_full_content(article['webUrl']) or 'Content not available'

    article_instance = Article_table(
        Title=title,
        Short_Description=None,
        Description=content,
        image=None,
    )
    article_instance.save()
    print(f"Guardian Article '{title}' saved successfully!")


def save_rss_article(article):
    """
    Save an article from an RSS feed to the database.
    """
    title = article.get('title', 'No Title')
    short_description = article.get('description', '')[:150]
    content = scrape_full_content(article.get('link', '')) or 'Content not available'

    article_instance = Article_table(
        Title=title,
        Short_Description=short_description,
        Description=content,
        image=None,
    )
    article_instance.save()
    print(f"RSS Article '{title}' saved successfully!")
