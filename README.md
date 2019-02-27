# **lpgdlcFontDuLinux**

Membres du projet : Les p'tits gars d'la côte Paul BOUQUET, Cédric DELAUNAY et Thomas LE MASSON

## **Projet de Linux embarqué : contrôle d'un serveur Caméra et d'un serveur Servomoteur depuis un client déporté**

Répertoires :

- Client : contient le client python

- Serveur_Caméra : contient le serveur Caméra et le binaire cross-compilé v4lgrab

- Serveur_Servo  : contient le serveur contrôlant le servo-moteur

## **Démarrage rapide**

- Pour le serveur caméra, les binaires sont déjà compilés. Vous pouvez donc transférer les deux
  exécutables sur la Raspberry, et lancer le serveur Caméra (par défaut, il est en écoute sur le
  port 8008). Si vous voulez recompiler le serveur caméra, il vous suffit de copier le dossier
  ServeurCamera/ dans le docker contenant le cross-compilateur, et d'utiliser le Makefile. Le binaire s'appelle alors servCam.

- Pour le serveur servo-moteur, copiez le dossier sur la Raspberry, et exécutez le script `server.py` avec python2. Le serveur se lance sur le port 6667 et se connecte sur la pin 11 de la raspberry.

- Pour le client python, lancez le simplement avec en paramètres l'ip de la raspberry, le port du
  serveur caméra et le port du serveur servo-moteur. Suivez ensuite les instructions affichées dans
  votre console.

## **Flashage de la carte / Compilation de v4lgrab**

Le flashage de la carte a été réalisé en suivant l'ensemble des indications fournies dans le sujet. Nous n'avons pas jugé nécessaire de fournir les deux partitions dans ce répertoire Github.

En ce qui concerne le binaire v4lgrab, il est déjà compilé et fourni dans le répertoire Serveur_Caméra. Pour la compilation de celui-ci, nous avons utilisé les lignes de commande suivantes, en ayant au préalable remplacé tous les appels à la fonction **malloc** par des appels à la fonction **calloc** :
```./configure --host=arm-buildroot-linux-uclibcgnueabihf CC=/root/buildroot-precompiled-2017.08/output/host/bin/arm-linux-gcc```
```make```
```make install```

## **Client Python**

Le client Python permet de prendre des photos ou d'actionner le servomoteur à distance. 

Les paramètres à passer sont dans l'ordre : **l'ip de la Raspberry**, **le port du serveur camera** et **le port du serveur servomoteur**.

Les différentes instructions vous sont ensuite proposées, elles sont à entrer directement dans la console. Toute commande différant des commandes autorisées ne sera pas traitée, et la réception d'un signal **SIGINT**, **SIGSTP**, **SIGQUIT** ou **SIGTERM** entrainera la fermeture du programme et des sockets associés.

Attention : Comme la fermeture du client entraine la fermeture des sockets, vos devrez relancer les serveurs Caméra et Servomoteur pour utiliser à nouveau le client.

## **Serveur Servomoteur / Python**

Ce serveur permet de faire la liaison entre le client et le servomoteur.

Le serveur n'accepte qu'**une seule connection** jusqu'à la fin de son exécution.

On peut lancer le serveur sur le port et sur la pin de la raspeberry que l'on souhaite.

Par défaut, le serveur se lance sur le **port 6667** et la **pin 11** de la raspberry. [plan
raspberry](schema_raspeberryPI3)

Les commandes reçues par le serveur sont ensuite envoyées et traitées par le servomoteur.

Les signaux **SIGINT**, **SIGSTP**, **SIGQUIT** et **SIGTERM** sont gérés et arrêtent correctement
le serveur (On arrête le servomoteur. Puis, on coupe la connection avec le client. Enfin, la socket
est fermée). scoket est fermé)

Si aucune commande n'est envoyée, le serveur s'arrête.

On initialise le servomoteur à la position "0". C'est-à-dire, qu'il n'y pas d'angle entre la
référence de mesure des angles et l'axe du servomoteur. [documentation
constructeur](documentation_MicroServoSG90)

Le servomoteur reçoit les commandes du serveur sous forme de chaîne de caractère.

Cette chaîne de caractère est analysée à l'aide d'un **regex** pour déterminer si la commande est
correcte ou pas.

Si la commande n'est pas correte, une erreur est levée et la commande non interprétée est affichée
dans la console. Une mauvaise commande n'arrête pas le serveur, ni le servomoteur.

Si la commande est correcte, le servomoteur l'exécute.

La seule commande dsiponible est **MOVE**, suivie d'un numéro qui peut être négatif.

**Example de commande valide :** MOVE65, MOVE-16.

Le numéro représente, en degré, l'angle que l'on va rajouter à sa position actuelle.

**Exemple de fonctionnement :**

| Commandes consécutives | Position |
| ---------------------- | :------: |
| ```init```             |    0     |
| MOVE15                 |    15    |
| MOVE-45                |   -30    |

## **Serveur Caméra / C**

Ce serveur permet de prendre des photos grâce au module caméra Raspberry Pi. Par défaut, le serveur se lance et écoute le **port 8008**.

La première chose que fait le serveur est de charger le module kernel **bcm2835-v4l2** via la commande **modprobe**.

Ensuite, lorsqu'un message **PHOTO** arrive sur la socket, une photo est prise, puis renvoyée au client Python. On envoie d'abord sa taille, puis l'image bit par bit. Une fois l'opération terminée, l'image est supprimée de la Raspberry, et on se met en attente d'une nouvelle commande.

## **Axes d'amélioration**

- Nous aurions pu faire en sorte que les serveurs Camera et Servomoteur se lancent au démarrage de la Raspberry.

- Nous aurions pu rajouter plus de commandes, que ce soit pour le servomoteur ou pour la caméra (prise de plusieurs clichés par exemple pour la caméra, mouvement constant bouclé pour le servomoteur, ...)

- Eviter de coder en dur les ports des serveurs, et offrir la possibilité à l'utilisateur de le passer en paramètres.

- Automatiser la routine de copie des fichiers server du PC vers la Raspberry au moyen de scripts bash.

[schema_raspeberryPI3]:
https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png

[documentation_MicroServoSG90]:
http://www.ee.ic.ac.uk/pcheung/teaching/de1_ee/stores/sg90_datasheet.pdf

