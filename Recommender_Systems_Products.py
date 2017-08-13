# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:57:24 2017

@author: Sathya Narayanan Manivannan
"""

def recommender_systems(filename):
   import networkx as nx
   import pandas as pd
   from nxviz import CircosPlot
   import matplotlib.pyplot as plt
   dataframe_original_data = pd.DataFrame.from_csv(filename)

   Unique_users= list(dataframe_original_data['User_ID'].unique())
   #print(Unique_users)
   
   Unique_beacons = list(dataframe_original_data['Beacon_ID'].unique())
   #print (Unique_beacons)
   
   All_beacons= list(dataframe_original_data['Beacon_ID'])
   #print(All_beacons)
   
   All_users=list(dataframe_original_data['User_ID'])
   
   #Building a bipartite matrix
   #new_df=pd.DataFrame(index=Unique_users, columns=Unique_beacons[0:])
   #print(new_df)
   
   beacons_products={}

   for j in Unique_beacons:
       #print (j)
       
       for i in range(1, len(dataframe_original_data['Beacon_ID'])):
           
         if j == dataframe_original_data['Beacon_ID'][i]:
             
             
            if j in beacons_products:
                continue
            else :
                beacons_products[j] = dataframe_original_data['Product_Description'][i]
   print (beacons_products)
   #return (beacons_products)
   
   Bipartite_beacons_users = nx.Graph()
   Bipartite_beacons_users.add_nodes_from(Unique_users, bipartite='users')
   Bipartite_beacons_users.add_nodes_from(Unique_beacons, bipartite='beacons')
   Bipartite_beacons_users_pairs=[]
   
   for s in range(0, len(dataframe_original_data.index)):
      Bipartite_beacons_users_pairs.append((All_users[s],All_beacons[s]))
    
   #print(edge_pairs)
   Bipartite_beacons_users.add_edges_from(Bipartite_beacons_users_pairs)
   #Plot_trial=CircosPlot(Bipartite_beacons_users, node_color='bipartite')
   #Plot_trial.draw()
   nx.draw(Bipartite_beacons_users, with_labels=True)
   plt.show()
   #print(Bipartite_beacons_users.nodes(data=True))
   
   neighbor_lists_dict=dict()
   for i in range(1, len(Unique_users)+1):
       neighbor_lists_dict[i] = Bipartite_beacons_users.neighbors(i)
   #print (neighbor_lists_dict)
   
   recommended_beacons=dict()
   for i in neighbor_lists_dict:
       for j in list(set(list(neighbor_lists_dict.keys())).difference(set([i]))):
           y = set(neighbor_lists_dict[i]).difference(set(neighbor_lists_dict[j]))
           
           if len(y) > 0:
             recommended_beacons[j] = list(y)
   
   
   return recommended_beacons

print(recommender_systems('rawdata.csv'))