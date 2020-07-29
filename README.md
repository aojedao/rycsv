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
