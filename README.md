# Raspberry image controller

This software was developed to show how to combine **Raspberry** board with machine learning. It performs an abstract task of fan speed control via digit which you show to the USB camera.

## Necessary electronic elements

For code usage the follow details are required:
* Raspberry board with installed **OS** and **python**
*  USB or special Raspberry camera
* 7-segment display
	> Additional resistors for each pin are needed
	
* Fan or another small motor
	> It is better if motor has no battery requirements

* Transistor
	> PNP or NPN depends on the way how you want to connect fan
	
* Enough wires 

## Pin connections
The main challenge in the circuit connection is the fan. The example is described on the figure below:
![image](https://github.com/Padniuk/RaspberryImageControler/blob/main/fan.jpg)

Other stuff can be simply connected. 
> Remember to adhere to pin numbering in the code and real wires connected to pins!

> Do not forget about resistors for 7-segment display!

## CNN

For the classification task CNN with the follow structure was used(**Tensorflow**):
```python
model = models.Sequential() 
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1))) 
model.add(layers.MaxPooling2D((2, 2))) 
model.add(layers.Conv2D(64, (3, 3), activation='relu')) 
model.add(layers.MaxPooling2D((2, 2))) 
model.add(layers.Conv2D(64, (3, 3), activation='relu')) 
model.add(layers.Flatten()) 
model.add(layers.Dense(64, activation='relu')) 
model.add(layers.Dense(10, activation='softmax'))
```
In other way any other model can be used.
> **MNIST** was used as database
> Neural network was trained separately from the Raspberry board! 

After training process all trained weights was saved into file with **.h5** extension. This file can be loaded to the root directory of the project or path to the file inside the code should be changed.
