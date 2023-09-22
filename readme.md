## Introdução Vinheria 
O case nos apresenta a Vinheria Agnello, uma vinheria tradicional que atua há mais de 15 anos em São Paulo em uma única loja física. Durante a pandemia , constatou-se a necessidade da adesão dos serviços online para garantir um bom atendimento aos clientes. Assim, a plataforma de econmerce precisava ser desenvolvida a partir de uma condição estipulada pelo dono: a loja virtual precisava ser diferente, inovadora ao promover um atendimento totalmente personalizado aos compradores, uma experiência semelhante a oferecida fisicamente.

## Sensor de luz, temperatura e umidade.
Nota-se que neste case da Vinheria Agnello, a qualidade e excelente condição dos vinhos oferecidos é essencial.
Para garantir a qualidade dos produtos, está sendo desenvolvido um sensor capaz de captar dados referentes a luminosidade, temperatura e umidade do ambiente em que os vinhos seriam armazenados. O intuito deste, é monitorar a área e captar as informações, através de IOT, para garantir que as condições de armazenamento estejam adequadas para manter o vinho com suas propriedades apropriadas. Dessa maneira através do uso de Internet das coisas e Fiware, seria possível receber os dados, informações relevantes recebidas pelo dispositivo.Atualmente, estamos utilizando de uma placa ESP 32, sensor fotorresistor LDR e um Led vermelho. Nesta etapa, a ESP 32 é necessária para permitir a conexão ao WIFi para comunicação entre o dispositivo físico e o Fiware.

## Gráficos de leitura de luminosidade
Os gráficos abaixo foram montados a partir dos dados coletados em um intervalo de 15 minutos.
![Untitled (1)](https://github.com/fernandakaory/cp5-edge/assets/126582859/d7a043ad-0085-4fec-aeb8-a93f3da52889)
Este primeiro gráfico foi montado para mostrar as leituras de luminosidade por minuto em um determinado intervalo de tempo. Clique <a href="https://github.com/fernandakaory/cp5-edge/blob/main/grafico1.py">aqui</a> para visualizar o código utilizado.
![Untitled (2)](https://github.com/fernandakaory/cp5-edge/assets/126582859/48b73f69-59a5-46c5-8c1d-aa1ed0bb00ed)
Este segundo gráfico foi montado para exibir mais leituras de luminosidades captadas em um intervalo de tempo. Clique <a href="https://github.com/fernandakaory/cp5-edge/blob/main/grafico2.py">aqui</a> para visualizar o código utilizado.

## Arquitetura IoT
<div align="center">
  <img src="https://github.com/fernandakaory/cp5-edge/assets/126582859/14d7e32c-9c77-4bf5-b993-9316b761b6ad" >
</div>


## Recursos necessários para implementação da solução
<h3>O Hardware deste projeto, é composto essencialmente por: </h3>
Uma placa ESP 32, que conta com dois núcleos de 32 bits, responsável por permitir a conexão ao wifi ou blutooth, garantindo, assim, a comunuicação e transporte de dados entre ela e o Fiware.

<div align="center">
  <img src="https://github.com/fernandakaory/sprint3-edge/assets/126582859/2530d075-fcab-4b35-ad58-5eed09751ef7" >
</div>

E um sensor fotorresistor LDR para captar os dados de luminosidade que serão enviados para a camada Back-end.
<div align="center">
  <img src="https://github.com/fernandakaory/cp5-edge/assets/126582859/e915c367-c692-450a-985c-a55a7eae9e41" >
</div>
<h3>Back-end</h3>
Para o Back-end do projeto será utilizado o Fiware. Esta, é uma plataforma de código aberto que fornece uma infraestrutura padrão e aberta para o desenvolvimento de aplicações e serviços inteligentes baseados em IoT. Desta maneira, esta ferramenta será utilizada para que os dados coletado a partir do sensor LDR, sejam transportados e processados até um dashboard (camada Front-end), para que essas informações sejam analisadas e contraladas, com o objetivo de garantir a qualidade dos vinhos e condições adequadas do ambiente de armazenamento.
<div align="center">
  <img src="https://github.com/fernandakaory/sprint3-edge/assets/126582859/dcd4980b-f53f-444d-99d6-4925a6668d87" >
</div>
<h3>Front-end</h3>
A base front-end deste projeto, atualmente, será uma plataforma de dashboard gratuito, o <a href=https://freeboard.io/> freeboard </a>. Os dados captados pelos sensores, como a luminosidade, serão exibidos a partir de widgets e gráficos, para que as informações estejam disponíveis e vísiveis de uma maneira simples e intuitiva.

![Captura de tela 2023-09-21 211216](https://github.com/fernandakaory/cp5-edge/assets/126582859/58b6d4c4-50bc-40ce-ae28-d5bc36d917e1)


## Requisitos do projeto
- Docker e docker compose
- Fiware
- Postman
- ESP 32 e sensor fotorresistor LDR
- Conectividade Wifi
- Ambiente front-end, como o <a href=https://freeboard.io/> freeboard </a>.
  
## Configuração e reprodução
1. Instalação de uma máquina virtual Linux
2. Instalação do docker e do docker compose como especificado <a href="https://docs.docker.com/engine/install/ubuntu/"> aqui </a>.
3. Instalação do <a href=https://github.com/fabiocabrini/fiware> Fiware</a>.
4. Instalação do Postman
5. Importar as collection para o Fiware e executar os métodos HTTP de Health Check
6. Provisionar os sensores como dispositivos virtuais (como no arquivo json acima), definindo id, protocolo de comunicação, comandos e atributos.
7. Registrar esses dispositivos  (como no arquivo json acima).
8. Montar os sensores físicos na ESP 32.
9. Montar o código desses sensores para enviar por MQTT os dados.
10. Realizar a subscrição e métodos GET para receber os dados desejados.
11. Enviar e exibir as informações no front-end,
