from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging
import os
import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Callback functions for MQTT
def on_connect(client, userdata, flags, rc):
    log.info("Connected to MQTT broker with result code: %s", rc)

def on_publish(client, userdata, mid):
    log.info("Message published with mid: %s", mid)

# Read MQTT configuration from environment variables
mqtt_broker = os.getenv("MQTT_BROKER", "172.16.1.119")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_topic = os.getenv("MQTT_TOPIC", "EZVIZ")
mqtt_username = os.getenv("MQTT_USERNAME", "user")
mqtt_password = os.getenv("MQTT_PASSWORD", "passwd")

# Initialize MQTT client with versioned callback API
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Register callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

# Set MQTT username and password
mqtt_client.username_pw_set(mqtt_username, mqtt_password)

# Connect to the broker
mqtt_client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT client loop
mqtt_client.loop_start()

# Helper function to recursively publish JSON to MQTT
def publish_json(client, base_topic, key, value, retain=True):
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            publish_json(client, base_topic, f"{key}/{sub_key}", sub_value, retain)
    elif isinstance(value, list):
        if not value:  # If the list is empty
            topic = f"{base_topic}/{key}"
            result, mid = client.publish(topic, "[]", retain=retain)
            if result == mqtt.MQTT_ERR_SUCCESS:
                log.info("Published empty list to topic: %s", topic)
            else:
                log.error("Failed to publish to topic: %s", topic)
        else:
            for index, item in enumerate(value):
                publish_json(client, base_topic, f"{key}/{index}", item, retain)
    else:
        topic = f"{base_topic}/{key}"
        payload = str(value)  # Convert value to string
        result, mid = client.publish(topic, payload, retain=retain)
        if result == mqtt.MQTT_ERR_SUCCESS:
            log.info("Published to topic: %s with payload: %s", topic, payload)
        else:
            log.error("Failed to publish to topic: %s", topic)

# HTTP server request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        headers = self.headers

        log.info("Message received at %s, Headers: %s, Body: %s",
                 self.log_date_time_string(),
                 json.dumps(dict(headers)),
                 body)

        try:
            receive_message = json.loads(body)  # Parse JSON body

            # Extract deviceId and type from the header
            device_id = receive_message.get('header', {}).get('deviceId', 'unknown')
            message_type = receive_message.get('header', {}).get('type', 'unknown')

            # Construct the base MQTT topic dynamically
            base_topic = f"{mqtt_topic}/{device_id}/{message_type}"
            log.info("Constructed base MQTT topic: %s", base_topic)

            # Iterate over the body data and publish to MQTT
            body_data = receive_message.get('body', {})
            for key, value in body_data.items():
                publish_json(mqtt_client, base_topic, key, value)

        except Exception as e:
            log.error("Error processing message: %s", e)
            self.send_response(500)  # Internal server error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = json.dumps({"error": "Internal Server Error", "message": str(e)})
            self.wfile.write(error_response.encode('utf-8'))
            return

        # Respond to the client
        message_id = receive_message.get('header', {}).get('messageId', '')
        result = {"messageId": message_id}
        response = json.dumps(result)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        log.info("Response sent: %s", json.dumps(result))

# Function to run the HTTP server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=7777):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
