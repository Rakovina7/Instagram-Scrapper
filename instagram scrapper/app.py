from flask import Flask, request, jsonify
from celery_app import update_contact_metrics_task

app = Flask(__name__)

@app.route('/update-contact-metrics', methods=['POST'])
def update_contact_metrics_endpoint():
    data = request.get_json()
    instagram_handle = data['instagram_handle']
    contact_id = data['contact_id']

    update_contact_metrics_task.delay(instagram_handle, contact_id)

    return jsonify({"message": "Task queued."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
