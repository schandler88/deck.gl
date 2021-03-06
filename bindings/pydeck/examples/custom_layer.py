import pydeck

# See https://github.com/ajduberstein/pydeck_custom_layer for a minimal example layer

pydeck.settings.custom_libraries = [
    {
        "libraryName": "LabeledGeoJsonLayerLibrary",
        "resourceUri": "https://unpkg.com/pydeck-custom-layer-demo@0.0.1/dist/bundle.js",
    }
]

DATA_URL = (
    "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
)

custom_layer = pydeck.Layer(
    "LabeledGeoJsonLayer",
    data=DATA_URL,
    filled=False,
    billboard=False,
    get_line_color=[180, 180, 180],
    get_label="properties.name",
    get_label_size=200000,
    get_label_color=[0, 64, 128],
    label_size_units='"meters"',
    line_width_min_pixels=1,
)

view_state = pydeck.ViewState(latitude=0, longitude=0, zoom=1, bearing=-45, pitch=60,)

r = pydeck.Deck(
    custom_layer,
    initial_view_state=view_state,
    map_style="",
)

r.to_html('custom_layer.html', css_background_color="#333")
