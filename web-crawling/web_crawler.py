import requests
from bs4 import BeautifulSoup

# 1. 크롤링할 URL
url = "https://news.ycombinator.com/"

# 2. HTML 요청
response = requests.get(url)
html = response.text

# 3. HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 4. 원하는 데이터 추출 (뉴스 제목들)
titles = soup.select(".storylink")  # 해당 클래스명을 가진 요소 선택

# 5. 출력
for i, title in enumerate(titles, 1):
    print(f"{i}. {title.text}")
