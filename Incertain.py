import streamlit as st
import  streamlit_vertical_slider  as svs
from streamlit_option_menu import option_menu
import uuid
import numpy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import math

st.title("Quel choix faire ?")

def maximin(dataframe):
    d = {}
    for i in dataframe.index:
        d[i] = min(dataframe.loc[i])
    print(d)
    l = [None] * len(dataframe.index)
    k = 1
    li=[]
    while k<=len(l):
        j = None
        m = None
        n = None
        z = 0
        for i in list(d.keys()):
            if (j is None or j < d[i]) and z not in li :
                j = d[i]
                m = i
                n = z
            z += 1
        print(k)
        li.append(n)
        l[n] = k
        k += 1
    return l

def Hurwicz(dataframe,alpha):
    d = {}
    for i in dataframe.index:
        d[i] = alpha*min(dataframe.loc[i])+(1-alpha)*max(dataframe.loc[i])
    print(d)
    l = [None] * len(dataframe.index)
    k = 1
    li=[]
    while k<=len(l):
        j = None
        m = None
        n = None
        z = 0
        for i in list(d.keys()):
            if (j is None or j < d[i]) and z not in li :
                j = d[i]
                m = i
                n = z
            z += 1
        print(k)
        li.append(n)
        l[n] = k
        k += 1
    return l
def Laplace(dataframe):
    d = {}
    for i in dataframe.index:
        d[i] = sum(dataframe.loc[i])/len(dataframe.loc[i])
    print(d)
    l = [None] * len(dataframe.index)
    k = 1
    li=[]
    while k<=len(l):
        j = None
        m = None
        n = None
        z = 0
        for i in list(d.keys()):
            if (j is None or j < d[i]) and z not in li :
                j = d[i]
                m = i
                n = z
            z += 1
        print(k)
        li.append(n)
        l[n] = k
        k += 1
    return l
def maximax(dataframe):
    d = {}
    for i in dataframe.index:
        d[i] = max(dataframe.loc[i])
    print(d)
    l = [None] * len(dataframe.index)
    k = 1
    li=[]
    while k<=len(l):
        j = None
        m = None
        n = None
        z = 0
        for i in list(d.keys()):
            if (j is None or j < d[i]) and z not in li :
                j = d[i]
                m = i
                n = z
            z += 1
        print(k)
        li.append(n)
        l[n] = k
        k += 1
    return l
def Bernoulli(df):
    d = {}
    dataframe= 0.1+(df - df.min()) / (df.max() - df.min())
    for i in dataframe.index:
        d[i] = sum([math.log(x) for x in dataframe.loc[i]])/len(dataframe.loc[i])
    l = [None] * len(dataframe.index)
    k = 1
    li=[]
    while k<=len(l):
        j = None
        m = None
        n = None
        z = 0
        for i in list(d.keys()):
            if (j is None or j < d[i]) and z not in li :
                j = d[i]
                m = i
                n = z
            z += 1
        print(k)
        li.append(n)
        l[n] = k
        k += 1
    return l
        
def Minimax(df):
    max_val=df.max()
    dataframe=max_val-df
    d = {}
    for i in dataframe.index:
        d[i] = max(dataframe.loc[i])
    print(d)
    l = [None] * len(dataframe.index)
    k = 1
    li=[]
    while k<=len(l):
        j = None
        m = None
        n = None
        z = 0
        for i in list(d.keys()):
            if (j is None or j > d[i]) and z not in li :
                j = d[i]
                m = i
                n = z
            z += 1
        print(k)
        li.append(n)
        l[n] = k
        k += 1
    return l   





st.title("Les États de Votre Monde")
n1=st.number_input("Combien d'états avez-vous ?",min_value=1, step=1)
if n1<4:
    colonnes = st.columns(n1)
else:
    colonnes = st.columns(4)
l_colonnes = [None] * (n1)
for i, col in enumerate(colonnes):
    with col:
        for j in range(i,n1,4):
            l_colonnes[j]=st.text_input("Etat "+str(j+1),key=str(j)).strip()
b=True
for i in l_colonnes:
    if (i==None or i.strip()=='' ):
        b=False
        break
if (b):
    st.write("Voici les différents états : ")
    st.success(' || '.join(l_colonnes))
else:
    st.error("Veuillez remplir tous les champs requis")
st.title("Les Différents Choix")
n2=st.number_input("Combien de choix avez-vous ?",min_value=2, step=1)
if n2<4:
    colonnes2 = st.columns(n2)
else:
    colonnes2 = st.columns(4)
l_lignes = [None] * (n2)
for i2, col2 in enumerate(colonnes2):
    with col2:
        for j2 in range(i2,n2,4):
            l_lignes[j2]=st.text_input("Choix "+str(j2+1),key=str((j2+1)*1000))
b2=True
for j in l_lignes:
    if (j==None or  j.strip()==''):
        b2=False
        break

if (b2):
    st.success(' || '.join(l_lignes))
else:
    st.error("Veuillez remplir tous les champs")



if (b&b2):
    st.title("Evaluez vos Préférences")
    st.markdown("<b><div class='streamlit-text-container' style='text-align: center;'>Sur une échelle</div></b>", unsafe_allow_html=True)
    col1_1,col1_2=st.columns(2)
    with col1_1:
        min_val=st.number_input('de :',key='min')
    with col1_2:
        max_val=st.number_input("   à :",key='max',value=100)
    id=500001
    data = [[None] * n1 for _ in range(n2)]
    for k in range(n2):
        st.subheader(l_lignes[k])
        col3=st.columns(min(n1,4))
        for i2, col2 in enumerate(col3):
            with col2:
                for j3 in range(i2,n1,4):
                    id=id+1
                    st.write(l_colonnes[j3])
                    data[k][j3]=svs.vertical_slider(key=id, 
                        default_value=int((min_val+max_val)/2),
                        min_value=min_val, 
                        max_value=max_val,
                        thumb_shape="pill",
                        slider_color= '#0080FF', 
                        track_color='lightgray', #optional
                        thumb_color = 'red' #optional
                        )
    df=pd.DataFrame(data, index=l_lignes,columns=l_colonnes)
    st.subheader("Représentation sous forme de Tableau : ")
    col10, col20, col30 = st.columns([2.5, 5, 1])
    with col20:
        st.write(df)
    G = nx.DiGraph()

# Add nodes
    G.add_node('Individual')
    l_new_nodes = {}
    c = 0
    for index in df.index:
        G.add_node(index)
        G.add_edge('Individual', index)
        c = c + 1
        l_new_nodes[index]=[]
        for colonne in df.columns:
            colonne_node = colonne + ' ' + str(c)
            G.add_node(colonne_node)
            l_new_nodes[index].append(colonne_node)
            G.add_edge(index, colonne_node)

# Define positions of nodes
    pos = {}

# Place Individual at center left
    pos['Individual'] = (0, 0)

# Place indices centered vertically
    y_center = len(df.index)/2
    y_offset = 0.5
    for i, index in enumerate(df.index):
        pos[index] = (2, i - y_center + y_offset)

# Place columns on the right
    x_right = 4
    i=0
    for key, colonne_nodes in l_new_nodes.items():
        for colonne_node in colonne_nodes:
            pos[colonne_node] = (x_right, i)
            i=i+1

# Draw graph
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12, font_weight="bold")

# Display plot in Streamlit
    plt.show()
    st.pyplot(plt)
    st.markdown(
    f"""
    <style>
        .st-eb {{
            text-align: center;
            font-size: 24px;
        }}
    </style>
    """,
    unsafe_allow_html=True)
    on=st.toggle("Analyser")
    if on:
        st.balloons()
        alpha = st.number_input("Choisissez votre alpha pour le critère d'Hurwicz", min_value=0.0, max_value=1.0, value=0.5)
        l=maximin(df)
        df2=pd.DataFrame(index=l_lignes)
        df2['maximin']=l
        l=maximax(df)
        df2["maximax"]=l
        l=Hurwicz(df,alpha)
        df2["Hurwicz"]=l
        l=Laplace(df)
        df2["Laplace"]=l
        l=Bernoulli(df)
        df2["Bernoulli"]=l
        l=Minimax(df)
        df2["Minimax"]=l
        means = df2.mean(axis=1)
        index_of_min_mean = means.idxmin()
        st.write(df2)
        st.write("Vous devriez donc choisir "+index_of_min_mean)




        




    

    









        
        