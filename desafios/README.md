# Evolución de técnicas en procesamiento de lenguaje natural

Este repositorio consolida una serie de prácticas progresivas en el campo del procesamiento de lenguaje natural (NLP). A través de cuatro etapas bien diferenciadas, se documenta el avance desde la manipulación básica de texto y modelos probabilísticos hasta la implementación de arquitecturas neuronales complejas para tareas de traducción automática.

## Desafío 1: vectorización y clasificación probabilística

La etapa inicial se centró en la comprensión de cómo las máquinas interpretan el texto. El objetivo principal fue: transformar datos no estructurados en representaciones numéricas.

Se utilizaron técnicas de bolsa de palabras (bag of words) y tf-idf para convertir documentos de texto en vectores dispersos. Posteriormente, se implementaron clasificadores bayesianos ingenuos (naive bayes), lo que permitió establecer una línea base de rendimiento para tareas de categorización de noticias. Esta fase asentó las bases sobre la importancia del preprocesamiento y la limpieza de datos antes de cualquier modelado.

## Desafío 2: representaciones distribuidas y embeddings

El segundo hito abordó la limitación de las representaciones dispersas, donde se pierde el contexto semántico entre palabras. El enfoque cambio hacia la creación de espacios vectoriales densos.

Utilizando un corpus técnico específico sobre telecomunicaciones, se entrenaron modelos de word2vec. Este proceso requirió un preprocesamiento más sofisticado para extraer texto limpio desde fuentes pdf. El resultado fue la capacidad de capturar relaciones semánticas y analogías entre términos técnicos, demostrando que el significado puede ser codificado mediante la co-ocurrencia de palabras en un contexto compartido.

## Desafío 3: modelos de lenguaje y redes recurrentes

En esta fase se introdujo la dimensión temporal y secuencial del lenguaje. El propósito fue predecir el siguiente caracter en una secuencia para generar texto coherente.

Se compararon tres arquitecturas de redes neuronales: rnn simple, lstm y gru. Este experimento evidenció los problemas de desvanecimiento del gradiente en redes simples y cómo las celdas con compuertas (lstm y gru) resuelven este problema al mantener memoria a largo plazo. Se implementaron generadores de datos eficientes y métricas como la perplejidad para evaluar la calidad de los textos científicos generados por el modelo.

## Desafío 4: arquitectura encoder-decoder para traducción

La etapa final representa la culminación del aprendizaje, integrando embeddings pre-entrenados y redes recurrentes en una arquitectura sequence-to-sequence (seq2seq). El desafío consistió en construir un sistema traductor de inglés a español.

Este modelo utiliza un codificador para procesar la secuencia de entrada y comprimirla en un vector de contexto, y un decodificador para generar la secuencia de salida en el idioma objetivo. Se utilizaron embeddings de glove para inicializar los pesos y mejorar la convergencia. Este proyecto demuestra la capacidad de las redes neuronales para mapear secuencias complejas de longitud variable, superando la generación simple de caracteres vista en la etapa anterior.

## Resumen de la evolución técnica

La siguiente tabla resume el incremento de complejidad y las tecnologías claves adoptadas en cada etapa:

| desafío | enfoque principal | representación de datos | arquitectura del modelo | objetivo |
| :--- | :--- | :--- | :--- | :--- |
| 1 | estadística clásica | vectores dispersos (tf-idf) | naive bayes | clasificación de texto |
| 2 | semántica distribuida | vectores densos (embeddings) | word2vec (red neuronal superficial) | similitud semántica |
| 3 | modelado secuencial | secuencias de caracteres | rnn, lstm, gru | generación de texto |
| 4 | mapeo de secuencias | secuencias de palabras + glove | encoder-decoder (seq2seq) | traducción automática |

Se observa una clara transición desde métodos que tratan las palabras como unidades independientes hacia modelos que comprenden el contexto, la secuencia y, finalmente, la relación compleja entre dos estructuras lingüísticas diferentes.