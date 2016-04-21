import sqlite3
import pyperclip
import sys
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sqlite_file = os.path.join(BASE_DIR, 'app/db.sqlite3') 

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


####
#  Create the required Table
####

table_name = 'credentials'

# account_col = 'account' 
# account_type = 'TEXT'
# user = 'username' 
# user_type = 'TEXT'
# passw = 'password' 
# pass_type = 'TEXT'

# c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY,{nf2} {ft2}, {nf3} {ft3})'\
#         .format(tn=table_name, nf=account_col, ft=account_type, nf2=user, ft2=user_type, nf3=passw, ft3=pass_type))

# account = 'test1'


# sys.exit()



##########################################





# CRED = {
# 	"buyold" : {
# 		"user" : "sadmin",
# 		"pass" : "admin123"
# 	},
# 	"vaxia" : {
# 		"user" : "admin",
# 		"pass" : "0aKdoxkkY0"
# 	}
# }
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



	# sys.exit()
	# if account in CRED:
	# 	acc = CRED.get(account,'NO Account')
	# 	c.execute("SELECT * FROM {tn} WHERE account = {account} "\
 #        .format(tn=table_name, account=account))
	# 	# pyperclip.copy(acc.get('pass',''))
	# else:
	# 	print 'No Account named %s' % account





##########################################################



conn.commit()
conn.close()
