from core.interfaces.repository import ExampleRepositoryInterface
from core.models.example import Example

class ExampleRepository(ExampleRepositoryInterface):
    """
    Implementación concreta del repositorio utilizando almacenamiento en memoria
    como ejemplo.
    """

    def __init__(self):
        self._storage = {}

    def get_by_id(self, example_id: int) -> Example:
        example = self._storage.get(example_id)
        if not example:
            raise ValueError(f"Example with ID {example_id} not found.")
        return example

    def save(self, example: Example) -> None:
        self._storage[example.id] = example
