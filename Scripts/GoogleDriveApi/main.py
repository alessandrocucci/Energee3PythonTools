"""
Google Drive API parser

In questo script, andiamo a leggere un file csv da Google Drive e lo parsiamo in un dizionario Python
cosi' formato d = {(riga, colonna): valore, ...}.

Prerequisiti:

	- Scaricare google-api-python-client alla versione 1.3.2 usando il seguente comando:
		sudo pip install -I google-api-python-client==1.3.2
	- Scaricare la libreria pydrive
	- Vai alla pagina di Google APIs Console and crea un nuovo progetto.
	- Nel menu API, attiva Drive API.
	- In API Access, crea un OAuth2.0 client ID.

		'Application type' deve essere una Web application.
		Inserisci http://localhost:8080/ in 'Redirect URIs' e http://localhost:8080 in 'JavaScript origins'.

	- Scarica il json cliccando a destra nel menu delle chiavi id, rinominalo in client_secrets.json e
	incollalo nel working path di questo file python.

Usage:
::
	python main.py -f "file.csv"
"""

import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

__author__ = 'alessandro.cucci@energee3.com'


def main(file):
	# Autentichiamoci
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()
	drive = GoogleDrive(gauth)

	# Prendiamo la lista dei file in Google Drive
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for file1 in file_list:
		# se troviamo il nostro file
		if file1['title'] == file:
			output = drive.CreateFile({'id': file1['id']})
			# lo scarichiamo
			output.GetContentFile('output.csv')
			# e lo parsiamo
			d = {}
			with open(file) as f:
				for x, line in enumerate(f):
					for y, value in enumerate(line):
						d[(x, y)] = value
			print d


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('--file', '-f', help='Nome del file da parsare')

	args = parser.parse_args()
	if args.file:
		main(args.file)
	else:
		print "Devi dirmi il nome del file (es 'output.csv')"
