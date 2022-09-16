from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://dubardin:du6ardin@cluster0.j5xdh6l.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

#한국 주간 조회수

data = requests.get('https://playboard.co/chart/video/most-viewed-all-videos-in-south-korea-weekly',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
utubes = soup.select('#app > div.root > main > div > div.container.container--mfit > table > tbody > tr')

for utube in utubes:
    a = utube.select_one('td.title > a > h3')

    if a is not None:
        name = utube.select_one('td.title > a > h3').text
        rank = utube.select_one('td.rank.rank.rank--ko > div.current').text
        thum = utube.select_one('td.thumbnail > a > div > div')["data-background-image"]
        view = utube.select_one('td.score > span').text
        chel = utube.select_one('td.channel > a > span').text

        doc = {
            'names': name,
            'ranks': rank,
            'thums': thum,
            'views': view,
            'chels': chel
        }

        # allin = rank.text, thum["data-background-image"], name.text, view.text, chel.text

        print(rank, thum, name, view, chel)
        # db.utkwv.insert_one(doc)


# 한국 역대 좋아요 수


data1 = requests.get('https://playboard.co/chart/video/most-liked-all-videos-in-south-korea-total',headers=headers)

soup1 = BeautifulSoup(data1.text, 'html.parser')
utubes1 = soup1.select('#app > div.root > main > div > div.container.container--mfit > table > tbody > tr')

#app > div.root > main > div > div.container.container--mfit > table > tbody > tr:nth-child(1) > td.rank.rank.rank--ko > div.current
#app > div.root > main > div > div.container.container--mfit > table > tbody > tr:nth-child(1) > td.title > a > h3
#app > div.root > main > div > div.container.container--mfit > table > tbody > tr:nth-child(1) > td.thumbnail > a > div > div
#app > div.root > main > div > div.container.container--mfit > table > tbody > tr:nth-child(1) > td.score > span
#app > div.root > main > div > div.container.container--mfit > table > tbody > tr:nth-child(1) > td.channel > a > span

for utube1 in utubes1:
    a = utube1.select_one('td.title > a > h3')

    if a is not None:
        name = utube1.select_one('td.title > a > h3').text
        rank = utube1.select_one('td.rank.rank.rank--ko > div.current').text
        thum = utube1.select_one('td.thumbnail > a > div > div')["data-background-image"]
        view = utube1.select_one('td.score > span').text
        chel = utube1.select_one('td.channel > a > span').text

        doc = {
            'names': name,
            'ranks': rank,
            'thums': thum,
            'views': view,
            'chels': chel
        }

        print(rank, thum, name, view, chel)
        # db.utktl.insert_one(doc)
#
#
# #한국 월간 좋아요수


data2 = requests.get('https://playboard.co/chart/video/most-liked-all-videos-in-south-korea-monthly',headers=headers)

soup2 = BeautifulSoup(data2.text, 'html.parser')
utubes2 = soup2.select('#app > div.root > main > div > div.container.container--mfit > table > tbody > tr')


for utube2 in utubes2:
    a = utube2.select_one('td.title > a > h3')

    if a is not None:
        name = utube2.select_one('td.title > a > h3').text
        rank = utube2.select_one('td.rank.rank.rank--ko > div.current').text
        thum = utube2.select_one('td.thumbnail > a > div > div')["data-background-image"]
        view = utube2.select_one('td.score > span').text
        chel = utube2.select_one('td.channel > a > span').text

        doc = {
            'names': name,
            'ranks': rank,
            'thums': thum,
            'views': view,
            'chels': chel
        }

        # print(rank, thum, name, view, chel)
        db.utkml.insert_one(doc)



# #한국 주간 좋아요 수
#
#
#
data3 = requests.get('https://playboard.co/chart/video/most-liked-all-videos-in-south-korea-weekly',headers=headers)

soup3 = BeautifulSoup(data3.text, 'html.parser')
utubes3 = soup3.select('#app > div.root > main > div > div.container.container--mfit > table > tbody > tr')


for utube3 in utubes3:
    a = utube3.select_one('td.title > a > h3')

    if a is not None:
        name = utube3.select_one('td.title > a > h3').text
        rank = utube3.select_one('td.rank.rank.rank--ko > div.current').text
        thum = utube3.select_one('td.thumbnail > a > div > div')["data-background-image"]
        view = utube3.select_one('td.score > span').text
        chel = utube3.select_one('td.channel > a > span').text

        doc = {
            'names': name,
            'ranks': rank,
            'thums': thum,
            'views': view,
            'chels': chel
        }

        # print(rank, thum, name, view, chel)
        db.utkwl.insert_one(doc)


