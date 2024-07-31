# <h1 align= 'center'>Análisis de Riesgo Crediticio</h1>
<p align = center>
  <img src= 'assets/banner_inicio.png' width= 100% >
</p>

![Markdown](https://img.shields.io/badge/-Markdown-black?style=flat-square&logo=markdown)
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)
![Numpy](https://img.shields.io/badge/-Numpy-black?style=flat-square&logo=numpy)
![Pandas](https://img.shields.io/badge/-Pandas-black?style=flat-square&logo=pandas)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-black?style=flat-square&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-black?style=flat-square&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-black?style=flat&logo=scikitlearn)
![Power BI](https://img.shields.io/badge/-Power%20BI-black?style=flat-square&logo=powerbi)
![Power Query](https://img.shields.io/badge/-Power%20Query-black?style=flat-square&logo=powerquery)
![Tableu](https://img.shields.io/badge/-Tableu-black?style=flat-square&logo=tableu)
![Microsoft Excel](https://img.shields.io/badge/-Microsoft%20Excel-black?style=flat-square&logo=excel)
![Git](https://img.shields.io/badge/-Git-black?style=flat-square&logo=git)
![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)
![Google Drive](https://img.shields.io/badge/-Google%20Drive-black?style=flat-square&logo=googledrive)
![Google Colaboratory](https://img.shields.io/badge/-Google%20Colaboratory-black?style=flat-square&logo=googlecolaboratory)
![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-black?style=flat&logo=visual-studio-code&logoColor=007ACC)

# Índice

- [Introducción](#Introducción)
- [Objetivos](#Objetivos)
- [Datos](#Datos)
- [Desarrollo](#Desarrollo)
  - [ETL](#ETL)
  - [EDA](#EDA)
  - [Dashboard](#Dashboard)
  - [Modelo](#Modelo)
  - [Deploy](#Deploy)
- [Tecnologías](#Tecnologías)
- [Conclusiones](#Conclusiones)
- [Equipo](#Equipo)

# Introducción

El Banco IPB es una entidad financiera que está ofreciendo creditos para empresas a una tasa de interes muy atractiva como parte de su politica financiera y el contexto economico que se esta dando en Argentina.
En un principio, centra su oferta de credito en los sectores que potencialmente tienen el mayor salto en el desarrollo y expansión actualmente, como son el sector hidrocarburífero, agricola, minero, de ciencias del conocimiento, etc.

Para ello, necesita un marco de análisis en conjunto con las herramientas necesarias para estimar el riesgo crediticio que conllevaria autorizar un prestamo a una empresa, lo que brindaria seguridad y garantia de pago al momento de otorgarlo.

Por este motivo, nos contrata a nosotros, la consultora AyC para que le brindemos el soporte para esta toma de decisiones.

# Objetivos

<p align = center>
  <img src= 'assets/banner_consultora_ayc.png' width= 100% >
</p>

Los principales objetivos y condiciones en este sentido son:

* La construccion de un marco analitico donde se puedan realizar la toma de decision principal (el otorgamiento y autorizacion del credito) tomando en cuenta riesgo y garantia.
* El estudio exhaustivo de la situacion general y potencial de la empresa en cuestion, que abarque aspectos de capital, financieros, contables, de sector, de produccion, etc
* La construccion de un modelo o sistema que permita una mirada concisa, precisa y predictiva del comportamiento de la empresa para/con el cumplimiento de pago del prestamo.
* El asesoramiento de ideas y conclusiones que complementen el marco analitico con informacion util y argumentos concretos para la toma de decisiones.

# Datos

En Principio, los datos con los que contamos y vamos a trabajar referidos a la tematica de proyecto, son de diferentes origenes, aunque principalmente se obtienen de la plataforma web de datos publicos de la nacion (tanto en Datos Argentina como en los diferenetes ministerios o la plataforma de la nación).

Detallamos los origenes principales:
* https://kaggle.com/
* https://datos.gob.ar/
* https://www.argentina.gob.ar/
* https://nasdaq.com
* https://inversores.ypf.com/informacion-financiera.html
* https://datos.enerdata.net/productos-petroliferos/estadisticas-consumo-mundial-petroleo-consumo-domestico.html
* https://datos.enerdata.net/petroleo-crudo/datos-produccion-energia-mundial.html

Como se hace notar, nos centramos en la data de empresas petroleras en un contexto general medio apuntamos a el ambito dentro de argentina (el objeto de estudio se centra principalmente en la empresa YPF), aunque complementamos la misma con algunos datos referentes al área (de hidrocarburos) de otras empresas no radicadas en Argentina, y en el contexto global apuntamos a informacion general del sector de hidrocarburos en un contexto amplio para tomar como punto de referencia en diversos analisis.

La data apunta a el estado general de actividad productiva, el estado financiero y/o contable de la empresa y su capital-infraestructura, la proyeccion de produccion y crecimiento, las inversiones que realiza, la cotizacion en bolsa, etc... todo esto, pertinente para tener un panorama claro del estado general de la empresa a evaluar.

Los datos con los que se trabaja son:

* Inversiones de empresas petroleras en Argentina (desde el año 2020 hasta el año 2024)
* Informacion contable sobre YPF
* Cotizaciones de diversas empresas petroleras/ de hidrocarburos en bolsas de EEUU
* Produccion de gas y petroleo en Argentina (desde 2020 hasta 2024)
* Precio internacional del barril de crudo (desde el año 1970)
* Consumo internacional de hidrocarburos por pais
* Reservas de hidrocarburos en Argentina
* Pozos registrados en el pais
* Rentas del petroleo en Argentina (en % de PBI)
* Informacion contable y financiera de diversas empresas de hidrocarburos

Mención aparte a los informes o analisis y benchmark de la temática que utilizamos y que no se registran como datos, ya que nos sirven para tener conocimiento y guia del tema en analisis
y poner en contexto y terminologia, asi como mecanismos y utilizacion de herramientas y logica al material de datos con el que contamos.


# Desarrollo
## ETL

En la fase de Transformación de Datos (ETL), se llevaron a cabo una serie de procedimientos para garantizar la preparación adecuada y la limpieza exhaustiva de los datos antes de su carga en el almacén de datos. Estas acciones incluyeron:

- Verificación del tipo de datos de cada columna: Se examinó minuciosamente el tipo de datos de cada columna para garantizar su coherencia y precisión en el análisis posterior. 
- Análisis de la dimensionalidad de los datos: Se exploró la estructura del conjunto de datos para comprender su tamaño y complejidad, lo que permitió una mejor comprensión de la cantidad de registros y variables presentes.
- Manejo de valores nulos: Se identificaron y abordaron los valores nulos en el conjunto de datos mediante técnicas como la imputación de datos o la eliminación de registros incompletos, con el fin de evitar sesgos o distorsiones en el análisis posterior.
- Verificación visual de valores atípicos: Se realizó una exploración gráfica de los datos para detectar posibles valores atípicos o anomalías que podrían afectar la integridad y la precisión de los resultados.
- Indagación de consistencia de los datos: Se llevaron a cabo investigaciones exhaustivas sobre la consistencia de los datos, incluyendo la identificación de máximos, mínimos y rangos de valores para cada variable, lo que ayudó a garantizar la fiabilidad de los datos utilizados en el análisis.

Como paso previo, en algunos casos los ficheros presentaban un formato no adecuado para su transformacion y manipulacion directa por lo que se debia realizar una instancia previa, la extraccion de los datos en formato de tabla, para su posterior manipulación y conversión. Esto se puede ver plasmado en este [notebook](notebooks/tratamiento_ficheros_tabdinamicas.ipynb)

Todas estas acciones en conjunto permitieron la normalizacion, formateo y estructuracion de los datos que obtuvimos en referencia a la tematica. Esta serie de acciones se pueden ver en el notebook [ETL_ipynb](notebooks/ETL.ipynb) donde tambien estan comentados los cambios realizados a cada archivo y su fundamentación.

|                       |                       |
|-----------------------|-----------------------|
| ![Imagen 1](assets/grafico_nulos_1.png) | ![Imagen 2](assets/grafico_nulos_2.png) |
| Distribucion de los valores nulos| Correlación entre valores nulos |

Para completar el camino realizado en la Extracción, Transformacion y Carga/disponibilización de los datos ponemos a disposicion dos informes concernientes a informar y detallar el estado de los datos en instancias anteriores a su proceso de ETL y posteriores al mismo:

-El [Informe ETL_preliminar](notebooks/Informe_ETL_Preliminar.ipynb) proporciona un análisis detallado de la calidad y las características de los datos originales, y ofrece funciones específicas para examinar y explorar los datos en profundidad. Estas funciones incluyen la visualización de valores nulos, análisis de frecuencia de palabras, boxplots numéricos y más, lo que facilita la identificación de patrones, tendencias y relaciones significativas en los datos.

|                       |
|-----------------------|
| ![Imagen 3](assets/tabla_datos.png) |
| Parte del analisis realizado en el momento del proceso de ETL a los datos, vemos uno de los campos con datos anidados |


-El [Informe EDA_preliminar](notebooks/EDA_preliminar.ipynb) hace incapie en una instancia intermedia entre la carga y disponibilizacion de los datos y su uso puntual en un informe EDA. En el utilizamos funciones que permiten ver graficamente la distribucion de valores de cada campo en cada fichero y su proporcion en el conjunto total, complementando los mismos con estadísticas básicas de los mismos los que nos permiten tener un panorama general al momento de realizar un análisis mas exhaustivo y complejo, es decir, nos permite aproximarnos a los datos de una manera general en un sentido mucho mas estadistico/analítico previo a su estudio.

|                       |
|-----------------------|
| ![Imagen 4 ](assets/distribucion_densidad.png) |
| Distribucion de frecuencias en un campo con valores proporcionales. Podemos ver en los gráficos la distribucion y densidad de valores en conjunto con la presencia de outliers y asimetria en la distribución |

<details>
  <summary>Otra información: Modelo ER</summary>

  El modelo ER (Entidad-Relación) se construyó con la finalidad de proporcionar un marco estructurado a las relaciones entre las tablas provenientes de las diferentes fuentes de datos.

  Estas relaciones en parte estaban intrínsecamente dadas para la mayor parte de los ficheros de un origen común, y en otros casos se tuvo que realizar una ingenieria en los datos, donde se construyeron campos que actuaran como PK y FK (Primary Key y Foreing Key respectivamente) para su adecuado manejo y almacenamiento o se normalizaron y/o formatearon campos para que actuaran como tales.

  En principio, esto nos brindo además una adecuada relacion entre las diversas tablas para su visualizacion e interactividad, segmentación, filtrado y ploteo en el dashboard.

|                       |
|-----------------------|
| ![modelo](assets/modelo_ER.png) |
| Modelo Entidad-Relación |

</details>

## EDA
## Dashboard

Se tomó en un principio un enfoque general del contexto para luego plantear el enfoque en el análisis más específico concerniente a YPF.

|                       |                       |
|-----------------------|-----------------------|
| ![dash 1](assets/dash_1.png) | ![dash 2](assets/dash_2.png) |
| Análisis de producción en Argentina de petróleo y gas| Inversión en el país y cotizacion de acciones y movimiento en el mercado bursatil de la empresa YPF |


|                       |
|-----------------------|
| ![Dash 3](assets/dash_3.png) |
| Ratios de la empresa YPF del año 2024 contrastados con el año 2023 (este último representado por la linea negra en cada barra) |

Disponibilizamos el dashboard para su descarga [aquí](dashboard/Estudio_Analisis_Riesgo_Crediticio.pbix).

## Modelo
## Deploy
# Tecnologías
# Conclusiones
# Equipo

<div align="center">

<!-- Primera fila -->
<table>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/106486985?s=400&u=f2b5a4953b674b71e5df9e4c71c89ee2ae75fa65&v=4" width="200" height="200"><br><strong>Marco</strong><br>
      <a href="https://www.linkedin.com/in/marco-antonio-caro-22459711b"><img src="assets/linkedin.png" style="width:20px;"></a>
      <a href="https://github.com/marco11235813"><img src="assets/github.png" style="width:20px;"></a>
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/157044866?v=4" width="200" height="200"><br><strong>Ángel</strong><br>
      <a href="LINK-LINKEDIN"><img src="assets/linkedin.png" style="width:20px;"></a>
      <a href="https://github.com/AngelTroncoso"><img src="assets/github.png" style="width:20px;"></a>
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/131561932?v=4" width="200" height="200"><br><strong>Malena</strong><br>
      <a href="https://www.linkedin.com/in/malena-jara"><img src="assets/linkedin.png" style="width:20px;"></a>
      <a href="https://github.com/Malena646"><img src="assets/github.png" style="width:20px;"></a>
    </td>
  </tr>
</table>

<!-- Segunda fila -->
<table>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/109807315?v=4" width="200" height="200"><br><strong>Ana</strong><br>
      <a href="http://www.linkedin.com/anaherrerachuica"><img src="assets/linkedin.png" style="width:20px;"></a>
      <a href="https://github.com/AnaHerreraC"><img src="assets/github.png" style="width:20px;"></a>
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/158371081?v=4" width="200" height="200"><br><strong>Jitzua</strong><br>
      <a href="LINK-LINKEDIN"><img src="assets/linkedin.png" style="width:20px;"></a>
      <a href="https://github.com/JJCHRICO"><img src="assets/github.png" style="width:20px;"></a>
    </td>
  </tr>
</table>

</div>
