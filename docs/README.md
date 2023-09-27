# Machine Learning Project


### Step 1 : Create Virtual Environment

-  Create virtual environment using anaconda or vscode.
-  Activate virtual environment.

### Step 2 : Create file requirements.txt

-  In this file we have to mention all required libraries which we need to install and use.

### Step 3 : Create src folder

-  All work of our project will do in this folder.
-  Make __init__.py file inside src folder so it considered as package. 

### Step 4 : Create setup.py file 

-  Setup file will help to create entire packages required for project.
-  We can also trigger this setup file by using requirement file. 

### Step 5 : Create Project setup with git 

-  Install git cli(command line interface) if not exist.
-  Make repository in git hub.
-  Initialize git in local folder and make connection with github.
-  Add all files in git and push on github.
-  make .gitignore file for prevent push some unnecessary documents. 

### Step 6 : Create Project Structure

-  Inside local system create folders artifacts, notebooks, templates.
-  Inside notebook make new folder named data for origional data file.
-  Inside src folder make folders components and pipelines for save python files and pipelines.
-  make sure that inside all folders in src create file __init__.py
-  make utils.py file inside src folder.
-  make logger.py and exception.py inside src folder for logging and handling exception purpose.
-  keep pushing all data on github after complete every steps.

### Step 7 : Logging and Exception Handling

-  Inside logger.py import required libraries and type code for projects overall logg information.
-  Make logs folder inside main folder.
-  Inside exception.py file type codes for handle exception.
-  Make custom exception for return exception as our requirement format.

### Step 8 : Data Preprocessing , EDA , FE and Model Training and validation

-  Install requirements and packages.
-  Make one jupiter notebook for simply do full process of preprocessing , eda and fe. 
-  Make one more jupiter file for model training and evaluation. 
-  save this both files inside  notebooks folder

### Step 9 : Data Ingestion

-  Make data ingestion file inside components and do all process of data ingestion and also save raw data and test and train data inside artifacts.
-  Make class and functions inside class so we can call it in training pipeline for automate training purpose.
-  It will save files and return path of the file by which we will do further process.

### Step 10 : Data Transformation 

-  Make data transformation file inside components for purpose of preprocessing and fe automation .
-  import data from artifacts and do preprocessiong automation and also scaling and save preprocessor model inside artifacts and return preprocessed data .

### Step 11 : Model Training 

-  Make model training file inside components folder for training model and also for evaluation.
-  Here also we have to create classes and methods for automate training purpose and also save model to artifacts for prediction.
-  Keep remember that some functionalities code will written in utils file and with the help of sys library we will get it to our folders.

### Step 12 : Training Pipeline 

-  Make training pipeline fil einside pipelines folder.
-  Training pipelines main purpose is to automate total process.
-  we will call class and its methods to training pipeline for purpose of automation.
-  Firstly we have to call class of data ingestion and by that we will get path of raw data.
-  Then we call data transformations class and method for preprocessiong autometion it will use raw data path which we are getting from data ingestion.
-  It will give use preprocessed data for further process.
-  Then we call model training classes and methods for automate model training purpose.
-  It will take preprocessed data from data transformation automation process and do model training on this data.
-  After complete model training we find the we will evaluate model and also save model.
-  We need to do logging after every required stap and also try and exception.
-  we have to save results and evaluation metrics as logs.
-  After evaluate model and save it our training pipeline process is completed. 

### Step 13 : Prediction Pipeline

-  Make prediction pipeline file inside pipelines folder.
-  Main purpose of this file is to use preprocessor and model for prediction.
-  We need to det both preprocessor and machine learning model and make objects of that.
-  With the help of this we will predict our result.
-  Make class and methods for automate intire process and get predicted result.
-  Make classes for get data by frontend so we can do prediction by our model.

### Step 14 : FrontEnd

-  Inside templates folder make html file for Home page.
-  Make one more html page for data gathering purpose and make form inside that by which we get data.
-  Make one result file for show our result or we can also render result in same form.
-  We can also do special styles by css for attractive vision.

### Step 15 : Application file 

-  Make application file to main project folder for merge overall concept and get data do process and render result.
-  Get data from front end.
-  Call class and methods from prediction pipeline and do prediction on data.
-  Result show on frontend with result html file and by here our project is completed 
-  In the last make readme markdown file to explain and type anything about project.
