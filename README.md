# lpgdlcFontDuLinux

membres du projet : Paul BOUQUET - Cédric DELAUNAY - Thomas LE MASSON

## Projet de Linux embarqué : contrôle d'un serveur Caméra et d'un serveur Servomoteur depuis un client déporté

Répertoires :
    - Client : contient le client python
    - Serveur_Caméra : contient le serveur Caméra et le binaire cross-compilé v4lgrab
    - Serveur_Servo  : contient le serveur contrôlant le servo-moteur

# Démarrage rapide

    - Pour le serveur caméra, les binaires sont déjà compilés. Vous pouvez donc transférer les deux exécutables sur la Raspberry, et lancer le serveur Caméra (par défaut, il est en écoute sur le port 8002). Si vous voulez recompiler le serveur caméra, il vous suffit de copier le dossier ServeurCamera/ dans le docker contenant le cross-compilateur, et d'utiliser le Makefile.
    - Pour le serveur servo-moteur, copiez le dossier sur la Raspberry, et exécutez ... 
    - Pour le client python, lancez le simplement avec en paramètres l'ip de la raspberry, le port du serveur caméra et le port du serveur servo-moteur. Suivez ensuite les instructions affichées dans votre console.


# Client Python

# Serveur Caméra

# Serveur Servomoteur


# Axes d'amélioration

    - lancer les serveurs au démarrage de la Raspberry

