
class Msg(object):

    def __init__(self):
        self._data = None

    @classmethod
    def adsbuffer_deserializer(cls, data):
        """
        Receives a serialized protocol buffer message and returns an object.
        """
        record = cls()
        record._data.ParseFromString(data)
        return record

    @classmethod
    def adsbuffer_serializer(cls, record):
        """
        Receives an object and return a serialized protocol buffer message.
        """
        return record.SerializeToString()


    def SerializeToString(self):
        """
        Returns a serialized protocol buffer message
        """
        return self._data.SerializeToString()

