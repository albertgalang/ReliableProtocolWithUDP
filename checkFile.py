def checkFile(filename):
	err = False
	while (err == False):
		try:
			inputFile = open(filename, "r")
		except IOError:
			print("File", filename, "does not exist! Run client.py again while server.py is still listening to try again!")
			break
		else:
			print(filename, "will now be tranfered reliably!")
			err = True

			inputFile.close()
			break
		

	return err
