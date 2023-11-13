# Telemarketing Subscription Analaysis


# Environment setup 

To get started, follow these steps:

1. Fork and clone this repository. 
    ```
    https://github.com/asif-mahmud-am/Bank-Deposit-Subscription-ML
    ```
2. After you fork this repository, it will be a part of your github. Then you can clone the repository in your home directory.
    ```
    git clone https://github.com/your-username/asif-mahmud-am/Bank-Deposit-Subscription-ML
    ```
    <br>
     Incase if you need help to clone the repository:
     
     ```
      a. Go to your Git account
      b. Go to Settings-> Developer Settings->Personal Access Token
      c. Click on Generate new token
      d. Create a token with title you want and with the functionalities
      e. When you are cloning the private repo, by using git clone repoName,
        after entering your username, give personal access token as the password.
     ```  
3. After that, create a conda environment 
    ```
    conda create -n bank python=3.10.0
    ```
4. Activate the environment 
    ```
    conda activate bank
    ```
5. Install the packages 
    ```
    pip install -r requirements.txt
    ```

# Run the notebook 

Download the dataset from the [link](https://docs.google.com/spreadsheets/d/1JmGVyfVgn2i0uhDZk4xc5kBDtlPqPnugT0HhcNYfNXY/edit#gid=0) and put the excel file inside the data folder.

There is a notebook named ```data_visualization.ipynb```, you can run the notebook by each cell and see the output. 

# Run the app 

Run this command 

```
uvicorn app:app --host 0.0.0.0 --port 8000 --reload 
```

Your fast api app will be run in localhost:8000

to see the Fastapi interface, go to 
```
localhost:8000/docs
```
route. 

There is a post route named ```predict``` in the interface, you can enter values in the parameters and then hit execute. 

The data will be sent to the model and output will be either ```Customer will subscribe!``` or ```Customer will not subscribe!``` 

The input format will be just like it was in the dataset. The only difference is 5 variables are removed as they seemed unncessary features: 
```
default, month, day, poutcome, pdays
```

For better understanding, a picture of input format is provided here. 

<img src=https://github.com/asif-mahmud-am/bank-loan-approval-with-ML/assets/65419625/854414b9-789f-427d-8502-6ce72d781477 width=800>
