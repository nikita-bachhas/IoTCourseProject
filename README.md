# IoT Course Project - Flower Identification Application

## Image Classification of Flowers using an Android Application
 Users can take or upload any image of a flower and the type of flower is recognised and returned 

## Project Documents
1. YouTube Video:
2. Presentation Slides:
 
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
2. Download folder IoTAndroidApplication
3. Open folder in Android Studip
4. Run on either Emulated Device or Physical Device
 
 ## Flask Server

 ## Utilisation of Virtual Machine on Google Cloud Platform
