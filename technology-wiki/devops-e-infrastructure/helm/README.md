# Helm

* Comumente usado para empacotamento de aplicações kubernetes
* Surgiu em 2015, empresa criadora foi adquirida pela Microsoft
* Projeto graduado na CNCF
* É um gerenciador de pacotes, semelhante ao APT e YUM

* Chart é o pacote do helm que possui vários arquivos, entre eles:
  * Chart: que é a versão e metadados do chart, carrega as próprias informações
  * Values: valores para otimizar e personalizar as entregas
  * Templates: arquivos que vão receber os valus e combinados vão gerar os arquivos(yaml) kubernetes
  * Repositório: onde sobe e também consome charts (hub.helm)
  * Release: instância de um chart, quando faz a instalação de um microserviço(helm install cria um release)