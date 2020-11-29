from fpdf import FPDF, HTMLMixin
from datetime import datetime

from mod_comanda.comandaBD import Comanda



class PDF(FPDF, HTMLMixin):
    
    def header(self):
        self.image("static/imgs/pastelaria-logo-2.png", 10, 8, 35)
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
        pdf = PDF('L', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Pastelaria do Zé")
        pdf.set_title('Recebimento a Vista')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(280, 5, 'Recebimento', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(280, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 10)
        comanda = Comanda()
        recebimento = comanda.buscaRecebimentoPorId(id_recebimento)

        
        if recebimento:
            for dado in recebimento:            
                pdf.cell(10, 5, 'ID Recebimento: ' + str(id_recebimento), 0, 1, 'L')
                pdf.ln(2)
                pdf.cell(55, 5, 'Número Comanda: ' + str(dado['comanda']), 0, 1, 'L')
                pdf.ln(2)
                pdf.cell(30, 5, 'Data: ' + str(dado['data_hora']), 0, 1, 'L')
                pdf.ln(2)
                pdf.cell(10, 5, 'Produtos: ', 0, 1,'L')
                pdf.ln(2)
                pdf.cell(40, 5, 'Nome', 0, 0, 'L')
                pdf.cell(25, 5, 'Quantidade', 0, 0, 'L')
                pdf.cell(30, 5, 'Valor Unitário', 0, 1, 'L')
                comanda.id_comanda = dado['id_comanda']
                produtos = comanda.selectProdutosPorIdComanda()
                for produto in produtos:
                    pdf.cell(50,5, str(produto[0]), 0, 0, 'L')
                    pdf.cell(20, 5, str(produto[1]), 0, 0)
                    pdf.cell(30, 5,'R$ ' + str(produto[2]), 0, 1)
                pdf.ln(2)
                pdf.cell(30, 5, 'Valor Total R$ ' + str(dado['valor_total']), 0, 1, 'L')
                pdf.ln(2)
                pdf.cell(30, 5, 'Desconto: R$ ' + str(dado['desconto']), 0, 1, 'L')
                pdf.ln(2)                
                pdf.cell(30, 5, 'Valor: R$ ' + str(dado['valor_final']), 0, 1, 'L')
                    
        
        

        pdf.output('recebimento.pdf', 'F')
        

    