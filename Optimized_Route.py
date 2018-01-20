# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:57:53 2017

@author: Sathya Narayanan Manivannan
"""

def optimized_route(filename, time):
   import networkx as nx
   import pandas as pd
   #import matplotlib.pyplot as plt
   from datetime import datetime
   
   dataframe_original_data = pd.DataFrame.from_csv(filename)
   
   #User_ID = list(dataframe_original_data['User_ID'])
   
   EntryTime = []
   for i in list(dataframe_original_data['Entry timestamp']):
       x = datetime.strptime(i, '%m/%d/%Y %H:%M')
       EntryTime.append(x)
   
   Unique_Pkup = list(dataframe_original_data['Pickup'].unique())
   Unique_Dest = list(dataframe_original_data['Destination'].unique())
   All_Pkup = list(dataframe_original_data['Pickup'])
   All_Dest = list(dataframe_original_data['Destination'])
   
   Bipartite_Pickup_Destination = nx.Graph()
   
   Bipartite_Pickup_Destination.add_nodes_from(Unique_Pkup, bipartite='Pickup')
   Bipartite_Pickup_Destination.add_nodes_from(Unique_Dest, bipartite='Destination')
   Bipartite_Pickup_Destination_pairs=[]
   
   converted_time = datetime.strptime(time, '%m/%d/%Y %H:%M')
   
   for s in range(0, len(dataframe_original_data.index)):
      if converted_time < EntryTime[s]:
          Bipartite_Pickup_Destination_pairs.append((All_Pkup[s],All_Dest[s]))
      
   Bipartite_Pickup_Destination.add_edges_from(Bipartite_Pickup_Destination_pairs)
   
   Pkup_projection = nx.bipartite.projected_graph(Bipartite_Pickup_Destination, nodes=Unique_Pkup)
   max_degree_centrality_Pkup = list(set(sorted(nx.degree_centrality(Pkup_projection).values())))[-3:]
   Pkup_Dict = nx.degree_centrality(Pkup_projection)
   
   
   Dest_projection = nx.bipartite.projected_graph(Bipartite_Pickup_Destination, nodes=Unique_Dest)
   max_degree_centrality_Dest = list(set(sorted(nx.degree_centrality(Dest_projection).values())))[-3:]
   Dest_Dict = nx.degree_centrality(Dest_projection)
   
   closeness_centrality_Pkup = nx.closeness_centrality(Pkup_projection)
   closeness_centrality_Dest = nx.closeness_centrality(Dest_projection)
   Max_closeness_centrality_Pkup = max(nx.closeness_centrality(Pkup_projection).values())
   Max_closeness_centrality_Dest = max(nx.closeness_centrality(Dest_projection).values())
   
   Optimized_route_1 = []
   for x,y in Pkup_Dict.items():
      for i in max_degree_centrality_Pkup:
        if i == y:
            Optimized_route_1.append(x)
   print(Optimized_route_1)
   
   Via1 = []
   for x,y in closeness_centrality_Pkup.items():
       if y == Max_closeness_centrality_Pkup:
           Via1.append(x)
   print("via",Via1)
   
   
    
   Optimized_route_2 = []
   for x,y in Dest_Dict.items():
      for i in max_degree_centrality_Dest:
        if i == y:
            Optimized_route_2.append(x)
   print(Optimized_route_2)
         
   Via2 = []         
   for x,y in closeness_centrality_Dest.items():
       if y == Max_closeness_centrality_Dest:
           Via2.append(x)
   print("via",Via2)
   
   Route1 = list(set(Optimized_route_1 + Via2 + Via1))   
   Route2 = list(set(Optimized_route_2 + Via1 + Via2))
       
   #nx.draw(Pkup_projection,with_labels=True)
   #nx.draw(Dest_projection,with_labels=True)
   
   
   #nx.draw(Bipartite_Pickup_Destination, with_labels=True)
   #return (Bipartite_Pickup_Destination_pairs)
   
   return(Route1,Route2)

#Trial Execution   
print(optimized_route('Traveller_Data.csv', '7/23/2016 15:00' ))