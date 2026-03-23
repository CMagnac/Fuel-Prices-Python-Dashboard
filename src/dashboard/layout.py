from dash import html, dcc

def create_layout(df):

    fuels = sorted(df["carburant"].dropna().unique())
    regions = sorted(df["region"].dropna().unique())

    return html.Div([

        html.H1("Fuel Price Dashboard", style={"textAlign": "center"}),

        # Filters
        html.Div([
            dcc.Dropdown(
                id="fuel-filter",
                options=[{"label": f, "value": f} for f in fuels],
                value=fuels[0],
                placeholder="Select fuel"
            ),

            dcc.Dropdown(
                id="region-filter",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0],
                placeholder="Select region"
            ),
        ], style={"display": "flex", "gap": "10px"}),

        # Graphs
        dcc.Graph(id="price-distribution"),
        dcc.Graph(id="price-map"),
    ])
