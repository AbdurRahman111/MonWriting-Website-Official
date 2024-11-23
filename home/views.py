from django.shortcuts import render, redirect
from article.models import article_category, Article_table, article_chapter, article_subchapter, track_views, search_log
from account.models import Profile
from .models import contact_table, Newsletter_table
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q
from datetime import datetime
import uuid
import urllib.request
import json
from device_detector import DeviceDetector
from django.utils.translation import get_language
from django.http import HttpResponse, JsonResponse
import operator
from functools import reduce
# Create your views here.
from pytrends.request import TrendReq
from django.conf import settings
import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify



def index(request):
    # all category list
    all_categories = article_category.objects.all()

    # all articles in reverse
    all_article = Article_table.objects.all().order_by('-id')[20]

    # popular article based on total views
    popular_article = Article_table.objects.all().order_by('-total_views')[:4]

    # recent articles the last 4 articles
    recent_article = Article_table.objects.all().order_by('-id')[:4]

    # most viewed article in last hour
    bennar_article = Article_table.objects.all().order_by('-last_hour_views')[:1]

    # trending articles depands on last mosted viewed in last hour
    trending_article = Article_table.objects.all().order_by('-last_hour_views')[:4]

    # recommended article based on last search of users
    if request.user.is_authenticated:
        user_info = request.user
        search_log_last_3 = search_log.objects.filter(user = user_info)[:3]
        lst_keyword = []
        for i in search_log_last_3:
            lst_keyword.append(i.search_word)
        print(lst_keyword)
        try:
            first_word = lst_keyword[0]
        except:
            first_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

        try:
            second_word = lst_keyword[1]
        except:
            second_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

        try:
            third_word = lst_keyword[2]
        except:
            third_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'


        recommended_article = Article_table.objects.filter(Q(Title__icontains=first_word) |Q(Title__icontains=second_word) |Q(Title__icontains=third_word) | Q(Category__name__icontains=first_word) | Q(Category__name__icontains=second_word) | Q(Category__name__icontains=third_word) | Q(Chapter__name__icontains=first_word) | Q(Chapter__name__icontains=second_word) | Q(Chapter__name__icontains=third_word) | Q(Subchapter__name__icontains=first_word) | Q(Subchapter__name__icontains=second_word) | Q(Subchapter__name__icontains=third_word) | Q(tags__icontains=first_word) | Q(tags__icontains=second_word) | Q(tags__icontains=third_word))[:1]

        recommended_article2 = Article_table.objects.filter(
            Q(Title__icontains=first_word) | Q(Title__icontains=second_word) | Q(Title__icontains=third_word) | Q(
                Category__name__icontains=first_word) | Q(Category__name__icontains=second_word) | Q(
                Category__name__icontains=third_word) | Q(Chapter__name__icontains=first_word) | Q(
                Chapter__name__icontains=second_word) | Q(Chapter__name__icontains=third_word) | Q(
                Subchapter__name__icontains=first_word) | Q(Subchapter__name__icontains=second_word) | Q(
                Subchapter__name__icontains=third_word) | Q(tags__icontains=first_word) | Q(
                tags__icontains=second_word) | Q(tags__icontains=third_word))[1:5]

    else:
        if request.COOKIES.get('user_uid'):
            user_info = request.COOKIES.get('user_uid')

            search_log_last_3 = search_log.objects.filter(user_uid=user_info)[:3]
            lst_keyword = []
            for i in search_log_last_3:
                lst_keyword.append(i.search_word)

            try:
                first_word = lst_keyword[0]
            except:
                first_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

            try:
                second_word = lst_keyword[1]
            except:
                second_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

            try:
                third_word = lst_keyword[2]
            except:
                third_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'


            recommended_article = Article_table.objects.filter(
                Q(Title__icontains=first_word) | Q(Title__icontains=second_word) | Q(Title__icontains=third_word) | Q(
                    Category__name__icontains=first_word) | Q(Category__name__icontains=second_word) | Q(
                    Category__name__icontains=third_word) | Q(Chapter__name__icontains=first_word) | Q(
                    Chapter__name__icontains=second_word) | Q(Chapter__name__icontains=third_word) | Q(
                    Subchapter__name__icontains=first_word) | Q(Subchapter__name__icontains=second_word) | Q(
                    Subchapter__name__icontains=third_word) | Q(tags__icontains=first_word) | Q(
                    tags__icontains=second_word) | Q(tags__icontains=third_word))[:1]

            recommended_article2 = Article_table.objects.filter(
                Q(Title__icontains=first_word) | Q(Title__icontains=second_word) | Q(Title__icontains=third_word) | Q(
                    Category__name__icontains=first_word) | Q(Category__name__icontains=second_word) | Q(
                    Category__name__icontains=third_word) | Q(Chapter__name__icontains=first_word) | Q(
                    Chapter__name__icontains=second_word) | Q(Chapter__name__icontains=third_word) | Q(
                    Subchapter__name__icontains=first_word) | Q(Subchapter__name__icontains=second_word) | Q(
                    Subchapter__name__icontains=third_word) | Q(tags__icontains=first_word) | Q(
                    tags__icontains=second_word) | Q(tags__icontains=third_word))[1:5]

        else:
            recommended_article = None
            recommended_article2 = None

   

    context = {'all_categories':all_categories, 'all_article':all_article, 'popular_article':popular_article, 'recent_article':recent_article, 'bennar_article':bennar_article, 'trending_article':trending_article, 'recommended_article':recommended_article, 'recommended_article2':recommended_article2}
    return render(request, 'index.html', context)





def privacy_policy(request):
    return render(request, 'privacy_policy_page.html')



def about_us(request):
    return render(request, 'about_us.html')


def searchbar(request):
    keyword = request.GET.get('keyword')
    all_categories = article_category.objects.all()
    filter_article = Article_table.objects.filter(Q(Title__icontains=keyword) | Q(Category__name__icontains=keyword) | Q(Chapter__name__icontains=keyword) | Q(Subchapter__name__icontains=keyword) | Q(tags__icontains=keyword))
    count_search = filter_article.count()

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    if request.COOKIES.get('user_uid'):
        user_uid = request.COOKIES.get('user_uid')
    else:
        user_uid = None


    var_search_log = search_log(user=user, user_uid=user_uid, search_word=keyword)
    var_search_log.save()

    context = {'all_categories': all_categories, 'filter_article':filter_article, 'count_search':count_search}
    return render(request, 'search_articles.html', context)



@csrf_exempt
def function_all_categories(request):
    var_all_categories = article_category.objects.all()
    serializer_var_all_categories = serializers.serialize('json', var_all_categories)
    return JsonResponse(serializer_var_all_categories, safe=False)



def category_articles(request, slug):
    all_categories = article_category.objects.all()
    get_category = article_category.objects.get(slug = slug)
    filter_article = Article_table.objects.filter(Category=get_category).order_by('-id')
    context = {'all_categories': all_categories, 'get_category':get_category, 'filter_article':filter_article}
    return render(request, 'category_articles.html', context)



def submit_newsletter(request):
    email = request.POST.get('email')
    var_Newsletter_table = Newsletter_table(email = email)
    var_Newsletter_table.save()
    messages.success(request, "Thanks for subscribe !")

    return redirect('index')



def article_details(request, slug):
    if Article_table.objects.filter(slug=slug):
        get_article = Article_table.objects.get(slug=slug)
        get_article.total_views = get_article.total_views + 1
        get_article.save()
        try:
            get_profile = Profile.objects.get(user=get_article.Author)
            var_follow = False
            if request.user.is_authenticated:
                if request.user in get_profile.followers.all():
                    var_follow = True
            else:
                pass
        except:
            get_profile = None
            var_follow = False


        context = {'get_article':get_article, 'get_profile':get_profile, 'var_follow':var_follow}

        response = render(request, 'article_page_details.html', context)

        if request.COOKIES.get('user_uid'):
            user_uid = request.COOKIES.get('user_uid')
        else:
            print('Cookie does not exist')

            user_uid = str(uuid.uuid1())
            response.set_cookie(key='user_uid', value=user_uid, max_age=60 * 60 * 24 * 30)

        tracker(request, user_uid, get_article)
        return response
    else:
        return render(request, "404-page.html")


def tracker(request, user_uid, get_article):
    # User information

    # IP address
    api = "https://www.iplocate.io/api/lookup/"

    # Basic information
    userTimeZone = None
    userLongitude = None
    userLatitude = None
    userCountry = None
    userContinent = None
    userCity = None
    userLocZip = None
    userIp = None

    try:
        resp = urllib.request.urlopen(api)
        result = resp.read()
        result = json.loads(result.decode("utf-8"))
        userIp = result["ip"]
        userCountry = result["country"]
        userContinent = result["continent"]
        userCity = result["city"]
        userTimeZone = result['time_zone']
        userLatitude = result['latitude']
        userLongitude = result['longitude']
        userIp = result['ip']
        userLocZip = result['postal_code']

    except:
        print("Could not find: ")

    # User agent string
    ua = request.META['HTTP_USER_AGENT']

    # URL of the website
    url = request.get_full_path()

    # Time
    timeStamp = datetime.now().replace(microsecond=0)

    # Device information
    device = DeviceDetector(ua).parse()
    deviceOS = device.os_name()
    deviceType = device.device_type()
    deviceBrowser = device.client_name()
    deviceLang = get_language()

    deviceBrand = device.device_brand()
    if deviceBrand == '':
        deviceBrand = 'N/A'

    deviceModel = device.device_model()
    if deviceModel == '':
        deviceModel = 'N/A'

    # referer_view = get_referer_view(request)
    ref_url = request.META.get('HTTP_REFERER')

    # if a new user visits the website
    # a new record will be created in the database
    # but if the existing user visits the page again it will increment in the pages number
    try:
        temp = track_views.objects.get(
            Article = get_article,
            device_os=deviceOS,
            device_browser=deviceBrowser,
            device_type=deviceType,
            device_model=deviceModel,
            site_url=url,
            referrer_url=ref_url,
            user_agent=ua,
            timezone=userTimeZone,
            location_longitude=userLongitude,
            location_latitude=userLatitude,
            location_country=userCountry,
            location_region=userContinent,
            location_city=userCity,
            location_zip=userLocZip,
            user_ip=userIp,
            user_uid=user_uid,
        )

        views = temp.views
        views = views + 1
        temp.views = views
        temp.save()
    except:
        track_views.objects.create(
            Article=get_article,
            device_os=deviceOS,
            device_browser=deviceBrowser,
            device_type=deviceType,
            device_model=deviceModel,
            site_url=url,
            referrer_url=ref_url,
            user_agent=ua,
            timestamp=timeStamp,
            timezone=userTimeZone,
            location_longitude=userLongitude,
            location_latitude=userLatitude,
            location_country=userCountry,
            location_region=userContinent,
            location_city=userCity,
            location_zip=userLocZip,
            user_ip=userIp,
            user_uid=user_uid,
        )



def follow_writer(request):
    ref_url = request.META.get('HTTP_REFERER')
    print('ref_url')
    print(ref_url)
    profile_id = request.POST.get('profile_id')
    print(profile_id)
    get_writer_profile = Profile.objects.get(id=profile_id)
    print('get_writer_profile')

    user = request.user

    if user in get_writer_profile.followers.all():
        print(user)
        get_writer_profile.followers.remove(user)
    else:
        get_writer_profile.followers.add(user)

    return redirect(ref_url)



def test(request):
    return render(request, 'test.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        var_contact_table = contact_table(name=name, email=email, subject=subject, message=message)
        var_contact_table.save()

        messages.success(request, "Your Message Has Been sent to admin !")
    return render(request, 'contact.html')


def article_page(request):
    return render(request, 'article_page.html')


def article_page_details(request):
    return render(request, 'article_page_details.html')


def writer(request, username):
    if User.objects.filter(username=username):
        get_user = User.objects.get(username=username)
        filter_article = Article_table.objects.filter(Author = get_user).order_by('-id')
        get_profile = Profile.objects.get(user = get_user)

        var_follow = False
        if request.user.is_authenticated:
            if request.user in get_profile.followers.all():
                var_follow = True
        else:
            pass

        writer_chapters = article_chapter.objects.filter(Author = get_profile)

        context = {'filter_article':filter_article, 'get_user':get_user, 'get_profile':get_profile, 'var_follow':var_follow, 'writer_chapters':writer_chapters}
        return render(request, 'user_profile.html', context)
    else:
        return render(request, "404-page.html")


def subchapter(request, slug):
    if article_subchapter.objects.filter(slug = slug):
        get_subchapter = article_subchapter.objects.get(slug = slug)

        get_user = get_subchapter.Author.user
        filter_article = Article_table.objects.filter(Subchapter=get_subchapter).order_by('-id')
        get_profile = Profile.objects.get(user=get_user)

        var_follow = False
        if request.user.is_authenticated:
            if request.user in get_profile.followers.all():
                var_follow = True
        else:
            pass

        writer_chapters = article_chapter.objects.filter(Author=get_profile)
        context = {'filter_article': filter_article, 'get_user': get_user, 'get_profile': get_profile,
                   'var_follow': var_follow, 'writer_chapters': writer_chapters}
        return render(request, 'user_profile.html', context)
    else:
        return render(request, "404-page.html")


def user_profile(request):
    return render(request, 'user_profile.html')



def Blogging(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category_select = request.POST.get('category_select')
        get_category = article_category.objects.get(id = category_select)

        chapter_select = request.POST.get('chapter_select')
        new_chapter = request.POST.get('new_chapter')
        print(chapter_select, new_chapter)

        new_subchapter = request.POST.get('new_subchapter')
        subchapter_select = request.POST.get('subchapter_select')
        print(new_subchapter, subchapter_select)

        if chapter_select == "new_chapter":
            final_chapter = article_chapter(name = new_chapter, Author = Profile.objects.get(user = request.user))
            final_chapter.save()
            final_subchapter = article_subchapter(name = new_subchapter, Author = Profile.objects.get(user = request.user), Chapter = final_chapter)
            final_subchapter.save()

        else:
            final_chapter = article_chapter.objects.get(id = chapter_select)
            if subchapter_select == "new_subchapter":
                final_subchapter = article_subchapter(name=new_subchapter, Author=Profile.objects.get(user = request.user), Chapter=final_chapter)
                final_subchapter.save()
            else:
                final_subchapter = article_subchapter.objects.get(id = subchapter_select)



        Article_image = request.FILES.get('Article_image')
        Short_Description = request.POST.get('Short_Description')
        editor1 = request.POST.get('editor1')
        tags_article = request.POST.get('tags_article')

        var_final_Article = Article_table(Title=title, Category=get_category, Chapter=final_chapter, Subchapter=final_subchapter, Author=request.user, image=Article_image, Short_Description=Short_Description, Description=editor1, tags=tags_article)
        var_final_Article.save()

        messages.success(request, "Article Added Successfully !")
        return redirect('Blogging')




    all_categories = article_category.objects.all()
    all_chapter = article_chapter.objects.filter(Author = Profile.objects.get(user = request.user))
    context = {'all_categories':all_categories, 'all_chapter':all_chapter}
    return render(request, 'Create_Blogging.html', context)


def edit_article(request, slug):
    if request.method == "POST":
        article_id = request.POST.get('article_id')
        title = request.POST.get('title')
        category_select = request.POST.get('category_select')
        get_category = article_category.objects.get(id = category_select)

        chapter_select = request.POST.get('chapter_select')
        new_chapter = request.POST.get('new_chapter')
        print(chapter_select, new_chapter)

        new_subchapter = request.POST.get('new_subchapter')
        subchapter_select = request.POST.get('subchapter_select')
        print(new_subchapter, subchapter_select)

        if chapter_select == "new_chapter":
            final_chapter = article_chapter(name = new_chapter, Author = Profile.objects.get(user = request.user))
            final_chapter.save()
            final_subchapter = article_subchapter(name = new_subchapter, Author = Profile.objects.get(user = request.user), Chapter = final_chapter)
            final_subchapter.save()

        else:
            final_chapter = article_chapter.objects.get(id = chapter_select)
            if subchapter_select == "new_subchapter":
                final_subchapter = article_subchapter(name=new_subchapter, Author=Profile.objects.get(user = request.user), Chapter=final_chapter)
                final_subchapter.save()
            else:
                final_subchapter = article_subchapter.objects.get(id = subchapter_select)
                print('hi')



        Article_image = request.FILES.get('Article_image')
        Short_Description = request.POST.get('Short_Description')
        editor1 = request.POST.get('editor1')
        tags_article = request.POST.get('tags_article')

        get_article = Article_table.objects.get(id = article_id)
        get_article.Title = title
        get_article.Category = get_category
        get_article.Chapter = final_chapter
        get_article.Subchapter = final_subchapter
        if Article_image:
            get_article.image = Article_image
        get_article.Short_Description = Short_Description
        get_article.Description = editor1
        get_article.tags = tags_article
        get_article.save()


        messages.success(request, "Article Updated Successfully !")
        return redirect('article_details', get_article.slug)



    get_article = Article_table.objects.get(slug = slug)
    all_categories = article_category.objects.all().exclude(id=get_article.Category.id)
    all_chapter = article_chapter.objects.filter(Author = Profile.objects.get(user = request.user)).exclude(id=get_article.Chapter.id)
    all_subchapter_in_this_chapter = article_subchapter.objects.filter(Author = Profile.objects.get(user = request.user), Chapter=get_article.Chapter).exclude(id=get_article.Subchapter.id)
    context = {'all_categories':all_categories, 'all_chapter':all_chapter, 'get_article':get_article, 'all_subchapter_in_this_chapter':all_subchapter_in_this_chapter}
    return render(request, 'edit_Blogging.html', context)


@csrf_exempt
def getsubchapters(request):
    value = request.POST.get('value')
    getchapter = article_chapter.objects.get(id = value)
    filter_subchapter = article_subchapter.objects.filter(Chapter = getchapter)
    print(filter_subchapter)
    serializer_filter_subchapter = serializers.serialize('json', filter_subchapter)
    return JsonResponse(serializer_filter_subchapter, safe=False)