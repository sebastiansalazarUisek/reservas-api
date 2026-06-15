from fastapi import HTTPException

def validate_exists(item, message: str):
    if item is None:
        raise HTTPException(
            status_code=404,
            detail=message
        )

    return item