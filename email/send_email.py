import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def send_email():
    password = 'kotyisxmwyvzkjfr'
    msg = MIMEMultipart()
    msg['From'] = 'empresaramachandran@gmail.com'
    msg['To'] = 'usuarioramachandran@gmail.com'
    msg['Subject'] = 'Gráfico ramachandran'
    body = MIMEText(f'plotagem do gráfico ramachandran')
    msg.attach(body)
    with open('asd.png', 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment; filename="asd.png"')
        msg.attach(img)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('empresaramachandran@gmail.com', password)
    smtp.sendmail('empresaramachandran@gmail.com', 'usuarioramachandran@gmail.com', msg.as_string())
    smtp.quit()
    
    #with open('arquivo.txt', 'r') as f:
        #text_content = f.read()
    # Cria um objeto MIMEText para representar o arquivo de texto como anexo
    #attachment = MIMEText(text_content)
    #attachment.add_header('Content-Disposition', 'attachment; filename="arquivo.txt"')
    # Anexa o objeto MIMEText à mensagem de email
    #msg.attach(attachment)