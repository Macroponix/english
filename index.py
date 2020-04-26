import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from app import app
from data import df

fig = go.Figure(data=[
                go.Scatter(
                    mode='markers',
                    x=df.Rank_books,
                    y=df.Rank_subtitles,
                    text=df.Word,
                    hovertemplate =
                    '<i>Word</i>: %{text}'+
                    '<br><b>Rank in books</b>: %{x}'+
                    '<br><b>Rank in subtitles</b>: %{y}',
                    showlegend=False,
                    )
                ])

fig.update_layout(
    width=1000,
    height=1000,

)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[
        dcc.Graph(
            id='main',
            figure=fig,
        )
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
