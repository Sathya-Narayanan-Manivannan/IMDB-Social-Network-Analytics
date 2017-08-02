'''This script works better in python 3.5 version'''

#import pip
#pip.main(['install','nxviz'])

import networkx as nx
import nxviz as nv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''Reading the years from main dataset'''
dataframe_main= pd.DataFrame.from_csv('IMDB-Movie-Data.csv')
year_lst=list(dataframe_main.Year)

'''Creating the nodes for bipartite graph'''

dataframe_one = pd.DataFrame.from_csv('Movies_Genres.csv')
genres= list(pd.concat([dataframe_one['Genre1'], dataframe_one['Genre2']]).unique())

del genres[-8]

genres_lst= sorted(genres)
movie_lst= list(dataframe_one.index)

'''To concatenate movie and year to handle same titled movies'''
movie_year_list = []
for i in range(1000):
    l=str(movie_lst[i]) + '-' + str(year_lst[i])
    movie_year_list.append(l)


Bipartite_Movies_Genres = nx.Graph()

Bipartite_Movies_Genres.add_nodes_from(movie_year_list, bipartite='movies')
Bipartite_Movies_Genres.add_nodes_from(genres_lst, bipartite='genres')

'''Creating the undirected edges for bipartite graph'''

Genre1 = list(dataframe_one.Genre1.replace(np.NaN, 'NIL'))
Genre2 = list(dataframe_one.Genre2.replace(np.NaN, 'NIL'))
Genre3 = list(dataframe_one.Genre3.replace(np.NaN, 'NIL'))

edge_pairs=[]

for s in range(1000):
    edge_pairs.append((movie_year_list[s],Genre1[s]))
    
for h in range(1000):
    edge_pairs.append((movie_year_list[h],Genre2[h]))

for j in range(1000):
    edge_pairs.append((movie_year_list[j],Genre3[j]))
    
Bipartite_undirected_edges=[]

for k in edge_pairs:
    if k[1]!='NIL':
        Bipartite_undirected_edges.append(k)

Bipartite_Movies_Genres.add_edges_from(Bipartite_undirected_edges)


'''Visualizing the graph through a circos plot'''
from nxviz import CircosPlot
c=CircosPlot(Bipartite_Movies_Genres)
c.draw()
plt.show()

'''Visualizing the graph through an arc plot'''
from nxviz import ArcPlot
a=ArcPlot(Bipartite_Movies_Genres)
a.draw()
plt.show()

'''Creating a projection of movies from the bipartite graph'''
movies_projection = nx.bipartite.projected_graph(Bipartite_Movies_Genres, nodes=movie_year_list)
degree_centrality_dict=nx.degree_centrality(movies_projection)


#Creating a new csv file which is the input file for IBM SPSS
ratings_list=list(dataframe_main.Rating)

movie_rating_dict=dict()

'''Classifying the ratings'''
for q in range(1000):
    if ratings_list[q] <= 6.0:
        y = '1'
    elif ratings_list[q] > 6.0  and ratings_list[q] <= 7.5:
        y = '2'
    elif ratings_list[q] > 7.5:
        y = '3'
    movie_rating_dict[movie_year_list[q]]= y

'''matching the ratings with movies and corresponding degree centrality measures'''
movie_dcs_rating=dict()
for m,d in degree_centrality_dict.items():
    movie_dcs_rating[m]=[d,movie_rating_dict[m]]
    
int_op = pd.DataFrame(movie_dcs_rating).transpose()
final_op = int_op.rename(columns={0: 'Degree Centrality', 1: 'Rating'})
final_op.to_csv('Movies_DCS_Ratings.csv')

'''Creating a projection of genres from the bipartite graph for genres'''
genres_projection = nx.bipartite.projected_graph(Bipartite_Movies_Genres, nodes=genres_lst)
Max_closeness_centrality = max(nx.closeness_centrality(genres_projection).values())
Min_closeness_centrality = min(nx.closeness_centrality(genres_projection).values())

Closeness_centrality_dict = nx.closeness_centrality(genres_projection)


'''Calculating the most flexible genre which is closer to all movies and genres'''
for x,y in Closeness_centrality_dict.items():
    if Closeness_centrality_dict[x] == Max_closeness_centrality:
        print (x , y)
    elif Closeness_centrality_dict[x] == Min_closeness_centrality:
        print (x , y)