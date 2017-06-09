
class Msg(object):

    def __init__(self):
        self._data = None

    @classmethod
    def deserializer(cls, data):
        """
        Receives a serialized protocol buffer message and returns an object.
        """
        record = cls()
        record._data.ParseFromString(data)
        return record

    @classmethod
    def serializer(cls, record):
        """
        Receives an object and return a serialized protocol buffer message.
        """
        return record.serialize()


    def serialize(self):
        """
        Returns a serialized protocol buffer message
        """
        return self._data.SerializeToString()

    def is_valid(self):
        return self._data.IsInitialized()

    @property
    def data(self):
        return self._data
