# Vibez Music Player
## Made by Zaeem Ghauri

### What is this?

This is the last project I worked on during my Summer break of 2021. It was my first ever experience with OpenCV, TensorFlow and other computer vision tools so I had to do a lot of research. The conceptual idea was simple: create a program that looks at your face and determines the emotion then plays music to match the mood. Bringing this to reality was not. The program was coded in Python and uses many libraries and frameworks such as OpenCV, Keras, and TKinter. The tools I had to use forced some innaccuracies in the program that I didn't expect. Nevertheless, I still believe the program fullfills its purpose and is thus successful.

### Some important definitions

Before I continue, if you are new to the world of artificial intelligence (AI), I think its best if I explain some terms. If you're already knowledgable about the topic, stick around anyways and correct me in case I'm wrong (please). 

Artificial intelligence is essentially a simulation of human intelligence, the way we act and think, through a machine. Machine learning is a subset of AI focused on teaching machines through algorithms that analyse the data given and improve the accuracy of the AI. Computer vision is another a subset of AI 

### How does it work?

This program is purely software and requires no hardware to use/run. There are 2 important libaries, OpenCV and TKinter, and 1 framework, Keras, being used. TKinter is a Python GUI package, it was used to build the interface of the program. OpenCV is a computer vision library used to process images and videos. In this case it was used to capture and detect the user's face in realtime and finally display it with the necessary information. Keras is a deep learning framework used to train neural network models. This program uses Keras to process the data taken from video capture and compare it with a given model to determine the user's emotion. 

