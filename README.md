# scripts-sms
<h3><center> Scripts de linha de comando em Python para envio de múltiplos SMS's pelo Twilio ou pela AWS SNS </center></h3>
<p> Scripts para enviar mensagem de texto através da linha de comando para um ou mais telefones, através do Twilio ou do 
Simple Notification Service - SNS - da Amazon Seb Services - AWS. </p>

<h4> Instalando as dependências </h4>
<p> Instale as bibliotecas do AWS e Twilio <blockquote> pip install -r requirements.txt </blockquote> </p>

<h4> Configure suas Credenciais do SNS AWS, do Twilio, ou ambas </h4>
<h5> SNS AWS </h5>
<p> substitua as credencias do arquivo /credenciais/aws_credentials.py pelas suas credenciais em
https://console.aws.amazon.com/iam/home -> Usuários -> Security Credentials ->
Sign-in credentials -> Access Key </p> 
<h5> TWILIO</h5>
<p> substitua as credencias do arquivo /credenciais/twilio_credentials.py pelas suas credenciais em
https://www.twilio.com/console/project/settings </p>
<H4> COMO USAR </H4>
<p> Os números de telefone para envio devem usar o formato internacional, com o '+' na frente. Por exemplo, o telefone (11)9999-8877 
ficará sendo +551199998877 (sem espaços, traços e com o código do Brasil (55) depois do + )</p>
<h5> Para enviar pelo Twilio </h5>
<blockquote> python smstwilio.py +551199998877 "mensagem entre aspas" </blockquote>
Para anviar para vários telefones ao mesmo tempo, basta adicionar outros números antes da mensagem. Ex:
<blockquote> python smstwilio.py +551199998877 +551199998876 +551199998875 +551199998874 "mensagem entre aspas" </blockquote>
<h5> Para enviar pela AWS - SNS </h5>
Basta substituir o nome do script. Ex.:
<blockquote> python smsaws.py +551199998877 +551199998876 +551199998875 +551199998874 "mensagem entre aspas" </blockquote>

