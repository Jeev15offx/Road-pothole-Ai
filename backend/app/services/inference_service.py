async def run_inference(image_bytes: bytes):
    # Temporary fake result
    return [
        {
            "x": 120,
            "y": 200,
            "width": 50,
            "height": 40,
            "confidence": 0.92,
            "class_name": "pothole"
        }
    ]