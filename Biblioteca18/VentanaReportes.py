
from tkinter import *
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from Entidades.iteradores.iteradorPrestamosSocio import iteradorPrestamosSocio
from Entidades.iteradores.iteradorSolicitantesLibroParticular import iteradorSolicitantesLibroParticular
from Entidades.iteradores.iteradorCantidadLibrosEstados import IteradorCantidadLibrosEstados
from Entidades.iteradores.iteradorSumatoriaLibrosExtraviados import IteradorSumatoriaLibrosExtraviados
from Entidades.iteradores.iteradorPrestamosDemorados import IteradorPrestamosDemorados
class VentanaReportes:
    def __init__(self, padron):
        self.window = Tk()
        self.window.title("Reportes")
        self.padro = padron

        frame1 = Frame(self.window)
        frame1.pack(pady=20, padx=10)
        frame2 = Frame(frame1)
        frame2.grid(row=3, column=0)
        frame3 = Frame(frame1)
        frame3.grid(row=5, column=0)
        self.socio = IntVar(self.window)
        self.libro = IntVar(self.window)
        Label(frame1, text="Cantidad de libros en cada estado (tres totales)").grid(row=0, column=0)
        Button(frame1, text="Generar", command=self.reporte1).grid(row=0, column=1)
        Label(frame1, text="Sumatoria del precio de reposición de todos los libros extraviados").grid(row=1, column=0)
        Button(frame1, text="Generar", command=self.reporte2).grid(row=1, column=1)
        Label(frame1, text="Nombre de todos los solicitantes de un libro en particular identificado por su título").grid(row=2, column=0)
        Button(frame1, text="Generar", command=self.reporte3).grid(row=2, column=1)
        Label(frame2, text="Libro:").pack(side="left", padx=5)
        Entry(frame2, textvariable=self.libro).pack(side="right", padx=5)
        Label(frame1, text="Listado de préstamos de un socio identificado por su número de socio").grid(row=4, column=0)
        Button(frame1, text="Generar", command=self.reporte4).grid(row=4, column=1)
        Label(frame3, text="Socio:").pack(side="left", padx=5)
        Entry(frame3, textvariable=self.socio).pack(side="right", padx=5)
        Label(frame1, text="Listado de préstamos demorados").grid(row=6, column=0)
        Button(frame1, text="Generar", command=self.reporte5).grid(row=6, column=1)
        
        
    def reporte1(self):
        doc = SimpleDocTemplate("./TPI_DAO_2023/Biblioteca18/ReporteCantidadLibros.pdf", pagesize=letter)
        elements=[]
        styles = getSampleStyleSheet()
        titulo="Estado de libros en la biblioteca"
        elements.append(Paragraph(titulo, styles['Title']))
        espacio = ""
        elements.append(Paragraph(espacio, styles['Normal']))
        iterador=IteradorCantidadLibrosEstados(self.padro.libros)
        contEstados= iterador.contarLibros()
        data=[["Disponibles", "Prestados", "Extraviados"],[contEstados[0],contEstados[1],contEstados[2]]]
        table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(table)
        doc.build(elements)
    def reporte2(self):
        doc = SimpleDocTemplate("./TPI_DAO_2023/Biblioteca18/ReporteSumatoriaLibrosExtraviados.pdf", pagesize=letter)
        elements=[]
        styles = getSampleStyleSheet()
        titulo="Libros extraviados: monto para reposición"
        elements.append(Paragraph(titulo, styles['Title']))
        espacio = ""
        elements.append(Paragraph(espacio, styles['Normal']))
        iterador=IteradorSumatoriaLibrosExtraviados(self.padro.libros)
        datos=iterador.sumarReposiciónLibrosExtraviados()
        texto = "Se han encontrado un total de " + str(datos[0]) + " libros extraviados. El total de reposición es de " + str(datos[1])
        elements.append(Paragraph(texto, styles['Normal']))
        doc.build(elements)
    def reporte3(self):
        doc = SimpleDocTemplate("./TPI_DAO_2023/Biblioteca18/ReporteCantidadLibros.pdf", pagesize=letter)
        elements=[]
        styles = getSampleStyleSheet()
        titulo="Estado de libros en la biblioteca"
        elements.append(Paragraph(titulo, styles['Title']))
        espacio = ""
        elements.append(Paragraph(espacio, styles['Normal']))
        iterador=iteradorSolicitantesLibroParticular(self.padro.prestamos)
        lista= iterador.listaSolicitantesLibro(self.libro.get())
        messagebox.showinfo(title="Reporte", message=lista)
        # data=[["Disponibles", "Prestados", "Extraviados"],[contEstados[0],contEstados[1],contEstados[2]]]
        # table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
        # table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        #                         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        #                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        #                         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        #                         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        #                         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        #                         ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        # elements.append(table)
        doc.build(elements)
    def reporte4(self):
        doc = SimpleDocTemplate("./TPI_DAO_2023/Biblioteca18/ReportePrestamosSocioParticular.pdf", pagesize=letter)
        elements=[]
        styles = getSampleStyleSheet()
        titulo="Listado de prestamos por socio"
        elements.append(Paragraph(titulo, styles['Title']))
        espacio = ""
        elements.append(Paragraph(espacio, styles['Normal']))
        iterador=iteradorPrestamosSocio(self.padro.prestamos)
        lista= iterador.listaPrestamosSocio(self.socio.get())
        messagebox.showinfo(title="Reporte", message=lista)
        # data=[["Disponibles", "Prestados", "Extraviados"],[contEstados[0],contEstados[1],contEstados[2]]]
        # table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
        # table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        #                         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        #                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        #                         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        #                         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        #                         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        #                         ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        # elements.append(table)
        #doc.build(elements)
    def reporte5(self):
        doc = SimpleDocTemplate("./TPI_DAO_2023/Biblioteca18/ListaPrestamosDemorados.pdf", pagesize=letter)
        elements=[]
        styles = getSampleStyleSheet()
        titulo="Lista de prestamos demorados"
        elements.append(Paragraph(titulo, styles['Title']))
        espacio = ""
        elements.append(Paragraph(espacio, styles['Normal']))
        iterador=IteradorPrestamosDemorados(self.padro.prestamos)
        lista=iterador.listaPrestamosDemorados()
        datos=[["Titulo del libro", "Dias de demora"]]
        for d in lista:
            datos.append(d)
        table = Table(datos, colWidths=[1 * inch, 1 * inch, 1 * inch])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(table)
        doc.build(elements)
    
    def mostrar(self):
        self.window.mainloop()
        
