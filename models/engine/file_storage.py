#!/usr/bin/python3
"""FileStorage module (class and its functions)"""
from os import path
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects with all objects stored"""
        return self.__objects

    def new(self, obj):
        """sets in dictionary __objects the object
        with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes dictionary __objects to the
        JSON file (path: __file_path)"""
        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """deserializes (reads) the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception is raised"""
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                content_catcher = file.read()
                if len(content_catcher) == 0:
                    return
                models_json = json.loads(content_catcher)
            for model in models_json.values():
                class_name = model["__class__"]
                self.new(eval(class_name)(**model))
        except FileNotFoundError:
            return
