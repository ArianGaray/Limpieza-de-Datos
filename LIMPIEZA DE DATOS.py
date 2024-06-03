#!/usr/bin/env python
# coding: utf-8

# **<h1><center>LIMPIEZA DE DATOS**

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


url = r"C:\Users\arian\OneDrive\Escritorio\Python\Proyectos\Limpieza\dataset_banco.csv"
data = pd.read_csv(url)
data.head(10)


# In[7]:


data.info()


# <h2>1. Datos Faltantes

# In[11]:


data.dropna(inplace=True)
data.info()


# <h2>2. Columnas irrelevantes

# In[15]:


#Averiguar si las columnas tienen 1 o más niveles
cat_string = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome','y']
for col in cat_string:
    print(f'Columna {col}: {data[col].nunique()} subniveles')


# In[17]:


data.describe().round(2)


# <h2>3. Datos faltantes

# In[18]:


print(f'Tamaño de la tabla antes de eliminar las filas repetidas: {data.shape}')
data.drop_duplicates(inplace = True)
print(f'Tamaño de la tabla después de eliminar las filas repetidas: {data.shape}')


# <h2>4. Valores extremos

# In[19]:


#Vamos a generar gráficas individuales ya que cada tipo de variable es diferente
columnas_numericas = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
fig, ax = plt.subplots(nrows=7, ncols=1, figsize=(8,30))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(columnas_numericas):
    sns.boxplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(col)


# Observaciones:
#     Gráfica 1: edades mayores a 100 años
#     Gráfica 2: todo ok
#     Gráfica 3: todo ok
#     Gráfica 4: hay valores negativos
#     Gráfica 5: todo ok
#     Gráfica 6: todo ok
#     Gráfica 7: valor casi de 300

# In[21]:


#Para la gráfica 1
print(f'Tamaño de la tabla antes de eliminar registros de edad: {data.shape}')
data = data[data['age']<=100]
print(f'Tamaño de la tabla después de eliminar registros de edad: {data.shape}')


# In[22]:


#Para la gráfica 4
print(f'Tamaño de la tabla antes de eliminar registros de duracion: {data.shape}')
data = data[data['duration']>0]
print(f'Tamaño de la tabla después de eliminar registros de duracion: {data.shape}')


# In[23]:


#Para la gráfica 7
print(f'Tamaño de la tabla antes de eliminar registros de previous: {data.shape}')
data = data[data['previous']<=100]
print(f'Tamaño de la tabla después de eliminar registros de previous: {data.shape}')


# <h2>5. Errores tipográficos en variables categóricas

# In[24]:


cols_cat = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome','y']

fig, ax = plt.subplots(nrows=10,ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
    sns.countplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30)


# In[25]:


#Esto es para colocar las palabras que están en mayúsculas a minúsculas
for column in data.columns:
    if column in cols_cat:
        data[column] = data[column].str.lower()
fig, ax = plt.subplots(nrows=10,ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
    sns.countplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30)


# In[26]:


#gráfico JOB: unificar admin y administrative
print(data['job'].unique())

data['job']= data['job'].str.replace('admin.','administrative', regex =False)
print(data['job'].unique())


# In[32]:


#gráfico MARITAL: unificar div. y divorced
print(data['marital'].unique())

data['marital']= data['marital'].str.replace('divorced.','divorced', regex =False)
print(data['marital'].unique())


# In[35]:


#gráfico EDUCATION: unificar secondary y sec
print(data['education'].unique())

data['education']= data['education'].str.replace('sec.','secondary', regex =False)
data['education']= data['education'].str.replace('unknownnown','unknown', regex =False)
print(data['education'].unique())


# In[36]:


#gráfico CONTACT: unificar (cellular y mobile) y (telephone y phone)
print(data['contact'].unique())

data['contact']= data['contact'].str.replace('cellular','mobile', regex =False)
data['contact']= data['contact'].str.replace('telephone','phone', regex =False)

print(data['contact'].unique())


# In[38]:


#gráfico POUTCOME: unificar unknown y unk
print(data['poutcome'].unique())

data['poutcome']= data['poutcome'].str.replace('unknownnown','unknown', regex =False)

print(data['poutcome'].unique())


# In[39]:


cols_cat = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome','y']

fig, ax = plt.subplots(nrows=10,ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
    sns.countplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30)


# In[40]:


data.shape


# In[5]:


ruta = r"C:\Users\arian\OneDrive\Escritorio\Python\Proyectos\Limpieza\data_limpia.csv"
data.to_csv(ruta)


# In[ ]:




