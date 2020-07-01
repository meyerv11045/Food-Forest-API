To use the Food Forest API to make updates to the database: 
1. Clone the repository to your local machine
2. Create a file named `config.ini` and enter your FF account login information like this:
```
[login]
email = johndoe@gmail.com
password = test123
```
The `config.ini` file will be used by `tokens.py` to get access tokens that will included in the API request headers so that the calls will work
