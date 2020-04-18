<h1 align="center">
  <br>
  <a href="www.xrths.fr"><img src="https://i.ibb.co/QPLPSNn/t-l-chargement-2.png)" alt="COVID-19 FRANCE" width="275"></a>
  <br>
  COVID-19 FRANCE TWITTER
  <br>
</h1>
  
<h4 align="center">Bot Twitter qui fournit les chiffres du COVID-19 pour la France. 
<br>
<a href="https://twitter.com/CovidFrance" target="_blank">@CovidFrance (+20K)</a></h4>

<p align="center">
  <a href="https://www.python.org/">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="tweepy">
  </a>
</p>

<div align="center">

  [![Tweepy](https://img.shields.io/badge/tweepy-3.8.0-blue.svg)](https://pypi.org/project/tweepy/)
  [![Requests](https://img.shields.io/badge/requests-2.23.0-blue.svg)](https://pypi.org/project/requests/)
  [![Matplotlib](https://img.shields.io/badge/matplotlib-2.2.5-blue.svg)](https://pypi.org/project/matplotlib/)
  [![Numpy](https://img.shields.io/badge/numpy-1.16.6-blue.svg)](https://pypi.org/project/numpy/)

</div>
    
<p align="center">
  <a href="#données">Données</a> |
  <a href="#mise-en-service">Mise en service</a> |
  <a href="#graphique-généré-automatiquement">Graphique</a> |
  <a href="#remerciements">Remerciements</a> |
  <a href="#licence">Licence</a> 
  <br>
  <a href="https://www.xrths.fr">Consultez mon portofolio !</a> 
</p>

<p align="center">
  <img src="https://i.ibb.co/M58RZFz/screely-1586216563483.png">
</p>

## Données
Les données sont lues sur le GitHub de [opencovid19-fr](https://github.com/opencovid19-fr/data/blob/master/dist/chiffres-cles.json).

**Exemple (15/04/2020)**

    {'decesEhpad': 5600, 'casEhpad': 39730, 'totalDeces': 15729, 'decesHopital': 10129, 'casGueris': 28805, 'casReanimation': 6730, 'casMalades': 59039, 'casConfirmes': 103573, 'casHopital': 32292}

* **Cas totaux confirmés:** 'casConfirmes'
* **Cas décédés en hopîtaux:** 'decesHopital'
* **Cas décédés en EPHAD ou EMS:** 'decesEhpad'
* **Cas totaux décédés:** 'totalDeces'
* **Cas en réanimations:** 'casReanimation'
* **Cas hospitalisés:** 'casHopital'
* **Cas guéris:** 'casGueris'
* **Cas toujours malades:** 'casMalades'
* **Cas  confirmés en EHPAD:** 'casEhpad'
---

Les données PEUVENT aussi êtres tirées de de Worldometers, l'API utilisée est [celle ci](https://coronavirus-19-api.herokuapp.com/countries/france).


*CEPENDANT, je déconseille fortement l'utilisation de leurs données car elles sont fausses, ils interprètent mal les chiffres.*


**Exemple (08/04/2020)**

    {'country': 'France', 'cases': 112950, 'todayCases': 3881, 'deaths': 10869, 'todayDeaths': 541, 'recovered': 21254, 'active': 80827, 'critical': 7148, 'casesPerOneMillion': 1730, 'deathsPerOneMillion': 167, 'totalTests': 224254, 'testsPerOneMillion': 3436}

## Mise en service

**C'est assez simple, il est actuellement hébergé sur un serveur Debian 10 (Linux)**

```bash
# Cloner ce dépôt
$ git clone https://github.com/xrths/COVID19-France
```
```bash
# Accéder au dossier
$ cd COVID19-France/
```

```bash
# Installer les dépendances
$ pip install -r requirements.txt
```

    Voir la configuration de "config.ini".
```bash
# Modifier ./modules/ConfigEngine.py
parser.read('/VotreDirectory/COVID19-France/'  +  'config.ini')  #Modifier cette ligne
```

```bash
$ python3 CovidFrance.py
```

## Configuration [config.ini]

    user_id  = 1222609878889443329
    
*Changer par l'ID Twitter du compte bot*

    preview_id  = 3400092689
 *Changer par l'ID Twitter du compte du propiétaire*

    app_name  =  #RestezChezVous
*Changer par le nom que vous avez donné à l'application Twitter (sur le portail développeur)*

    account_name  = CovidFrance
 *Changer par le nom du compte bot*

    consumer_key  = xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    consumer_secret  = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    access_token  = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    access_token_secret  = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
*Remplacer par vos keys API Twitter (sur le portail développeur)*

    directory  = /root/COVID19-France/
 *Remplacer par le chemin d'accès exact ou se trouve le fichier CovidFrance.py (doit bien se finir par "/")*

    checkTime  = False
*Si True, le bot attendra d'être  dans la tranche horaire donnée pour fonctionner*

    startTime  = 18:55
    endTime  = 21:30
*Tranche horaire à définir*

    casConfirmes  =
    decesHopital  =
    decesEhpad  =
    casReanimation  =
    casHopital  =
    casGueris  =
    totalDeces  =
    casMalades  =
    casEhpad = 
    
*Permet de modifier les chiffres manuellements, laisser vide si vous ne souhaitez pas modifier.*
*Exemple de modification:*

    casMalades  = 10000
    
**Rendre le programme automatique**
Il suffit de créer une tâche CRON. Voici un exemple qui exécute le programme toutes les 8 minutes:

    */8 * * * * python3 /root/COVID19-France/CovidFrance.py > /root/COVID19-France/log.txt 2>&1

## Graphique généré automatiquement
<p align="center">
  <img src="https://i.ibb.co/Zf1gwGN/screely-1586902076592.png">
</p>

*Explication du fichier "graphData.txt"*

    |-|CAS TOTAUX CONFIRMES|HOSPITALISATIONS|REANIMATIONS|DECES|GUERIS
    0,6633,0,0,148,0 
    0,7730,2579,699,175,602
    0,9134,3626,931,264,1000

**N.B: Les "0" sont obligatoires à chaques début de ligne.** 

*J'ai fait ça rapidement et ce n'est vraiment pas optimisé, mais cela fonctionne plutôt bien.*

## Remerciements

Je tiens sincèrement à vous **remercier** si vous consultez ce repo ou même si vous avez suivis le compte, lorsque j'ai créé ce programme je ne pensais pas qu’autant de personnes me feraient **confiance** ! 

Je tiens à remercier tout spécialement l'équipe de **[@Conflits_FR](https://twitter.com/Conflits_FR)** qui ont permis de faire ****connaître**** le compte très rapidement et donc de le rendre vraiment utile au grand **public** ! 

<p align="center">
<img src="https://pbs.twimg.com/profile_images/1225053312615096322/W0iRUc1r_400x400.jpg" width="100px;"/><br /><sub><b>@Conflits_FR</b></sub></p>
<p align="center"><img src= "https://pbs.twimg.com/profile_images/1236781113198198785/uoN74yI__400x400.png" width="100px;"/><br /><sub><b>@allshebergfr</b></sub>
</p>



## Licence
Licence MIT - Contactez-moi si vous avez des questions à propos de ça.

## Contactez-moi
**Twitter - [@xrths](https://twitter.com/xrths)**

## Support
<a href="https://www.buymeacoffee.com/xrths" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
