# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

    for filename in os.listdir("upload_folder"):
        dst = f"upload_folder/{filename}"
        os.rmdir(dst)
        



# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
