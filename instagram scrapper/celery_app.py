from celery import Celery

celery_app = Celery('instagram_tasks', broker='redis://localhost:6379/0')

@celery_app.task
def update_contact_metrics_task(instagram_handle: str, contact_id: str):
    from hubspot_integration import update_contact_metrics
    update_contact_metrics(instagram_handle, contact_id)
