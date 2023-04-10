import os
import shutil 

def make_dir(path: str):
    """
    Create a new directory by 
    path must be there year and doy
    """
    try:
        os.mkdir(path)
    except OSError:
        print(f"Creation of the directory {path} failed")
    
    return path

def get_receivers_names(infile):
    folders = os.listdir(infile)
    
    out = []
    
    for folder in folders:
        
        day = os.path.join(infile, folder)
        
        for filename in os.listdir(day):
            out.append(filename)
    
    return list(dict.fromkeys(out))


def create_folder_from_receivers(
        receivers, 
        path_to_save):
    
    for rec in receivers:
        name = rec.replace(".txt", "")
        
        make_dir(os.path.join(path_to_save, name))



def copy_files_and_change_names(folders):
    
    for folder in folders:
        
        day = os.path.join(infile, folder)
        
        for filename in os.listdir(day):
            folder_rec = filename.replace(".txt", "")
            filename_to_save = os.path.split(day)[1]
            
            src = os.path.join(day, filename)
            dst = os.path.join(path_to_save, 
                               folder_rec, 
                               filename_to_save + ".txt")
            print("coping...", filename_to_save)
            shutil.copy(src, dst)

infile = "D:\\database\\tec\\2013\\"

receivers = get_receivers_names(infile)
path_to_save = "D:\\database\\tec\\2013.1\\"

create_folder_from_receivers(
        receivers, 
        path_to_save)

folders = os.listdir(infile)


copy_files_and_change_names(folders)