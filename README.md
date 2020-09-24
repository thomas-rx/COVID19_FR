
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/xrths/COVID19_FR">
    <img src="https://i.ibb.co/Xk9psjP/TWITTER-LOGO.png" alt="Logo" width="200" height="200">
  </a>

  <h2 align="center">COVID-19 France</h2>
  <h5 align="center">Robot in use available on Twitter.</h5>

  <p align="center">
  <a href="https://twitter.com/CovidFrance"><strong>Voir sur Twitter »</strong></a>
  <br>
<br>
<img src="https://img.shields.io/twitter/follow/CovidFrance?label=%40CovidFrance&style=for-the-badge" alt="Twitter account">
    <br>
    <br>
          <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Made with python">
    <br />
    <br />
    <a href="https://github.com/xrths/COVID19_FR/issues">Rapporter une erreur ❌</a>
    ·
    <a href="https://twitter.com/messages/3400092689-1222609878889443329?recipient_id=3400092689&text=Bonjour%2C+j%27aimerai+proposer+une+nouvelle+fonctionnalit%C3%A9+pour+le+compte+Twitter+%40CovidFrance.+Je+m%27explique%3A++">Proposer une idée 🧠</a>
  </p>
</p>

## À-Propos 🦠

<img src="https://img.shields.io/twitter/follow/Mediavenir?color=red&label=Mediavenir&style=for-the-badge" alt="Mediavenir Twitter account">

Ce projet existait à la base pour améliorer mon niveau de programmation en Python. Grâce au compte Twitter [@Mediavenir](https://twitter.com/Mediavenir) il est devenu un réel outil et une source d'information pour le [COVID-19 en France](https://www.santepubliquefrance.fr/dossiers/coronavirus-covid-19/). 

Les personnes qui ont [contribué](https://github.com/xrths/COVID19_FR/graphs/contributors) aux projets m'ont vraiment aidé à améliorer la qualité du code et la stabilité de ce programme.

Merci à vous tous ! 

## Données disponibles (FR) 📑

Les données sont fournies par le [Ministère de la Santé et des Solidarités](https://solidarites-sante.gouv.fr/).
Le programme lit les données brutes sur ce [fichier JSON](https://github.com/opencovid19-fr/data/blob/master/dist/chiffres-cles.json).
Merci à l'équipe derrière [opencovid19-fr](https://github.com/opencovid19-fr/data) pour ce travail immense.

### Les données suivantes sont utilisées (officielles)  ✅:
 - **casConfirmes** - *Nombre cumulé de cas de COVID-19 confirmés par un test positif.*

- **decesHopital** - *Nombre cumulé de décès de patients hospitalisés pour COVID-19 depuis le 1er mars 2020.*

- **decesEhpad** - *Nombre cumulé de décès en EHPAD et EMS (établissements médico-sociaux).*

- **totalDeces** - *Cumul des décès.*

- **casReanimation** - *Nombre de patients actuellement en réanimation ou soins intensifs.*

- **casHopital** - *Nombre de patients actuellement hospitalisés pour COVID-19.*

- **casGueris** - *Nombre cumulé de patients ayant été hospitalisés pour COVID-19 et de retour à domicile en raison de l’amélioration de leur état de santé.*

- **casMalades (non officiel & représenté par le calcul suivant)**: *cas_confirmes -  (total_deces + cas_gueris)*

- **casConfirmesEhpad** - *Nombre de cas confirmés par test PCR en EHPAD et EMS. Ce chiffre est inclus dans le nombre total de cas confirmés.*

### Les données suivantes peuvent êtres aussi utilisées (Worldmeters, fortement déconseillé ❌):

*Exemple:*

    {'country': 'France', 'cases': 112950, 'todayCases': 3881, 'deaths': 10869, 'todayDeaths': 541, 'recovered': 21254, 'active': 80827, 'critical': 7148, 'casesPerOneMillion': 1730, 'deathsPerOneMillion': 167, 'totalTests': 224254, 'testsPerOneMillion': 3436}

## Fichier de configuration ⚙️

- **user_id** = Identifiant de compte Twitter du compte robot.
- **preview_id** = Identifiant du compte Twitter du propriétaire.
- **app_name** = Nom de l'application qui héberge le bot (Twitter Dev Panel).
- **account_name** = @ du compte Twitter (robot).
- **consumer_key, consumer_secret, access_token, access_token_secret** = Twitter Dev panel.
- **checkTime** = Si oui, attend d'être dans l'intervalle horaire pour vérifier les données.
- **startTime** = Début du créneau horaire.
- **endTime** = Fin du créneau horaire.
- **[customData]** = Permet d'insérer des données manuellement.
- **countryView** = Nombre de pays à afficher sur le graphique mondial.
- **[traductionGraph]** = Traduit le pays donné (EN).
- **[traductionGraph]** = Traduit les mois de l'année (1 = Janvier, 12 = Décembre).

## Installation 🖥

- **1.** Récupérer des clefs pour l'API sur [Twitter Developer](https://developer.twitter.com/en).
- **2.** Cloner le dépot:
```sh
git clone https://github.com/xrths/COVID19_FR
```
- **3.** Installer les dépendances:
```sh
pip3.8 install -r requirements.txt
```

- **5.** Configurer avec le fichier de configuration.
- **6.** Exécuter le programme:
```sh
python3.8 CovidFrance.py
```
- **7.** Automatiser le programme:
```sh
crontab -e 
```
```sh
*/8 * * * * python3.8 /root/COVID19_FR/CovidFrance.py > /root/COVID19_FR/log.txt 2>&1
```

## Contribuer 🌍

Ce sont les contributions qui font de la communauté open source un endroit si extraordinaire pour apprendre, inspirer et créer. Toutes les contributions que vous apportez sont **appréciées**.

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commit vous changements (`git commit -m 'Add some AmazingFeature'`)
4. Push à la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une pull request.

## License ⚖️
<img src="https://img.shields.io/github/license/xrths/COVID19_FR?color=red&style=for-the-badge" alt="MIT LICENSE">

Distribué sous une licence MIT. Regardez `LICENSE` pour avoir plus d'informations.

## Contact 📧
<img src="https://img.shields.io/twitter/follow/xrths?color=red&label=%40xrths&style=for-the-badge" alt="XRTHS Twitter Account">

Thomas ROUX - [@xrths](https://twitter.com/xrthd) - thomas.roux@etu.iut-tlse3.fr

Project Link: [https://github.com/xrths/COVID19_FR](https://github.com/your_username/repo_name)


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/xrths/COVID19_FR?style=for-the-badge
[contributors-url]: https://github.com/xrths/COVID19_FR/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/xrths/COVID19_FR?style=for-the-badge
[forks-url]: https://github.com/xrths/COVID19_FR/network/members
[stars-shield]: https://img.shields.io/github/stars/xrths/COVID19_FR?style=for-the-badge
[stars-url]: https://github.com/xrths/COVID19_FR/stargazers
[license-shield]: https://img.shields.io/github/license/xrths/COVID19_FR?style=for-the-badge
[license-url]: https://github.com/xrths/COVID19_FR/blob/master/LICENSE
[product-screenshot]: images/screenshot.png