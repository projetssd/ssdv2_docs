#Handbrake

This is a Docker container for HandBrake.

The application's GUI can be accessed through a modern web browser (no client-side installation or configuration needed) or through any VNC client.

A fully automated mode is also available: drop files into a watch folder and let HandBrake process them without any user interaction.

![handbrake](https://user-images.githubusercontent.com/64525827/147670229-0f9f3e36-b734-42ae-ac55-de82570b4489.png)


### HandBrake is a tool for converting videos of almost any format to a selection of modern and widely supported codecs.

* $HOME: this location contains the files of your host which must be accessible by the application.
* $HOME/USER/local/HandBrake/watch: This is where the videos to be automatically converted are located.
* $HOME/USER/local/HandBrake/output: This is where automatically converted video files are written.

Navigate to http://your-host-ip:5800 to access the HandBrake GUI. The host files appear under the /storage folder in the container.