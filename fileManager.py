
import os 
import shutil


def sign_in():
    global user_input
    user_input = input('Login: ')
    if not os.path.isdir(user_input):
        os.mkdir(user_input)
    os.chdir(user_input)
            
def create_folder(foldername,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.mkdir(foldername)

def remove_folder(foldername, inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.rmdir(foldername)
  
def read_file(filename, inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    with open(filename,'r',encoding='utf-8') as f:
        print(f.read())
        
def create_file(filename,text=False):
    with open(filename,'w',encoding='utf-8') as f:
        if text:
            f.write(text)

def remove_file(filename,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.remove(filename)            

def unpack_archive_item(dir):
    shutil.unpack_archive(dir,'zip')
sign_in()
create_file('lox','rwerwerwerwerwe')    
    
def rename_file(curr_name,new_name,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.rename(curr_name,new_name)

def move_file(curr_dir,new_dir):
    shutil.move(curr_dir,new_dir)

def copy_text_file(filename,foldername,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    shutil.copy(filename,foldername)

def archive_item(dir):
    shutil.make_archive(dir,'zip')

def change_dir(dirname):
    os.chdir(dirname)    
    
