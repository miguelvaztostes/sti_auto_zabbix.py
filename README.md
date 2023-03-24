# Automatizando adição de hosts no Zabbix

---
Este script Python automatiza a adição de hosts no Zabbix, lendo informações de um arquivo XLSX (no exemplo fornecido, 'cameras_fmrp.xlsx') e adicionando os hosts com nome, IP, grupo de host e template.
---
Para usar o script, é necessário preencher as informações do seu ambiente Zabbix na seção de configuração.


Em seguida, basta executar o script Python e aguardar até que todos os hosts sejam adicionados com sucesso.

O script usa as seguintes bibliotecas Python:

---
os
---

---
pandas
---

---
pyzabbix
---

Certifique-se de instalá-las antes de executar o script. Além disso, é necessário ter o arquivo 'cameras_fmrp.xlsx' no diretório atual ou especificar o caminho completo para o arquivo na variável 'file_path'.

No exemplo fornecido, o script adiciona mais de 100 câmeras da Hikvision para monitoramento no Zabbix.
