class iteradorSolicitantesLibroParticular:
    def __int__(self, listaPrestamos: list, listaSocios:list):
        self.listaPrestamos=listaPrestamos

    def listaSolicitantesLibro(self, codLib: int):
        solicitantes=[]
        for prestamo in self.listaPrestamos:
            if prestamo.libro.get_codigo() == codLib:
                socio=prestamo.socio
                nombreSocio=str(socio.nombre) + " " + str(socio.apellido)
                solicitantes.append(nombreSocio)
        return solicitantes