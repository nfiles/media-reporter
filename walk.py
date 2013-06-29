import os
import json



if __name__ == '__main__':
	var Movies = []
	var TvShows = []
	for root, dirs, files in os.walk(os.getcwd()):
		print("Current directory", root)
		print("Sub directories", dirs)
		print("Files", files)
