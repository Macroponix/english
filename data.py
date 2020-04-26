import pandas as pd

df_books = pd.read_csv('books.txt', sep='\t')
df_books.Word = [str(word).lower() for word in df_books.Word]
df_subtitles = pd.read_csv('subtitles.txt', sep=' ', names=['Word', 'Count'])
df_subtitles['Rank'] = range(1, len(df_subtitles) + 1)
df = df_books.join(df_subtitles.set_index('Word'), on='Word', lsuffix='_books', rsuffix='_subtitles')

print(df[df.isnull().any(axis=1)])
