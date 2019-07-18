import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import *


def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]



df= pd.read_csv("movie_dataset.csv")


features=['keywords','cast','genres','director']
for feature in features:
    df[feature]=df[feature].fillna(' ')


def combine_features(row) :
    return row['keywords']+ " " +  row['cast']+ " " + row['genres']+ " " + row['director']
df["combined_features"]=df.apply(combine_features,axis=1)
   


cv= CountVectorizer()
count_matrix=cv.fit_transform(df["combined_features"])


cosine_sim=cosine_similarity(count_matrix)
    
def getValue():
        movie_user_likes=e1.get()
        movie_index=get_index_from_title(movie_user_likes)
        similar_movies=list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies=sorted(similar_movies, key= lambda x:x[1], reverse=True)        
        i=0
        l=list()
        for movie in sorted_similar_movies :
            if(i>0): 
                l.append(get_title_from_index(movie[0]))
            i=i+1
            if i>10:
                break
        msg="Top 10 Recommended movies because you watched "+movie_user_likes+"\n" + ("\n".join(l))
        child=Toplevel()
        child.title("Recommender System Output")
        Label(child,text=msg).pack()
        Button(child,text="OK",command=child.destroy).pack()
        
root=Tk()
root.title("Recommender System")
l1=Label(root,text="Enter the movie")
e1=Entry(root)
l1.grid(row=0)
e1.grid(row=0, column=1)




b1=Button(root,text="Enter",command=getValue)
b1.grid(columnspan=2)

root.mainloop() 

