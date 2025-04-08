# FastAPI Project

## Overview
This is an open - source project based on FastAPI. The main functionality is to count the number of hot dogs in an image given its URL. It uses OpenCV for image processing and provides a simple API through FastAPI.

## Project Structure

## Installation
### Clone the project
git clone <repository_url>
cd FastAPIProject
python -m venv .venv
.venv\Scripts\activate
source .venv/bin/activate
pip install fastapi uvicorn opencv - python - headless pydantic

The service will start at `http://0.0.0.0:8000`.
K
## API Endpoints
### Count Hot Dogs (`POST /getHotDogCount`)
Request body:
```json

{
    "image_url": "https://example.com/image.jpg"
}

```
Response body:
```json
{
    "HotDogCount": 3
}
```

## Testing
You can use the requests in test_main.http to test the API endpoints. Make sure the service is running, then execute the requests in an editor that supports HTTP request files.

## Contributing
Contributions are welcome! If you have suggestions for improvement or find issues, please submit an issue or a pull request.

## License
This project is licensed under the MIT License. https://opensource.org/license/MIT 