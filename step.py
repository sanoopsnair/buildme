#!/usr/bin/python
import sys
import os
import yaml   #sudo pip install PyYAML
import ast

params = str(sys.argv)
params = ast.literal_eval(params)


def readConfig():
	with open('config.yaml', 'r') as f:
		doc = yaml.load(f)
	return doc


def buildProject(configDatas=None, baseFolder=None, path=None):
	if path:
		destinPath = path+"/"+baseFolder
	else:
		destinPath = "yard/"+baseFolder

	os.system('mkdir '+destinPath)

	if configDatas:
		for data in configDatas:
			if data['content']['type'] == 'file':
				os.system('touch '+destinPath+data['content']['path'])
				os.system('echo "'+data['content']['data']+'">>'+destinPath+data['content']['path'])
			elif data['content']['type'] == 'folder':
				os.system('mkdir '+destinPath+data['content']['path'])
			else:
				pass


if len(params) > 1:
	configDatas = readConfig()
	if len(params) >= 3:
		path = params[2]
	else:
		path = None

	buildProject(configDatas[params[1]], params[1], path)
else:
	configDatas = readConfig()
	keysOfConfig = configDatas.keys()
	print "\n".join(keysOfConfig)


