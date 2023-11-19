class iteradorSolicitantesLibroParticular:
    def __init__(self, listaPrestamos):
        self.listaPrestamos=listaPrestamos

    def listaSolicitantesLibro(self, codLib):
        solicitantes=[]
        for prestamo in self.listaPrestamos:
            if prestamo.libro.codigo == codLib:
                socio=prestamo.socio
                nombreSocio=str(socio.nombre) + " " + str(socio.apellido)
                solicitantes.append(nombreSocio)
        return solicitantes