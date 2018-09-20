from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "http://gis-pkc.opendata.arcgis.com/datasets.json?q=polling&sort_by=-updatedAt"
stations_url = "http://gis-pkc.opendata.arcgis.com/datasets/909e45688aa646199cad8e8616ddef7a_0.geojson"
districts_url = "http://gis-pkc.opendata.arcgis.com/datasets/6dac129ea3cb492b961186e316e09690_0.geojson"
council_id = 'S12000024'


search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape()
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
