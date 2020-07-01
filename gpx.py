import os
import gpxpy
import pandas as pd

import constants


def get_trail_paths():
    dataframes = []

    for filename in os.listdir(constants.DATA_FOLDER):
        if filename.endswith(constants.DATA_EXTENSION):
            file_path = os.path.join(constants.DATA_FOLDER, filename)
            print "Reading %s" % file_path
            gpx_file = open(file_path)
            gpx = gpxpy.parse(gpx_file)
            for track in gpx.tracks:
                for segment in track.segments:
                    longitudes = []
                    latitudes = []
                    hikes = []
                    for point in segment.points:
                        longitudes.append(point.longitude)
                        latitudes.append(point.latitude)
                        hikes.append(filename)
                    df = pd.DataFrame({
                        'lon': longitudes,
                        'lat': latitudes,
                        'hike': hikes
                        })
                    dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)
