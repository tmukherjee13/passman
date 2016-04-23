import sqlite3
import pyperclip
import sys
import os




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sqlite_file = os.path.abspath(os.path.join(BASE_DIR, 'app/db.sqlite3')) 

# If the system can't determine the path to DB uncomment the following line and provide the path to DB.
# sqlite_file = os.path.abspath('<ABSOLUTE_PATH_TO_DB.SQLITE3>')

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table_name = 'vault'


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
#         .format(tn=table_name, nf=account_col, ft=account_type, nf2=user, ft2=user_type, nf3=passw, ft3=pass_type))


##########################################


if len(sys.argv) < 3:
	print '''Usage: python app.py set/get <account>
	'''
	sys.exit()
invoke = sys.argv[1]
account = sys.argv[2]
if invoke == 'set':
	user,passwd = sys.argv[3].split('/')
	try:
	    c.execute("INSERT OR IGNORE INTO {tn} ('account', 'username', 'password') VALUES ('{acc}','{usr}', '{ps}')".\
        	format(tn=table_name, acc=account, usr=user, ps=passwd))
	except sqlite3.IntegrityError:
	    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

else:

	c.execute("SELECT * FROM {tn} WHERE account = '{account}' "\
        .format(tn=table_name, account=account))

	cred = c.fetchone()


	if cred:
	    # print('{}'.format(cred))
	    pyperclip.copy(cred[2])
	    print 'Password copied to clipboard'
	else:
	    print('Account {} does not exist'.format(account))

conn.commit()
conn.close()


def get():
	pass

def set():
	pass