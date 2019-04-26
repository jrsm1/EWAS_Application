class noPowerException(Exception):
    """Exception to raise when suspicious power issues with Control Module."""
    def __init__(self, message):
        super().__init__(message)
