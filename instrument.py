import os
import subprocess

#OUTPUT_FOLDER = 'ella-out/'
#OUTPUT_FOLDER = '/media/nas162/instrument/ella-out_134/'
#OUTPUT_FOLDER = '/media/nas162/instrument/ella-out_155_69_147_248/'
OUTPUT_FOLDER = '/mnt/nas162/instrument/ella-out_155_69_145_180_appsapk/'

#INPUT_FOLDER = 'apks'
#INPUT_FOLDER = '/media/nas162/instrument/apks_155_69_151_134/'
#INPUT_FOLDER = '/media/nas162/instrument/apks_gp_low/'
INPUT_FOLDER = '/mnt/nas162/instrument/apks_appsapk/'
OUTPUT_FILE = 'ella-out/already.txt'

def instrument(apk_path):
	#print apk_path
	subprocess.call(['./ella.sh', 'i', apk_path])

def main():
	processed = []
	#for f in os.listdir(OUTPUT_FOLDER):
	#	f = f.replace('_data_android_ella_apks_', '')
	#	f = f.replace('/', '')
		#print f
	#	processed.append(f)
	#for f in open(OUTPUT_FILE):
	#	f = f.replace('_data_android_ella_apks_', '')
	#	f = f.replace('/', '')
	#	processed.append(f.strip())

	for f in os.listdir(INPUT_FOLDER):
		if not f in processed:
			instrument(os.path.join(INPUT_FOLDER, f))

if __name__ == '__main__':
	main()
