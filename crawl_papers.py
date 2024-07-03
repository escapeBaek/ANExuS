import os
import django
import requests
from bs4 import BeautifulSoup

# Django 설정 파일 경로 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anhub.settings')  # 실제 프로젝트 이름으로 변경
django.setup()

from board.models import Board

def get_latest_papers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    papers = []
    for article in soup.select('.issue-item__title a'):
        title = article.text.strip()
        link = article['href']
        papers.append({'title': title, 'link': link})

    return papers

def save_papers_to_db(papers):
    for paper in papers:
        try:
            Board.objects.create(
                title=paper['title'], 
                contents=f"Link: {paper['link']}", 
                author='crawler'  # 필요한 경우 적절한 author로 변경
            )
            print(f"Saved paper: {paper['title']}")
        except Exception as e:
            print(f"Failed to save paper: {paper['title']}. Error: {e}")

# 테스트 실행
if __name__ == '__main__':
    url = 'https://www.bjanaesthesia.org/current'
    latest_papers = get_latest_papers(url)
    save_papers_to_db(latest_papers)
    print("Successfully crawled and attempted to save papers.")
