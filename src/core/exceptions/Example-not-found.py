class ExampleNotFoundError(Exception):
    """
    Excepción personalizada para manejar el caso donde no se encuentra un ejemplo.
    """
    def __init__(self, example_id):
        super().__init__(f"Example with ID {example_id} not found.")
        self.example_id = example_id