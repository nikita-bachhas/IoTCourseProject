# IoT Course Project - Flower Identification Application

## Image Classification of Flowers using an Android Application
 Users can take or upload any image of a flower and the type of flower is recognised and returned 

## Project Documents
1. [YouTube Video]()
2. [Presentation Slides]()
 
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
 
## Flask Server

`Steps to Start & Run Flask Server`

1. Download folder [FlaskServer](https://github.com/nikita-bachhas/IoTCourseProject/tree/main/FlaskServer) and open in any IDE
2.Ensure Python Version > 3.8 using the following command: **python3 --version**
3. Ensure Pip Version > 20.3: **pip3 --version**
4. Install Miniconda using the following command: **curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.shbash Miniconda3-latest-MacOSX-x86_64.sh**
5. Create a Conda Environment using the following command: **conda create --name tf python=3.9**
6. Activate Conda Evironment using the following command: **conda activate tf**
7. Upgrade Pip using the following command: **pip install --upgrade pip**
8. Install TenserFlow using the following command: **conda install -c conda-forge tensorflow**
9. Install all necessary packages: *pillow, flask, etc*
10. Change IP Address to your own in *test.py*:

<img width="1179" alt="test py Water Lily Test File" src="https://user-images.githubusercontent.com/72136295/235317822-a163fd4a-706a-4c32-86fc-004e8d818dfe.png">

11. Change to an available port number to utilise in *model.py*:

<img width="378" alt="model py Port Number" src="https://user-images.githubusercontent.com/72136295/235318212-e19e295c-f78c-44c5-8de6-3c7c19aad6fc.png">

12. Run python file, using the following command: **python *runfile.py*** 
13. To deativate the Conda Environment, run the following command: **conda deactivate**

`test.py`

1. Add any flower image that you wish to test to the following folder: [testImages](https://github.com/nikita-bachhas/IoTCourseProject/tree/main/testImages)
2. Change the following file path in [test.py](https://github.com/nikita-bachhas/IoTCourseProject/blob/main/testImages/test.py): *resp = requests.post("http://192.168.10.141:8000", files={'file': open('/Users/nikitabachhas/IoTCourseProject/IoTCourseProject/TestImages/water_lily.jpg', 'rb')})*

`test.py results`
 - The following imges shows the results obtained when the test image of a water lily is used to test the integration of the flask server with the model and the accuracy of the model:

<img width="1179" alt="test py Water Lily Test File" src="https://user-images.githubusercontent.com/72136295/235317822-a163fd4a-706a-4c32-86fc-004e8d818dfe.png">

<img width="982" alt="test py Water Lily Test Results" src="https://user-images.githubusercontent.com/72136295/235317829-cdd824a3-cfae-4791-a0d4-2d853ffbfa8f.png">

 ## Utilisation of Virtual Machine on Google Cloud Platform
