import cocinero

class CocineroFactory:
    @staticmethod
    def create_cocinero() -> cocinero.Cocinero:
        return cocinero.CocineroAragones('Adrián')