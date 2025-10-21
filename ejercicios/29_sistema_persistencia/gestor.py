from abc import ABC, abstractmethod
from movie import Movie

class GestorPersistenciaBase(ABC):
    @abstractmethod
    def create(self, movie : Movie):
        pass

    @abstractmethod
    def find_by_title(self, title : str):
        pass

    @abstractmethod
    def delete(self, title : str):
        pass

    @abstractmethod
    def update(self, updated_movie : Movie):
        pass