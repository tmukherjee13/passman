import sqlite3
import pyperclip
import sys
import os


# If the system can't determine the path change to absolute path to your project directory.
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = '/var/www/pyapps/passman'


sqlite_file = os.path.abspath(os.path.join(BASE_DIR, 'app/db.sqlite3')) 

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

TABLE_NAME = 'vault'


##########################################################

####
#  Create the required columns.[only used when using just this cli and not the django app]
####

# account_col = 'account' 
# account_type = 'TEXT'
# user = 'username' 
# user_type = 'TEXT'
# passw = 'password' 
# pass_type = 'TEXT'

# c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY,{nf2} {ft2}, {nf3} {ft3})'\
#         .format(tn=TABLE_NAME, nf=account_col, ft=account_type, nf2=user, ft2=user_type, nf3=passw, ft3=pass_type))

##########################################

def get():

	if len(sys.argv) < 2:
		print '''Usage: getpass <account>
		'''
		sys.exit()
	account = sys.argv[1]

	c.execute("SELECT * FROM {tn} WHERE account = '{account}' "\
        .format(tn=TABLE_NAME, account=account))

	cred = c.fetchone()

	if cred:
	    pyperclip.copy(cred[2])
	    print 'Password copied to clipboard'
	else:
	    print('Account {} does not exist'.format(account))

	conn.commit()
	conn.close()



def set():

	if len(sys.argv) < 3:
		print '''Usage: setpass <account> <user>/<pass>
		'''
		sys.exit()

	account = sys.argv[1]
	user,passwd = sys.argv[2].split('/')
	try:
	    c.execute("INSERT OR IGNORE INTO {tn} ('account', 'username', 'password') VALUES ('{acc}','{usr}', '{ps}')".\
        	format(tn=TABLE_NAME, acc=account, usr=user, ps=passwd))
	except sqlite3.IntegrityError:
	    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(account))

	conn.commit()
	conn.close()