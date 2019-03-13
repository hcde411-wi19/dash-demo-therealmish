# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/data_car_2004.csv')
cols = []
for i, col in enumerate(df.columns):
    if i == 1 or i == 2 or i == 3:
        cols.append(col)

finaldf = pd.DataFrame(columns=cols)

hp = {"Sedan": 0, "Sports Car": 0, "SUV": 0}
cityMPG = {"Sedan": 0, "Sports Car": 0, "SUV": 0}
hwyMPG = {"Sedan": 0, "Sports Car": 0, "SUV": 0}

sedCount = 1
suvCount = 1
sportCount = 1

for row in df.iterrows():
    if row[1]["Sedan"] == 1:
        sedCount += 1
        hp["Sedan"] = (hp["Sedan"] * (sedCount - 1) + row[1]["HP"]) / sedCount
        cityMPG["Sedan"] = (cityMPG["Sedan"] * (sedCount - 1) + row[1]["City MPG"]) / sedCount
        hwyMPG["Sedan"] = (hwyMPG["Sedan"] * (sedCount - 1) + row[1]["Hwy MPG"]) / sedCount

    elif row[1]["Sports Car"] == 1:
        sportCount += 1
        hp["Sports Car"] = (hp["Sports Car"] * (sportCount - 1) + row[1]["HP"]) / sportCount
        cityMPG["Sports Car"] = (cityMPG["Sports Car"] * (sportCount - 1) + row[1]["City MPG"]) / sportCount
        hwyMPG["Sports Car"] = (hwyMPG["Sports Car"] * (sportCount - 1) + row[1]["Hwy MPG"]) / sportCount

    elif row[1]["SUV"] == 1:
        suvCount += 1
        hp["SUV"] = (hp["SUV"] * (suvCount - 1) + row[1]["HP"]) / suvCount
        cityMPG["SUV"] = (cityMPG["SUV"] * (suvCount - 1) + row[1]["City MPG"]) / suvCount
        hwyMPG["SUV"] = (hwyMPG["SUV"] * (suvCount - 1) + row[1]["Hwy MPG"]) / suvCount


hp = [hp[key] for key in hp.keys()]
cityMPG = [cityMPG[key] for key in cityMPG.keys()]
hwyMPG = [hwyMPG[key] for key in hwyMPG.keys()]


app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Dash Exercise 2'),

    # a div to put a short description
    html.Div(children='''
        Average HP, City MPG, and Highway MPG for Different Car Types
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': cols, 'y': hp, 'type': 'bar', 'name': 'Horse Power'},
                {'x': cols, 'y': cityMPG, 'type': 'bar', 'name': 'City MPG'},
                {'x': cols, 'y': hwyMPG, 'type': 'bar', 'name': 'Highway MPG'},

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Average HP, City MPG, and Highway MPG for Different Car Types'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)

