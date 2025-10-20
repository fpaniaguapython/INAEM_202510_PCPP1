class Factura:
    iva_general = 21
    def __init__(self, numero_factura, importe):
        self.numero_factura = numero_factura
        self.importe = importe

    def generar_pdf(self):
        print('Generando pdf...')

    @classmethod
    def mostrar_iva_general(cls):
        print(cls.iva_general)

    @staticmethod
    def saludar():
        print('Hola, soy una factura')


factura_1 = Factura(100, 10_000)
factura_1.generar_pdf()
Factura.mostrar_iva_general()
Factura.saludar()
