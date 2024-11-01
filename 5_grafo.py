import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


file_path = 'theonion_posts.csv'
df_posts = pd.read_csv(file_path)



##########################Criação de um grafo com os dados obtidos
G = nx.Graph()

for _, row in df_posts.iterrows():
    author = row['author']
    comment_authors = row['comment_authors']

    if author not in G:
        G.add_node(author)

    #Novo nó para cada autor de comentário e arestas entre o autor e quem comentou no post dele
    if pd.notna(comment_authors):
        comment_authors_list = eval(comment_authors)
        for commenter in comment_authors_list:
            #Se der erro, precisa incluir [] nas entradas da coluna comment_authors. Ex.: ['user1', 'user2', ...]
            if commenter != author:
                if commenter not in G:
                    G.add_node(commenter)
                G.add_edge(author, commenter)



#Exibição
plt.figure(figsize=(30, 30))
pos = nx.spring_layout(G, k=0.15, iterations=20)
nx.draw(G, pos, with_labels=True, node_size=50, font_size=8, node_color='skyblue', edge_color='gray', alpha=0.7)
plt.title('Grafo TheOnion')
plt.show()


nx.write_gml(G, 'grafo_theonion.gml')
