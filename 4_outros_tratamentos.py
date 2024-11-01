import pandas as pd

file_path = 'theonion_posts.csv'
df_posts = pd.read_csv(file_path)

#Remoção de URLs repetidas
df_posts = df_posts.drop_duplicates(subset=['url'])

#Exclusão de linhas com o campo 'text' vazio ou textos curtos
min_text_length = 300
df_posts = df_posts[df_posts['text'].notna() & (df_posts['text'].str.len() >= min_text_length)]

#Na coluna 'comment_authors', remoção do username de autores que comentaram no próprio post
#Remoção feita para a criação do grafo
def remove_author_from_commenters(row):
    if pd.isna(row['comment_authors']):
        return ''
    commenters = row['comment_authors'].split(', ')
    if row['author'] in commenters:
        commenters.remove(row['author'])
    return ', '.join(commenters)

df_posts['comment_authors'] = df_posts.apply(remove_author_from_commenters, axis=1)


df_posts.to_csv('theonion_posts.csv', index=False)
print(f'Posts restantes: {len(df_posts)}')
