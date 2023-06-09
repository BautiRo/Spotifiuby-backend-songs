from fastapi import HTTPException, status


class MissingUserId(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_400_BAD_REQUEST, "Missing x-user-id", None)
