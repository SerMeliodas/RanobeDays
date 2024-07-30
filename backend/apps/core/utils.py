def get_response_data(status: int, data: dict | None = None, detail: str | None = None) -> dict:
    return {
        "status": status,
        "detail": detail or "",
        "data": data or [],
    }
