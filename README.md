# FastAPI Project

## Overview
This is an open - source project based on FastAPI. The main functionality is to count the number of hot dogs in an image given its URL. It uses OpenCV for image processing and provides a simple API through FastAPI.
这是一个基于 FastAPI 的开源项目。其主要功能是根据给定的图片 URL，统计图片中热狗的数量。该项目使用 OpenCV 进行图像处理，并通过 FastAPI 提供一个简单的 API 接口。
## Project Structure

## Installation
### Clone the project
The service will start at `http://0.0.0.0:8000`
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