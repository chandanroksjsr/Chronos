# Database Config

config = {
	'MYSQL_DATABASE_USER' : 'username', #Username for mysql
	'MYSQL_DATABASE_DB' : 'chronos',
	'MYSQL_DATABASE_PASSWORD' : 'password', # Password to connect to mysql
	'MYSQL_DATABASE_HOST' : 'chronos.cj9dhuqpwklh.us-west-2.rds.amazonaws.com', 
	'USERNAME' : '',
	'USERID' :'',
}

# To run the mail server run
# sudo python -m smtpd -n -c DebuggingServer localhost:25
# mail server settings

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# Administrator list
ADMINS = ['you@example.com']
