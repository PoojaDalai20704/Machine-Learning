import warnings
from tensorflow.keras.utils import pad_sequenc
es
from tensorflow.keras.preprocessing.text impor
t Tokenizer
from sklearn.model_selection import train_test
_split
import tensorflow as tf
from tensorflow import keras import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns
import plotly.express as px import numpy as np
import re import nltk
nltk.download('all')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize from nltk.stem import WordNetLemmatizer lemm = WordNetLemmatizer() warnings.filterwarnings("ignore")
data = pd.read_csv("/content/drive/MyDrive/Sal ary_Data (1).csv")
data.head(7) print(data.shape)
data = data[data['Salary'].isnull() == False] sns.countplot(data=data, x='Salary') plt.xticks(rotation=90)
plt.show() plt.subplots(figsize=(12, 5))
plt.subplot(1, 2, 1) sns.countplot(data=data, x='Salary') plt.subplot(1, 2, 2)
 
sns.countplot(data=data, x="Salary") plt.show()
fig = px.histogram(data, x="Age", marginal='box', title="Age Group", color="Rating", nbins=65-18, color_discrete_sequence\
=['black', 'green', 'blue', 'red', 'ye
llow'])
fig.update_layout(bargap=0.2) def filter_score(rating):
return int(rating > 3)

features = ['Class Name', 'Title', 'Review Tex
 
t']

















wer)
 

X = data[features] y = data['Rating']
y = y.apply(filter_score) def toLower(data):
if isinstance(data, float): return '<UNK>'
else:
return data.lower()
stop_words = stopwords.words("english") def remove_stopwords(text):
no_stop = []
for word in text.split(' '): if word not in stop_words:
no_stop.append(word) return " ".join(no_stop)
def remove_punctuation_func(text):
return re.sub(r'[^a-zA-Z0-9]', ' ', text)
X['Title'] = X['Title'].apply(toLower) X['Review Text'] = X['Review Text'].apply(toLo
 
X['Title'] = X['Title'].apply(remove_stopwords
)
X['Review Text'] = X['Review Text'].apply(remo
ve_stopwords)
X['Title'] = X['Title'].apply(lambda x: lemm.l emmatize(x))
X['Review Text'] = X['Review Text'].apply(lamb da x: lemm.lemmatize(x))
X['Title'] = X['Title'].apply(remove_punctuati on_func)
X['Review Text'] = X['Review Text'].apply(remo ve_punctuation_func)
X['Text'] = list(X['Title']+X['Review Text']+X ['Class Name'])
X_train, X_test, y_train, y_test = train_test_ split(
X['Text'], y, test_size=0.25, random_state=4
2)
tokenizer = Tokenizer(num_words=10000, oov_tok
en='<OOV>')
tokenizer.fit_on_texts(X_train)
train_seq = tokenizer.texts_to_sequences(X_tra
 
in)

)
 
test_seq = tokenizer.texts_to_sequences(X_test train_pad = pad_sequences(train_seq,
maxlen=40, truncating="post", padding="post")
test_pad = pad_sequences(test_seq, maxlen=40, truncating="post", padding="post")

model = keras.models.Sequential() model.add(keras.layers.Embedding(10000, 128)) model.add(keras.layers.SimpleRNN(64, return_se
 
quences=True))
model.add(keras.layers.SimpleRNN(64))
 
model.add(keras.layers.Dense(128, activation=" relu"))
model.add(keras.layers.Dropout(0.4)) model.add(keras.layers.Dense(1, activation="si
gmoid"))
model.summary() model.compile("rmsprop",
"binary_crossentropy", metrics=["accuracy"])
history = model.fit(train_pad, y_train,
epochs=5)
model = keras.models.Sequential() model.add(keras.layers.Embedding(10000, 128)) model.add(keras.layers.Bidirectional(
keras.layers.LSTM(64, return_sequences=True)
))
model.add(keras.layers.Bidirectional(keras.lay
ers.LSTM(64)))
model.add(keras.layers.Dense(128, activation=" relu"))
model.add(keras.layers.Dropout(0.4)) model.add(keras.layers.Dense(1, activation="si
gmoid"))
model.compile("rmsprop", "binary_crossentropy"
, metrics=["accuracy"])
history = model.fit(train_pad, y_train, epochs
 
=5)
 

model = keras.models.Sequential() model.add(keras.layers.Embedding(10000, 128)) model.add(keras.layers.Bidirectional(
keras.layers.GRU(64,
 
return_sequences=True))) model.add(keras.layers.Bidirectional(keras.lay
ers.GRU(64)))
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.4))
 
model.add(keras.layers.Dense(1, activation="sigmoid"))
model.compile("rmsprop", "binary_crossentropy", metrics=["accuracy"])
history = model.fit(train_pad, y_train, epochs=5)
