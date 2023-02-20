# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

    for count, filename in enumerate(os.listdir("upload_folder")):
        dst1 = f"SKU{str(count)}"
        src1 =f"upload_folder/{filename}" # foldername/filename, if .py file is outside folder
        dst1 =f"upload_folder/{dst1}"
        os.rename(src1, dst1)
        

	
    for i in os.listdir("upload_folder"):
        d="upload_folder/"+i
        for count, filename in enumerate(os.listdir(d)):
            
            dst = f"{i}_{str(count)}.jpg"
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
