# CS4485-Team67-Trendata

The main python file is `connect-mdb.py`

# Setting up Credentials

Add your mariadb credentials to the following:

1. Go to `config` folder
2. Add file `credentials.py`
3. Add the following code to the file replacing `username`, `password`, and `hostname`
   ```
    from config.credlib import credential
    user = credential("hostname", "username", "password")
   ```

This file is included within .gitignore and will not be uploaded to the repo
