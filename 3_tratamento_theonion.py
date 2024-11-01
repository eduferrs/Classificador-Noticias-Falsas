import pandas as pd
import re

file_path = 'theonion_posts.csv'
df_posts = pd.read_csv(file_path)


def remove_patterns(text):

    #Para verificar se o campo não está vazio e evitar erro
    if not isinstance(text, str):
        return text

    #Padrões
    horoscope_pattern = r"Advertising.*?Terms of Use"
    membership_pattern = r"Get The Paper\. Become A Member\..*?Share Published:"
    news_photos_pattern = r"More News in Photos.*?Terms of Use"
    videos_pattern = r"Explore More Videos.*?Terms of Use"
    magazine_pattern = r"Explore The Magazine.*?Terms of Use"

    #Remoção
    text = re.sub(horoscope_pattern, '', text, flags=re.DOTALL)
    text = re.sub(membership_pattern, '', text)
    text = re.sub(news_photos_pattern, '', text, flags=re.DOTALL)
    text = re.sub(videos_pattern, '', text, flags=re.DOTALL)
    text = re.sub(magazine_pattern, '', text, flags=re.DOTALL)

    return text.strip()


df_posts['text'] = df_posts['text'].apply(remove_patterns)
df_posts.to_csv('theonion_posts.csv', index=False)
