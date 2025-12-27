import os
from flask import Flask


def main():
    version = os.getenv("APP_VERSION", "dev")
    api_key = os.getenv("API_KEY", "no-key")
    print(f"Deploying version {version}")
    print(f"Using secret key: {api_key}")

# Flask app for service mode
app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "dev")
    api_key = os.getenv("API_KEY", "no-key")
    return f"Deploying version {version}, Using secret key: {api_key}"

if __name__ == "__main__":
    # Decide mode based on ENV variable
    mode = os.getenv("RUN_MODE", "job")
    if mode == "service":
        app.run(host="0.0.0.0", port=5000)
    else:
        main()
