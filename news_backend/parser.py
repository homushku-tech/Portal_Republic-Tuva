# Импорт необходимых библиотек
import requests
from bs4 import BeautifulSoup
# Получаем текст страницы
url = 'https://rtyva.ru/'
page = requests.get(url).text
# Turn page into BeautifulSoup object to access HTML tags
soup = BeautifulSoup(page)
# Get headline
headline = soup.find('h1').get_text()
# # Get text from all <p> tags.
# p_tags = soup.find_all('p')
# p_tags_text = [tag.get_text().strip() for tag in p_tags]
# print(p_tags_text)
# # Filter out sentences that contain newline characters '\n' or don't contain periods.
# sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
# sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
# # Combine list items into string.
# article = ' '.join(sentence_list)

# Находим все элементы с классом 'news-item'
news_items = soup.find_all(class_='news-item')

# Обработка найденных элементов
for item in news_items[1:10]:
    news_name = item.find(class_='news-name').find('b').get_text()
    news_text = item.find(class_='news-text').find(class_='news-preview-text').find('p').get_text()
    print(news_date_time)
    print(news_name)
    print(news_text)
print(len(news_items))