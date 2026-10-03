import streamlit as st
import pandas as pd

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["Título"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["Título"] == book]
df_reviews_f = df_reviews[df_reviews["Nome do livro"] == book]

book_title = df_book["Título"].iloc[0]
book_genre = df_book["Gênero"].iloc[0]
book_price = f"${df_book["Preço"].iloc[0]}"
book_rating = df_book["Nota"].iloc[0]
book_year = df_book["Lançamento"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Preço", book_price)
col2.metric("Nota", book_rating)
col3.metric("Lançamento", book_year)

st.divider()
for row in df_reviews_f.values:
      message = st.chat_message(f"{row[4]}")
      message.write(f"**{row[2]}**")
      message.write(row[5])