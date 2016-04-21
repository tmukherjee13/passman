import pyperclip
import sys


CRED = {
	"buyold" : {
		"user" : "sadmin",
		"pass" : "admin123"
	},
	"vaxia" : {
		"user" : "admin",
		"pass" : "0aKdoxkkY0"
	}
}
if len(sys.argv) < 3:
	print '''Usage: python app.py set/get <account>
	'''
	sys.exit()
invoke = sys.argv[1]
account = sys.argv[2]
if invoke == 'set':
	user,passwd = sys.argv[3].split('/')
	CRED[account] = {}
	CRED[account]['user'] = user
	CRED[account]['pass'] = passwd
	print CRED.get(account)
else:
	if account in CRED:
		acc = CRED.get(account,'NO Account')
		pyperclip.copy(acc.get('pass',''))
	else:
		print 'No Account named %s' % account
