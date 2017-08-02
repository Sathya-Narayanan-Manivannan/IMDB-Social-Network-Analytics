'''This script works better in python 2.7 version'''
import pandas as pd
dataframe_one = pd.DataFrame.from_csv('Movies_Genres.csv',index_col=False)
genres_lst= sorted(list(pd.concat([dataframe_one['Genre1'], dataframe_one['Genre2']]).unique()))
movie_lst= list(dataframe_one['Title'])
new_df=pd.DataFrame(index=movie_lst, columns=genres_lst[1:])
dataframe_no_null= dataframe_one.fillna(0)
new_df1=new_df.fillna(0)

Action = [0]*1000
Adventure = [0]*1000
Animation = [0]*1000
Biography = [0]*1000
Comedy = [0]*1000
Crime = [0]*1000
Drama = [0]*1000
Family = [0]*1000
Fantasy = [0]*1000
History = [0]*1000
Horror = [0]*1000
Music = [0]*1000
Musical = [0]*1000
Mystery = [0]*1000
Romance = [0]*1000
SciFi = [0]*1000
Sport = [0]*1000
Thriller = [0]*1000
War = [0]*1000
Western = [0]*1000

for Genre in ['Genre1','Genre2','Genre3']:
  for index in range(len(list(dataframe_one['Genre1']))):
      if list(dataframe_one[Genre])[index]=='Action':
        Action[index] = 1
      elif list(dataframe_one[Genre])[index]=='Adventure':
        Adventure[index] = 1
      elif list(dataframe_one[Genre])[index]=='Animation':
        Animation[index] = 1
      elif list(dataframe_one[Genre])[index]=='Biography':
        Biography[index] = 1
      elif list(dataframe_one[Genre])[index]=='Comedy':
        Comedy[index] = 1
      elif list(dataframe_one[Genre])[index]=='Crime':
        Crime[index] = 1
      elif list(dataframe_one[Genre])[index]=='Drama':
        Drama[index] = 1
      elif list(dataframe_one[Genre])[index]=='Family':
        Family[index] = 1
      elif list(dataframe_one[Genre])[index]=='Fantasy':
        Fantasy[index] = 1
      elif list(dataframe_one[Genre])[index]=='History':
        History[index] = 1
      elif list(dataframe_one[Genre])[index]=='Horror':
        Horror[index] = 1
      elif list(dataframe_one[Genre])[index]=='Music':
        Music[index] = 1
      elif list(dataframe_one[Genre])[index]=='Musical':
        Musical[index] = 1
      elif list(dataframe_one[Genre])[index]=='Mystery':
        Mystery[index] = 1
      elif list(dataframe_one[Genre])[index]=='Romance':
        Romance[index] = 1
      elif list(dataframe_one[Genre])[index]=='Sci-Fi':
        SciFi[index] = 1
      elif list(dataframe_one[Genre])[index]=='Sport':
        Sport[index] = 1
      elif list(dataframe_one[Genre])[index]=='Thriller':
        Thriller[index] = 1
      elif list(dataframe_one[Genre])[index]=='War':
        War[index] = 1
      elif list(dataframe_one[Genre])[index]=='Western':
        Western[index] = 1

Bipartite_Matrix = {'Title': movie_lst, 'Action': Action,'Adventure':Adventure,'Animation':Animation,'Biography':Biography,'Comedy':Comedy,'Crime':Crime,'Drama':Drama,'Family':Family,'Fantasy':Fantasy,'History':History,'Horror':Horror,'Music':Music,'Musical':Musical,'Mystery':Mystery,'Romance':Romance,'Sci-Fi':SciFi,'Sport':Sport,'Thriller':Thriller,'War':War,'Western':Western}
Bipartite_Matrix_df=pd.DataFrame(Bipartite_Matrix, index=movie_lst, columns=['Action','Adventure','Animation','Biography','Comedy','Crime','Drama','Family','Fantasy','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Sport','Thriller','War','Western'])

Bipartite_Matrix_df.to_csv('Bipartite_Matrix.csv')