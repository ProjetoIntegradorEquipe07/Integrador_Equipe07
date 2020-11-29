from fpdf import FPDF, HTMLMixin
from datetime import datetime

from mod_comanda.comandaBD import Comanda



class PDF(FPDF, HTMLMixin):
    
    def header(self):
        self.image("static/imgs/pastelaria-logo-2.png", 10, 8, 20)
        self.set_font('arial', 'B', 15)
        self.cell(0, 5, 'Pastelaria do Zé', 0, 1, 'C', 0)
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def pdfRecebimentoAVista(self, id_recebimento):

        

        pdf = PDF()
        pdf.add_page()
        html = """<table align="center" width="50%">
                    <thead>
                        <tr>
                            <th width="10%">ID</th>
                            <th width="10%">Número</th>
                            <th width="10%">Data</th>
                            <th width="10%">Valor Final</th>
                        </tr>
                    </thead>    
                </table>"""
        pdf.write_html(html)
        

        pdf.output('recebimento.pdf', 'F')
        

    