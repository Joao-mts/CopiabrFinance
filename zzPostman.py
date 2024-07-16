import requests

def download_pdf(num_sequencia, num_protocolo, desc_tipo):
    url = (
        "https://www.rad.cvm.gov.br/ENET/frmDownloadDocumento.aspx?"
        f"Tela=ext&numSequencia={num_sequencia}&"
        f"numProtocolo={num_protocolo}&descTipo={desc_tipo}&CodigoInstituicao=1"
    )

    response = requests.get(url)
    if response.status_code == 200:
        pdf_filename = f"document_{num_sequencia}.pdf"
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF baixado e salvo como {pdf_filename}")
    else:
        print(f"Falha no download do PDF. Status code: {response.status_code}")

# Parâmetros do request
num_sequencia = 784724
num_protocolo = 1259998
desc_tipo = "IPE"

# num_sequencia = 137205
# num_protocolo = '009512'
# desc_tipo = "ITR"

# Chamar a função para baixar o PDF
download_pdf(num_sequencia, num_protocolo, desc_tipo)
