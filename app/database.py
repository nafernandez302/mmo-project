from app.models.base import DBManager

_server = None

def get_db():
    """
    Returns database connection.
    """
    global _server
    if _server is None:
        _server = DBManager()
    return _server.db
