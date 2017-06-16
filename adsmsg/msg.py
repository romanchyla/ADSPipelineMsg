from google.protobuf import json_format

class Msg(object):

    def __init__(self, instance, args, kwargs):
        self.__dict__['_data'] = instance
        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, list) or isinstance(v, tuple):
                    getattr(instance, k).extend(v) #TODO(rca): use some smarter reflection
                else:
                    setattr(instance, k, v)


    def __str__(self):
        return str(self._data)

    def __getattr__(self, key):
        if key == '_data':
            return self._data
        return getattr(self._data, key)

    def __setattr__(self, key, value):
        return setattr(self.__dict__['_data'], key, value)


    @classmethod
    def deserializer(cls, data):
        """
        Receives a serialized protocol buffer message and returns an object.
        """
        record = cls()
        record._data.ParseFromString(data)
        return record


    def serialize(self):
        """
        Returns a serialized protocol buffer message
        """
        return self._data.SerializeToString()


    def dump(self):
        """
        Returns (class, serialized-data)
        """
        return ('%s.%s' % (self.__class__.__module__, self.__class__.__name__), self.serialize())


    @staticmethod
    def loads(cls, serialized_data):
        """
        Creates a new instance from the product of self.dump()
        """
        if isinstance(cls, basestring):
            parts = cls.split('.')
            m = __import__('.'.join(parts[0:-1]))
            cls = getattr(m, parts[-1])
        record = cls()
        record._data.ParseFromString(serialized_data)
        return record

    
    def is_valid(self):
        return self._data.IsInitialized()


    @property
    def data(self):
        return self._data


    def toJSON(self):
        return json_format.MessageToJson(self.__dict__['_data'])
