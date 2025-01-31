from abc import ABC, abstractmethod
from core.models.example import Example

class ExampleRepositoryInterface(ABC):
    """
    Define la interfaz que debe implementar cualquier repositorio
    relacionado con la entidad Example.
    """

    @abstractmethod
    def get_by_id(self, example_id: int) -> Example:
        pass

    @abstractmethod
    def save(self, example: Example) -> None:
        pass