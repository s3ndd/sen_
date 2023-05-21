import uuid

from sqlalchemy import TypeDecorator, BINARY


class GUID(TypeDecorator):
    """
    Platform-independent GUID type.
    Uses MySQL's BINARY(16) type
    """
    impl = BINARY(16)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value.bytes

    def process_result_value(self, value, dialect):
        if value is not None:
            return uuid.UUID(bytes=value)
