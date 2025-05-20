def track_usage(func):
    async def wrapper(*args, **kwargs):
        print("Tracking usage for this request...")
        result = await func(*args, **kwargs)
        return result
    return wrapper
