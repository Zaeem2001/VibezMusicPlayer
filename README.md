# Vibez Music Player
## Made by Zaeem Ghauri

### What is this?

This is the last project I worked on during my Summer break of 2021. It was my first ever experience with OpenCV, TensorFlow and other computer vision tools so I had to do a lot of research. The conceptual idea was simple: create a program that looks at your face and determines the emotion then plays music to match the mood. Bringing this to reality was not. The program was coded in Python and uses many libraries and frameworks (such as OpenCV, Keras, and TKinter) that I've never used before. The tools used to detect/recognize the user's face and emotions weren't always accurate and this led to some problems in consistency. Nevertheless, I still believe the program fullfills its purpose and is thus successful.

-----
### Some important definitions

Before I continue, if you are new to the world of artificial intelligence (AI), I think its best if I quickly explain some terms. If you're already knowledgable about the topic, stick around anyways and correct me in case I'm wrong (please). 

Artificial intelligence is essentially a simulation of human intelligence, the way we act and think, through a machine. Machine learning is a subset of AI focused on teaching machines with algorithms that analyse data in order improve the accuracy of the AI. Computer vision is another a subset of AI with a more precise focus on obtaining information through exclusively images and video. Just because machine learning and computer vision are both subsets of AI doesn't mean that one isn't used without the other. In fact, machine learning is responsible for improving the accuracy of image detection and recognition in computer vision and thus making it more efficient. Now deep learning is a subset of machine learning. It uses neural networks to automate part of the learning process which allows it to learn from a larger dataset. I encourage you to do your own research and learn more about these subjects in detail, especially when a lot of this information can be found online (and for free).
  
![AI Diagram](https://user-images.githubusercontent.com/86279858/133029386-d98bd387-4de2-4a68-80c6-cda6d5edc759.png)

-----

### How does it work?

This program is purely software and requires no hardware to use/run. There are 2 important libaries and a framework being used: TKinter, OpenCV, and Keras. TKinter is a Python GUI package, it was used to build the interface of the program. The program starts by capturing and detecting the user's face in realtime with the help of OpenCV, a computer vision library used to process images and videos. The facial detection is done through the CascadeClassifier class which uses a Haar Cascade to compare and recognize the front of a human face. The information from the user's face is then passed on to Keras, a deep learning framework. Keras uses its different libraries to process the data from the user's face and compares it to a (trained) model of possible human emotions. It lists the probability of each emotion currently being displayed and the program chooses the most likely option. The guessed emotion is then displayed on top of the video capture, along with other useful information, in realtime. Finally, when the user presses the "play music" button the program will send a request to the Spotify server and start playing the specified playlist on the user's current device (just like in my [Spotiplayer project](https://github.com/Zaeem2001/SpotifyMusicPlayer)).

-----

### How do I use it?

1. Copy the files from this repository to your PC and open them in a Python IDE of your choice (I recommend PyCharm).

2. Make sure you have the necessary libaries installed on your PC: TKinter, PIL, OpenCV, numpy, and TensorFlow (some of these are already included in Python as base libraries).

3. Make sure you have the Spotify desktop application installed and running on your PC along with an authorization token.

4. Finally, run the main Python script (Emotion+Music.py).

*See my [Spotiplayer project](https://github.com/Zaeem2001/SpotifyMusicPlayer) for a guide on how to get an authorization token for the Spotify part of the application.*

-----

### Special thanks to Karan Sethi who provided the emotion detection models for everybody to use!                                                                       
Here's a [link](https://github.com/karansjc1) to their GitHub profile.


### Visit [my website](https://zaeem2001.github.io/projects/vibez.html) to see my project in action!

