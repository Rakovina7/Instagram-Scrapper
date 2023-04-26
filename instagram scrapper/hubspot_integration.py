from hubspot import HubSpot
from instagram_scraper import scrape_instagram_metrics
import os

hubspot_api_key = os.environ['pat-na1-0527f55e-4259-4c01-9928-37869edd86ea']
api_client = HubSpot(api_key=hubspot_api_key)

def update_contact_metrics(instagram_handle: str, contact_id: str):
    avg_likes, avg_comments = scrape_instagram_metrics(instagram_handle)

    custom_fields = {
        "average_likes": avg_likes,
        "average_comments": avg_comments
    }

    api_client.crm.contacts.basic_api.update(contact_id, custom_fields)
