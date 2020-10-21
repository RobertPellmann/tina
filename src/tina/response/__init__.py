from flask import Response

STATUS_NOT_ALLOWED = 405

class NotAllowed(Response):
    def __init__(self):
        super().__init__(status=405)