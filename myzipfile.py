import zipfile

flag = 0

tab = 'asdf'
 
def zipbp(zip_file,passwd):
	try:
		zip_file.extractall(pwd = passwd)
		print("[*] success! password is %s"%passwd)
		global flag
		flag = 1
	except:
		print('Sorry, %s failed'%passwd)
 


# for i in zip_file.infolist():
#     print i.file_size, i.header_offset 
'''
	for i in tab:
        for j in tab:
            for k in tab:
                for l in tab:           
		            passwd = i+j+k+l
                    print(passwd)
		            zipbp(zip_file,passwd)
		            if flag == 1:
			            break
''' 
zip_file = zipfile.ZipFile('password.zip')

for i in tab:
    for j in tab:
        for k in tab:
            for l in tab:
                passwd = i+j+k+l
           
                zipbp(zip_file,passwd)
                print(flag)
                if flag == 1:
                    break
#if __name__ == '__main__':
#	main()
