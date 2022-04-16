

# ANAC Data Ingest
🗣📖 Este repositório contém o código fonte utilizado para desenvolver uma plataforma de dados que seja possível orquestrar a ingestão de dados (extração e carregamento) de microdados estatístico do transporte aéreo disponibilizado pela ANAC (Agência nacional de Aviação Cívil) e disponibilizar para futuro tratamento e consumo no Azure Datalake Gen2.

![Ingestão de dados sendo orquestrada pelo Apache Airflow ](https://i.imgur.com/30hqmcW.jpg)
![Arquitetura que serviu como base](https://i0.wp.com/www.theseattledataguy.com/wp-content/uploads/2022/01/https___bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com_public_images_7b1cc394-c7be-46fc-a772-b78d02299fbb_1620x620.png?resize=1024%2C392&ssl=1)


### Tecnologias utilizadas:
Para fazer com que o ambiente rodando Apache Airflow e Spark seja fácil de montar, recorremos ao Docker. As tecnologias utilizadas neste projeto foram:

- Apache Airflow 2.2.5 (Utilizando CeleryExecutor)
- Apache Spark 3.2.1 (Utilizando essa [imagem](docker.io/bitnami/spark:3.2.1))
- Azure Datalake Gen 2 (Utilizando a subscrição "Azure for Students", thanksss Mr. Gates)
- Jupyter Notebooks (Sim, já preparamos o terreno para analistas/cientistas, utilizando essa [imagem](https://hub.docker.com/r/jupyter/all-spark-notebook))


## 📖 Motivação
Atualmente, possuo um computador parrudo, mas não possuo créditos para utilizar o Apache Databricks, e para aperfeiçoar os meus estudos em Data Plataform Engineer, bem como em Data Engineering, resolvi subir um pequeno cluster (com dois nós) de Apache Spark, bem como utilizar o Airflow/Jupyter replicando uma arquitetura de plataforma de dados moderna. De brinde, resolvi aproveitar o desconto da Azure for Students.

##  🔧🔨  Ferramentas necessárias para desenvolver
- Git (Utilizado para versionamento do código)
- Docker (Para montarmos subirmos o Apache Spark, Apache Airflow e Jupyter)
- Subscrição da Azure para armazenarmos o Blob Storage.

## 🆘 Como subir o ambiente?
Para subir o ambiente de desenvolvimento é necessário ter as ferramentas instaladas, em seguida, gerar as chaves SSH para conseguir utilizar o GitHub ([veja esse tutorial](https://dev.to/dxwebster/como-conectar-ao-github-com-chaves-ssh-1i41)). Em seguida, siga os seguintes passos de execução.
#
 ### Clonar o repositório na máquina
 Execute o seguinte passo para fazer download do repositório em sua máquina.

    git clone git@github.com:FelipeGaleao/anac-data-ingest.git . 

### Subir o container com o Apache Spark e Apache Airflow.
Navegue até a pasta do Apache Spark, e execute o seguinte comando. Após concluir e subir o container, navegue até a pasta do Apache Airflow e execute novamente o comando para subir o container do Apache Airflow.

    docker-compose up -d --build 

