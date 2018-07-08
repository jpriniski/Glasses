import pandas as pd
import os

def main():
	img_dir = 'Selfie-dataset/images'
	cla_dir = 'Selfie-dataset/selfie_dataset.txt'

	#I copied in the column titles into the selfie_dataset.txt file for ease of reading in the data
	
	os.makedirs('Selfie-dataset/images/glasses', exist_ok=True)
	os.makedirs('Selfie-dataset/images/no_glasses', exist_ok=True)

	classes = pd.read_table(cla_dir, sep = ' ')
	classes_ = classes
	for index, row in classes_.iterrows():
		file_name = row['image_name']
		old_dir = "Selfie-dataset/images/"+ str(file_name) + ".jpg"
		glasses = row['wearing_glasses']
		if glasses is -1:
			new_dir = "Selfie-dataset/images/no_glasses/"+ str(file_name) + ".jpg"
		if glasses is 1:
			new_dir = "Selfie-dataset/images/glasses/"+ str(file_name) + ".jpg"
	
		os.rename(old_dir,new_dir)
	

main()
