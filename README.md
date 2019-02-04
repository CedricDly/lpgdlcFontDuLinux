# lpgdlcFontDuLinux

membres du projet : Paul BOUQUET - Cédric DELAUNAY - Thomas LE MASSON - Mathieu LOGARIO

4 fevrier : premier commit du server camera. Ce dernier est capable de recevoir l'ordre de photo, puis d'envoyer une image chargée dans le dossier de l'exécutbable. Côté client python, on reçoit correctement l'image. Néanmoins, pour le moment, il faut que la taille de l'image soit connue à l'octet près.
L'idée est qu'avant d'envoyer l'image, le server camera doit envoyer la taille de celle-ci. Pour l'instant, faire cela provoque des comportements inattendus.

Prochaines étapes : 
- modifier le code du server camera pour que lorsqu'il reçoit l'ordre de Photo, il capture la photo via v4l.
- Signal Handler pour tous le client et les serveur
