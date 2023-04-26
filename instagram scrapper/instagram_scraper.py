import instascrape
from typing import Tuple

def scrape_instagram_metrics(instagram_handle: str) -> Tuple[float, float]:
    user = instascrape.Profile(instagram_handle)
    user.scrape()

    recent_posts = user.get_recent_posts()[:20]

    total_likes = sum(post.likes for post in recent_posts)
    total_comments = sum(post.comments for post in recent_posts)

    avg_likes = total_likes / len(recent_posts)
    avg_comments = total_comments / len(recent_posts)

    return avg_likes, avg_comments
