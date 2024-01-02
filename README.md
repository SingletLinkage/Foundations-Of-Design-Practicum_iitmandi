# Problem Statement 5: Convex Shape Detection
### Batch 2023 - ODD Semester (Aug-Dec)
### Group 5

Hey, I'm Arka, CSE undergrad ('27) at IIT Mandi - This repository is for our First Year FDP (Foundations of Design Practicum) project. Our problem statement involved going around some object (concave or convex) and detecting whether it was convex or not. Our robot uses *Real Time Path Plotting*, *Turning Angle Detection*, and *Computer Vision* to analyse the path followed and decide concavity. Pleae do not copy and paste the code directly from here, try to learn the logic and then implement it by yourself. For questions/suggestions feel free to contact me! (Discord: _qchaos)  

**Sensors:** HC-SR04 ultrasonic sensor  
**Microcontroller:** NodeMCU ESP8266 (WiFi connectivity!)  

### Members:
1. Bhumika B23036
2. Diksha B23071
3. Arka B23120
4. Pranjal B23170
5. Nitesh B23219

### Tutors:
1. Aditya Sharma B22083
2. Chetan Kukreja B22097

### Code Logic at Present:
As soon as theta reaches 360 degrees, the robot stops. If the robot encounters any concave (has to be a bit too concave!) path ahead of it (distance from front sensor < threshold value), then too it'll stop. How to know if shape is concave or convex? If the robot stops before coming to its initial starting point, its a concave shape.  
As an alternate system, [this script](./scripts/is_convex.py) uses another method to determine concave/convex.  

## Code Struture and Working:

### ESPCode.ino:
> Libraries used: *[ESPAsyncWebSrv](https://reference.arduino.cc/reference/en/libraries/espasyncwebsrv/)*, *[ESP8266WiFi](https://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/readme.html)*, and *math*

This code uses time interval between two successive right/left turn calls to determine angle rotated (`theta = angular velocity * time`). Note that the value of angular velocity (`thetapersec`) is solely determined by experiments, not by theoretical calculations. Counters (`right_c, left_c`) are to filter out rouge left/right turn calls when the robot goes slightly out of the permissible distance range. It also determines the x,y coordinates of the robot using `x += v * cos theta` and `y += v * sin theta`. Again, the value of `v` is kind of random because we did not need accurate value of `v`. Then, the ESP runs a server which sends `(x,y)` coordinates and `theta` values whenever a request is sent to it.

### Python Scripts:
> Libraries used: *[requests](https://docs.python-requests.org/en/latest/user/quickstart/)*, *[OpenCV](https://opencv-python.readthedocs.io/_/downloads/en/latest/pdf/)*, *[NumPy](https://numpy.org/doc/)*

1. ***main*** - This starts the execution of the whole program. It was supposed to start both *input_data* and *dynamic_plot* simultaneously and then call *detection.py* when dynamic plot was either killed or ended. However, as of now (8th Dec) all three files start simultaneously (IDK why).
2. ***input_data*** - This sends a request to the ESP Web Server; parses the data received to extract `x,y` position of the robot and writes the coordinates in a CSV file.
3. ***writecsv*** - Writes data to a CSV file.
4. ***dynamic_plot*** - Reads the data from the csv every `DELAY` ms and plots it to generate an animation like view using *FuncAnimation* of *matplotlib*.
5. ***detection*** - Calls *drawfig* and *shape_from_image* to draw and analyse CSV points.
6. ***drawfig*** - Constructs the final image of object from the (x,y) coordinated saved in CSV file and saves the generated image in a file.
7. ***shape_from_image*** - Uses OpenCV to generate contours and passes that data to *shape_from_vertices*. Then using the returned array of corner points, it overlays the shape and the corner point coordinated on the shape itself.
8. ***shape_from_vertices*** - It runs OpenCV's **[approxPolyDP](https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html)** on list of contours to detect actual corner points of the shape; it then computes shape using number of corner points and return it.
9. ***is_convex*** - Determines whether shape from corner points. WORKING: It constructs vectors along length of sides; all in the same direction (by subtracting initial point x,y from final point x,y). If the cross product of each pair of consecutive vector yields a vector in the same direction, then the shape is convex. Otherwise, it's concave. (See [this picture](convexLogic.png) for a better understanding).
