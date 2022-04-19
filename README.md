# Laboratorio 2 - Modelo Geométrico Inverso
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Leviatt/Lab1">
    <img src="images/UNShield.png" alt="Logo" width="222" height="94">
  </a>

  <h3 align="center">Laboratorio 2 - Robótica</h3>
  

## Integrantes
* Alejandro Ojeda Olarte
* Mateo Rodriguez
* Brayan Calderon
## Desarrollo
Se desarrolló en MATLAB el Laboratorio 2, con los toolboxes Robotics System Toolbox y Robotics, Vision & Control de Peter Corke.








# Robótica y Control Servo-Visual

En este repo encontramos los diferentes talleres y desarrollos para la materia, cada taller tiene su carpeta y el proyecto final del curso posee una carpeta propia.

Todos los robots son simulados en Gazebo en base al framework ROS, y codificado con Python.
# PAQUETES NECESARIOS PARA EJECUTAR EL PROYECTO:

1. **orb_slam_2_ros**. (Instrucciones de instalación [aquí](https://github.com/appliedAI-Initiative/orb_slam_2_ros)). 
  - `ros/src/Node.cc` debe ser reemplazado por `Proyecto/orb_slam_2_ros/Node.cc`  
  - En la carpeta`ros/launch/` se debe añadir el archivo `Proyecto/orb_slam_2_ros/mono.launch`
Para correr el SLAM ejecute en un terminal nuevo:
```
roslaunch orb_slam_2_ros mono.launch
```
