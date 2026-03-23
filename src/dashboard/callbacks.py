from dash import Input, Output
import plotly.express as px

def register_callbacks(app, df):

    @app.callback(
        Output("price-distribution", "figure"),
        Output("price-map", "figure"),
        Input("fuel-filter", "value"),
        Input("region-filter", "value"),
    )
    def update_dashboard(fuel, region):

        filtered = df[
            (df["carburant"] == fuel) &
            (df["region"] == region)
        ]

        # Histogram
        fig_hist = px.histogram(
            filtered,
            x="prix",
            nbins=30,
            title="Price Distribution"
        )

        # Map
        fig_map = px.scatter_mapbox(
            filtered,
            lat="latitude",
            lon="longitude",
            color="prix",
            hover_name="ville",
            zoom=5,
            height=500
        )

        fig_map.update_layout(mapbox_style="open-street-map")

        return fig_hist, fig_map
