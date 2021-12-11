# Kaggle APC UAB 2021-22

### Nom: Víctor Bosch Pueyo
### DATASET: Music Genre Classification
### URL: https://www.kaggle.com/purumalgi/music-genre-classification

## Resum
La base de dades treballa amb dades obtingudes de cançons populars.
Tenim 17,996 dades amb 17 atributs. Tots, menys el nom de l'artista i el nom de la cançó són atributs numèrics.
El 50% d'aquests atributs estàn normalitzats, 18% segueixen la mètrica pròpia de l'atribut (ex. la duració s'expressa en min/ms) i la resta són categòrics.
Mirem la distribució de les nostres classes i veiem que estàn molt desbalancejades (la classe minoritària té 148 dades i la majoritària més de 3300), la qual cosa farà que obtinguem molt bons resultats d'unes classes i molt pobres d'altres.

### Objectius del dataset
Amb aquest dataset voldrem acabar predint a quin gènere musical (dels 11 que hi ha a la base de dades) pertany una cançó segons aquests atributs.

## Experiments
Per tal d'acomplir aquest objectiu aplicarem els coneixements obtinguts a Aprenentatge Computacional i utilitzarem alguns dels classificadors que coneixem per a fer-ne la predicció i extreure'n conclusions.

### Preprocessat
Dels 17 atributs que hi ha, suposarem que el nom de l'artista i el nom de la cançó no ens aportaràn informació a l'hora de predir el gènere musical ja que, un artista pot fer música de diferents estils i el nom de la cançó no ens és de cap ajuda en el nostre cas.
Dels atributs numèrics, hem normalitzat els que seguien una mètrica pròpia per a tenir tots els valors entre 0 i 1 (menys l'atribut a predir que, com no hem d'operar amb ell, ja ens va bé que vagi de 1 a 11).
Finalment, hem eliminat totes les dades duplicades o que tinguessin un atribut NaN.

Un cop "netejada" la base de dades, aplicarem els diferents models per a fer la classificació.

### Model
Hem provat amb l'execució de 4 classificadors: Regressió Logística, K-Nearest Neighborgs, Arbres de decisió i Màquines de Vectors de Suport.
Primer hem comprovat el seu rendiment amb els paràmetres base i després hem buscat els millors hiperparàmetres per a cadascún.

| Model | Mètrica (sense hiperparàmetres) | Mètrica (amb hiperparàmetres) |
| -- | -- | -- |
| Regressió Logística | 0.4739737621667372 | 0.4754497354497354 |
| KNN | 0.3643673296656792 | 0.422010582010582 |
| Arbres de desició | 0.33601354210749046 | 0.3928042328042328 |
| SVM | 0.4879390605162928 | 0.4908994708994709 |
| [Regressió Logística (1vs1)](https://www.kaggle.com/sveneschlbeck/music-genre-prediction-using-logistic-regression) | 0.51194444444 | -- |

## Conclusions
El millor resultat ha estat la màquina de vectors de suport amb un rendiment de 49.926%.

Després d'analitzar la base de dades, entrenar els classificadors per a la predicció i fer l'analisi mètric dels diferents models executats podem extreure les següents conclusions:
- Obtenim uns resultats pobres en tots els diferents models ja que la nostra base de dades està molt desbalancejada. Això fa que la classe majoritària obtingui resultats més bons que les altres.
- A l'analitzar gèneres musicals només amb dades numèriques, no tenim en compte molts altres aspectes de la música que poden arribar a ser decisius. Dues cançons poden arribar a tenir resultats numèrics molt semblants pero pertanyer a gèneres totalment diferents.
- Tot hi tenir una correlació molt baixa, els classificadors han pogut obtenir uns resultats prou optimistes (tenint en compte que existeixen 11 classes diferents).
- És important la búsqueda dels millors hiperparàmetres ja que ens permet obtenir un rendiment més elevat que la configuració estàndard.
- La màquina de vectors de suports és el millor model a l'hora de classificar aquesta base de dades. S'ha de tenir en compte que, al tenir 11 classes, un rendiment del 50% és acceptable. En un classificador binari seria molt dolent ja que significaria una predicció completament aleatòria però, en el nostre cas (com podem observar en les corves ROC) obtenim uns resultats bons per a cada classe.

## Idees per treballar en un futur
Seria interessant en un futur poder aplicar altres classificadors i veure el seu rendiment. 
També podriem aplicar tècniques més avançades per al tractament de nulls que no siguin només eliminar la fila sencera, tot hi comportaria un cost de càlcul més elevat.
Per últim, a l'hora de buscar els millors hiperparàmetres podriem buscar el millor valor per a cada hiperparàmetre ja que, al ser una búsqueda tant costosa, hem reduit temps només buscant els millors valors per alguns paràmetres.


