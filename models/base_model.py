class BaseModel:

    def to_json(self):
        dictionary: dict = self.__dict__
        dictionary.pop('_sa_instance_state')
        return dictionary
