import os, glob

diretorio_usuario = 'c:/'
diretorio = 'ws/'

def listar(diretorio_usuario, diretorio):
	if os.path.isdir(diretorio_usuario + diretorio ):
		os.chdir(diretorio_usuario + diretorio)
		for arquivo in glob.glob("*"):
			if os.path.isdir(diretorio_usuario+diretorio+arquivo):
				listar(diretorio_usuario, diretorio+arquivo+'/')
			else:
				print('arquivo: '+diretorio_usuario+diretorio+arquivo)
	else:
		print('arquivo: '+diretorio_usuario+diretorio)


print(listar(diretorio_usuario, diretorio))