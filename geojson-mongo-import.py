import geopandas as gpd

def convert_geojson(input_file, output_file, from_crs, to_crs='EPSG:4326'):
    """
    Convert a GeoJSON file from one CRS to another.

    :param input_file: Path to the input GeoJSON file.
    :param output_file: Path where the output GeoJSON file will be saved.
    :param from_crs: The EPSG code of the input file's CRS (e.g., 'EPSG:32633' for UTM zone 33N).
    :param to_crs: The EPSG code of the target CRS, default is 'EPSG:4326' (WGS 84).
    """
    # Load the GeoJSON file
    gdf = gpd.read_file(input_file)
    
    # Set the CRS for the GeoDataFrame if it's not automatically detected
    if not gdf.crs:
        gdf.set_crs(from_crs, inplace=True)

    # Transform the geometries to the target CRS
    gdf.to_crs(to_crs, inplace=True)

    # Save the transformed GeoDataFrame to a new GeoJSON file
    gdf.to_file(output_file, driver='GeoJSON')

# Example usage
input_geojson = 'input.geojson'  # Update this path
output_geojson = 'output.geojson'  # Update this path
from_crs_code = 'EPSG:32633'  # Example: UTM zone 33N, update this EPSG code according to your data

convert_geojson(input_geojson, output_geojson, from_crs_code)

# geopandas.read_file(input_file): Loads the GeoJSON file into a GeoDataFrame.
# gdf.set_crs(from_crs, inplace=True): Assigns the specified CRS to the GeoDataFrame if it isn't already set.
# gdf.to_crs(to_crs, inplace=True): Converts the geometries in the GeoDataFrame to the specified target CRS.
# gdf.to_file(output_file, driver='GeoJSON'): Saves the converted GeoDataFrame to a new GeoJSON file.