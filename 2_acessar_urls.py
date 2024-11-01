import pandas as pd
import requests
from bs4 import BeautifulSoup

file_path = 'theonion_posts.csv'
df_posts = pd.read_csv(file_path)

#Recupera o texto nas tags <p>
def get_paragraph_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(paragraph.get_text(separator=' ', strip=True) for paragraph in paragraphs)
        return text
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

df_posts['text'] = df_posts['url'].apply(get_paragraph_text)
df_posts.to_csv('theonion_posts.csv', index=False)
