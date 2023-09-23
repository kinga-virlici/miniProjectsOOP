from abc import ABC, abstractmethod

class GradinitaABC(ABC):

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError('Metoda nu este implementata')



