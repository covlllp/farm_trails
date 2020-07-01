import plotly.express as px

import constants

from gpx import get_trail_paths


df = get_trail_paths()

fig = px.line_mapbox(
    data_frame=df,
    lat="lat",
    lon="lon",
    color_discrete_sequence=['red'],
    line_group="hike",
    center={
        "lon": constants.CENTER_LONGITUDE,
        "lat": constants.CENTER_LATITUDE
        },
    zoom=constants.MAP_ZOOM
    )
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
