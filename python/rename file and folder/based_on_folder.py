# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

    
        

	
    for i in os.listdir("upload_folder"):
        d="upload_folder/"+i
        for count, filename in enumerate(os.listdir(d)):
            
            dst = f"{i}_{filename}.jpg"
            src =f"upload_folder/{i}/{filename}" # foldername/filename, if .py file is outside folder
            dst =f"renamed_images/{dst}"
            
            # rename() function will
            # rename all the files
            try:
                os.rename(src, dst)
            except:
                os.replace(src, dst)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
