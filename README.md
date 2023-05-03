# Intenet of Things (IoT) Course Project - Flower Identification Application

## Image Classification of Flowers using an Android Application
 Users can take or upload any image of a flower and the type of flower is recognised and returned 
 
 <img src="https://user-images.githubusercontent.com/72136295/235590518-9c649af5-e367-4346-91ed-2a2480927efe.png" width="341" height="301">   

## Project Documents
1. [YouTube Video](https://youtu.be/qjLQg6UKjX8)
2. [Presentation Slides](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/Documentation/IoT%20Course%20Project%20Presentation%20Slides.pptx)
3. [Application Demonstration - Selecting a Photo of a Calendula Flower from Gallery](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/Documentation/Calendula-Gallery.mp4)
4. [Application Demonstration - Selecting a Photo of a Carnation Flower from Gallery](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/Documentation/Carnation-Gallery.mp4)
5. [Application Demonstration - Taking a Photo of a Sunflower Flower using Device Camera](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/Documentation/Suflower-Camera.mp4)
6. [Application Demonstration - Taking a Photo of a Daisy Flower using Device Camera](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/Documentation/Daisy-Camera.mp4)
 
## Training of Model
 
 `Dataset`
 - flowersDataset obtained from the following dataset found on Kaggle: [Flower Dataset](https://www.kaggle.com/datasets/l3llff/flowers) 

`Google Teachable Machine`

- The dataset contains the following 16 categories of flowers:
   - Astilbe (737 Images)
   - Bellflower (873 Images)
   - Black Eyed Susan (1000 Images) 
   - Calendula (978 Images)
   - California Poppy (1022 Images)
   - Carnation (923 Images)
   - Coreopsis (1047 Images)
   - Daffodil (970 Images)
   - Daisy (980 Images)
   - Dandelion (1052 Images)
   - Iris (1054 Images)
   - Magnolia (1048 Images)
   - Rose (999 Images)
   - Sunflower (1027 Images)
   - Tulip (1048 Images)
   - Water Lily (982 Images)
   
   
- Total Batch Size *(Total number of images in the dataset)*: 15,740
- Training Dataset - 85% *(Used to train the models to correctly classify the image samples into the pre-existing classes)*: 13,379
- Test Dataset - 15% *(Not used to train the model; assess how well the model is performing on new, un-seen data)*: 2,361
- Epoch *(The number of times the training dataset has been fed through the model)*: 60
- Batch Size *(batch = set of samples used in one iteration of training)*: 16 --> *Number of Batches = 13,379/16 = 837*
- Learning Rate *(A tuning parameter in an optimization algorithm that determines the step size at each iteration while moving toward a minimum of a loss function)*: 0.001

![Screenshot 2023-04-29 at 11 27 27 PM](https://user-images.githubusercontent.com/72136295/235311022-b952e2ff-6754-43d8-a41a-64dfeede6805.png)

`Testing of the Image Classification Model`
- Test images used to test accuracy of the image classification model: [testImages](https://github.com/nikita-bachhas/IoTCourseProject/tree/main/testImages)

`Classification Results`

- Accuracy Per Class:

![Accuracy Per Class](https://user-images.githubusercontent.com/72136295/235311084-8caa8812-7a61-4657-9cce-c9c6109d468b.png)

- Accuracy Per Epoch:

![Accuracy Per Epoch](https://user-images.githubusercontent.com/72136295/235311092-011d2d20-3ebd-4804-ba06-cbce972d2169.png)

- Confusion Matrix:
   - 3 Classes Most **Easiest** to Identify Based on the Confusion Matrix:
      1. Dandelion - 154
      2. Tulip - 154 
      3. Sunflower - 150
   - 3 Classes Most **Difficult** to Identify Based on the Confusion Matrix:
      1. Astilbe - 105 
      2. Bellflower - 109
      3. Carnation - 118

![Confusion Matrix](https://user-images.githubusercontent.com/72136295/235311098-d9c19bfe-14c5-42c8-a08c-542e4a4b8d12.png)

- Loss Per Epoch:

![Loss Per Epoch](https://user-images.githubusercontent.com/72136295/235311109-4c5b1acd-68be-42ff-b72a-2f35543ee87b.png)

## Development of Android Application

1. Install Android Studio Flamingo 
2. Download folder [IoTAndroidApplication](https://github.com/nikita-bachhas/IoTCourseProject/tree/main/IoTAndroidApplication)
3. Open folder in Android Studio
4. Change IP Address to your own in *NetworkClient.java* 

<img width="503" alt="NetworkClient java IP Address" src="https://user-images.githubusercontent.com/72136295/235318182-a777f42e-1629-40c1-9e86-cd296bc85bce.png">

5. Run on either Emulated Device or Physical Device

<img src="https://user-images.githubusercontent.com/72136295/235587167-39f53825-8d56-4cea-86a4-520c50d54b25.jpeg" width="202" height="427">     <img src="https://user-images.githubusercontent.com/72136295/235587179-180189ef-e69a-4fe6-b8fa-f3ebab10e615.jpg" width="202" height="427">

## Flask Server

`Steps to Start & Run Flask Server`

1. Download folder [FlaskServer](https://github.com/nikita-bachhas/IoTCourseProject/tree/main/FlaskServer) and open in any IDE
2. Ensure Python Version > 3.8 using the following command: **python3 --version**
3. Ensure Pip Version > 20.3: **pip3 --version**
4. Install Miniconda using the following command: **curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.shbash Miniconda3-latest-MacOSX-x86_64.sh** *(specifically for MacOS; Choose according to your OS)*
5. Create a Conda Environment using the following command: **conda create --name tf python=3.9**
6. Activate Conda Evironment using the following command: **conda activate tf**
7. Upgrade Pip using the following command: **pip install --upgrade pip**
8. Install TenserFlow using the following command: **conda install -c conda-forge tensorflow**
9. Install all necessary packages: *pillow, flask, etc*
10. Change IP Address to your own in *test.py*:

<img width="1179" alt="test py Water Lily Test File" src="https://user-images.githubusercontent.com/72136295/235317822-a163fd4a-706a-4c32-86fc-004e8d818dfe.png">

11. Change to an available port number to utilise in *model.py*:

<img width="378" alt="model py Port Number" src="https://user-images.githubusercontent.com/72136295/235318212-e19e295c-f78c-44c5-8de6-3c7c19aad6fc.png">

12. Change directories to the FlaskServer folder using the following commad: **cd FlaskServer**
13. Run python file, using the following command: **python *model.py*** 
14. To deativate the Conda Environment, run the following command: **conda deactivate**

`test.py`

1. Add any flower image that you wish to test to the following folder: [testImages](https://github.com/nikita-bachhas/IoTCourseProject/tree/main/testImages)
2. Change the following file path in [test.py](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/testImages/test.py): *resp = requests.post("http://192.168.10.141:8000", files={'file': open('/Users/nikitabachhas/IoTCourseProject/IoTCourseProject/TestImages/water_lily.jpg', 'rb')})*
3. Execute the model.py in the FlaskServer folder
4. Execute test.py file

`test.py results`
 - The following imges shows the results obtained when the test image of a water lily is used to test the integration of the flask server with the model and the accuracy of the model:

<img width="1179" alt="test py Water Lily Test File" src="https://user-images.githubusercontent.com/72136295/235317822-a163fd4a-706a-4c32-86fc-004e8d818dfe.png">

<img width="982" alt="test py Water Lily Test Results" src="https://user-images.githubusercontent.com/72136295/235317829-cdd824a3-cfae-4791-a0d4-2d853ffbfa8f.png">

## Google Cloud Platform Virtual Machine 

`Steps to Create a VM Instance`

1. Click on **Compute Engine**
2. Click on **VM Instances**
3. Ensure that **Region = asia-southeast1(Singapore)**
4. Click Create

<img src="https://user-images.githubusercontent.com/72136295/235889889-cce6cd9b-8c17-4fb2-8674-def4587a1473.png" width="808" height="481">   

`Steps to Start & Run Flask Server on VM`

1. Use the command **pwd** to identify the directory that you are in and the command **ls** to get a list of all the files downloaded or uploaded into the virtual machine
2. Install wget onto your virtual machine using the following command: **sudo apt-get install wget**
3. Download Miniconda onto your virtual machine using the following command: **wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh** *(specifically for those using a Debian/Linux VM)*
4. Execute the downloaded Miniconda file in your virtual machine by using the following command: **bash Miniconda3-latest-Linux-x86_64.sh**
5. Restart your virtual machine
6. Ensure python is installed by using the following command: **python**
7. Exit from the python environment using the following command: **exit()**
8. Upload these three files into the vritual machine: *keras_model.h5*, *labels.txt* and *model.py*
9. Create a Conda Environment using the following command: **conda create --name tf python=3.9**
10. Activate Conda Evironment using the following command: **conda activate tf**
11. Upgrade Pip using the following command: **pip install --upgrade pip**
12. Install TenserFlow using the following command: **conda install -c conda-forge tensorflow**
13. Install all necessary packages: *pillow, flask, etc*
14. Run python file, using the following command: **python *model.py*** 
15. To deativate the Conda Environment, run the following command: **conda deactivate**

<img src="https://user-images.githubusercontent.com/72136295/235890559-7321a403-55f0-489d-b913-13f5423ef2a5.png" width="762" height="164">   
