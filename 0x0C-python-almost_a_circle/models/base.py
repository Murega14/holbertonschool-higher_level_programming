#!/usr/bin/python3
"""class base"""
import json


class Base:
    """this is inside the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """returns list of jsons"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """makes instance"""
        newCreate = cls(1,1)
        newCreate.update(**dictionary)
        return newCreate

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        try:
            jsons = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            jsons = '[]'
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            f.write(jsons)
    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []