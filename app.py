import os

def main():
    version = os.getenv("APP_VERSION", "dev")
    api_key = os.getenv("API_KEY", "no-key")
    print(f"Deploying version {version}")
    print(f"Using secret key: {api_key}")

if __name__ == "__main__":
    main()