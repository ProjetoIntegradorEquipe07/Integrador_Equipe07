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
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Pastelaria do Zé")
        pdf.set_title('Recebimento a Vista')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(190, 5, 'Recebimento a Vista', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(200, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 10)
        comanda = Comanda()
        recebimento = comanda.buscaRecebimentoPorId(id_recebimento)

        
        if recebimento:
            pdf.set_x(100)
            for dado in recebimento:            
                pdf.cell(10, 5, 'ID Recebimento: ' + str(id_recebimento), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(79)
                pdf.cell(55, 5, 'Número Comanda: ' + str(dado['comanda']), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(87)
                pdf.cell(30, 5, 'Data: ' + str(dado['data_hora']), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(92)
                pdf.cell(10, 5, 'Produtos: ', 0, 1,'C')
                pdf.ln(2)
                pdf.set_x(45)
                pdf.cell(50, 5, 'Nome', 0, 0, 'C')
                pdf.cell(25, 5, 'Quantidade', 0, 0, 'C')
                pdf.cell(30, 5, 'Valor Unitário', 0, 1, 'C')
                comanda.id_comanda = dado['id_comanda']
                produtos = comanda.selectProdutosPorIdComanda()
                for produto in produtos:
                    pdf.set_x(55)
                    pdf.cell(50,5, str(produto[0]), 'B T', 0)
                    pdf.cell(20, 5, str(produto[1]), 'B T', 0)
                    pdf.cell(30, 5,'R$ ' + str(produto[2]), 'B T', 1)
                pdf.ln(2)
                pdf.set_x(90)
                pdf.cell(30, 5, 'Valor Total R$ ' + str(dado['valor_total']), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(88.7)
                pdf.cell(30, 5, 'Desconto: R$ ' + str(dado['desconto']), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(86)                
                pdf.cell(30, 5, 'Valor: R$ ' + str(dado['valor_final']), 0, 1, 'C')
                    
        
        
        
        pdf.output("recebimento.pdf")

    def pdfRecebimentoFiado(self, id_recebimento):

        pdf = PDF()
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Pastelaria do Zé")
        pdf.set_title('Recebimento a Vista')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(190, 5, 'Recebimento Fiado', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(200, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 10)
        comanda = Comanda()
        recebimento = comanda.buscaRecebimentoPorId(id_recebimento)

        
        if recebimento:
            pdf.set_x(100)
            pdf.cell(10, 5, 'ID Recebimento: ' + str(id_recebimento), 0, 1, 'C')
            pdf.ln(2)
            pdf.set_x(83)
            pdf.cell(50, 5, 'Nome Cliente: ' + str(recebimento[0]['nome']), 0 ,1, 'C')
            pdf.ln(5)
            for dado in recebimento:           
                pdf.set_x(79)
                pdf.cell(55, 5, 'Número Comanda: ' + str(dado['comanda']), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(87)
                pdf.cell(30, 5, 'Data: ' + str(dado['data_hora']), 0, 1, 'C')
                pdf.ln(2)
                pdf.set_x(92)
                pdf.cell(10, 5, 'Produtos: ', 0, 1,'C')
                pdf.ln(2)
                pdf.set_x(45)
                pdf.cell(50, 5, 'Nome', 0, 0, 'C')
                pdf.cell(25, 5, 'Quantidade', 0, 0, 'C')
                pdf.cell(30, 5, 'Valor Unitário', 0, 1, 'C')
                comanda.id_comanda = dado['id_comanda']
                produtos = comanda.selectProdutosPorIdComanda()
                valor_comanda = 0.0
                
                for produto in produtos:
                    pdf.set_x(55)
                    pdf.cell(50,5, str(produto[0]), 'B T', 0)
                    pdf.cell(20, 5, str(produto[1]), 'B T', 0)
                    pdf.cell(30, 5,'R$ ' + str(produto[2]), 'B T', 1)
                    valor_comanda += (float(produto[1]) * float(produto[2]))
                    
                pdf.ln(2)
                pdf.set_x(90)
                pdf.cell(30, 5, 'Valor Comanda R$ ' + str(valor_comanda), 0, 1, 'C')
                pdf.ln(10)
            pdf.set_x(90)
            pdf.cell(30, 5, 'Valor Total: R$ ' + str(recebimento[0]['valor_total']), 0, 1, 'C')
            pdf.ln(2)
            pdf.set_x(88)
            pdf.cell(30, 5, 'Desconto: R$ ' + str(recebimento[0]['desconto']), 0, 1, 'C')
            pdf.ln(2)
            pdf.set_x(89.9)                
            pdf.cell(30, 5, 'Valor Final: R$ ' + str(recebimento[0]['valor_final']), 0, 1, 'C')
        
        pdf.output("recebimento.pdf")
    