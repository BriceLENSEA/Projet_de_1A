# ENSEA-Projet

Le projet se place au sein du projet CoHoMa II (coopération homme-machine) de l’Armée de Terre. Le projet CoHoMa a pour but d’incarner des sections de reconnaissance robotisées qui doivent se déplacer sur un parcours parsemé de pièges modélisant des obstacles qui doivent être désactivés pour pouvoir avancer. Le retour d’expérience de l’année prochaine a montré un manque d’autonomie, au sens sans fil, des robots. Il a donc été convenu d’améliorer cette autonomie en ajoutant un réseau secondaire utilisant des balises wifi. Ainsi, pour mettre en place ce réseau il est nécessaire de déployer et récupérer les balises à des points stratégiques d’où l’utilisation d’un bras robot sur une base mobile. On se concentrera sur la commande globale haut niveau du bras en intégrant un système ROS.


Le projet était d’intégrer un système ROS implémenté sur une carte Raspberry afin d’effectuer une commande haut niveau entre le bras robot doté d’une carte STM32 et une interface utilisateur. Nous disposions d’un bras robot uStepperArm Rev 4 et d’une machine virtuelle de l’école sur laquelle ROS 1 Noetic était installé. Le uStepperArm Rev 4 est un bras composé de 3 moteurs commandant 3 axes et permettant un déplacement à 360° autour de la base du bras. Une pince est placée à l’extrémité du bras et est orientée vers le bas, peu importe la rotation des moteurs et donc le positionnement du bras. Le bras que nous avons utilisé présente des contraintes mécaniques que nous devions résoudre afin de permettre une meilleure maniabilité du bras.

Besoins :
-	Faire bouger le bras robot en fonction :
  •	D’une position demandée
  •	D’une commande d’angle
-	Implémentation dans un projet plus vaste

Contraintes :
-	Utiliser ROS
-	Communication UART avec les actionneurs
-	Contraintes mécaniques du bras


Nous avons utilisé ROS 1 Noetic

Afin de commencer à utiliser ROS

Nous avons passer beaucoup de temps à étudier le tutoriel sur le wiki ROS:

http://wiki.ros.org/ROS/Tutorials

(les points 8 et 9 ne sont pas forcément pertinent et peuvent être passés)
