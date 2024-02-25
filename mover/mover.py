import os
import shutil
import datetime
from typing import Optional
from .constants import Constant


def get_file_info(s_file_path: str, t_type='m') -> Optional[datetime.date]:
    match t_type:
        case 'm':
            modified_date = os.path.getmtime(s_file_path)
            return datetime.date.fromtimestamp(modified_date)
        case 'a':
            modified_date = os.path.getatime(s_file_path)
            return datetime.date.fromtimestamp(modified_date)
        case 'c':
            modified_date = os.path.getctime(s_file_path)
            return datetime.date.fromtimestamp(modified_date)
        case _:
            return None

class FileMover:
    def __init__(self):
        self.constant = Constant()

    def is_dir_not_exists_create(self, stored_folder):
        if stored_folder is not None:
            check_folder_path = os.path.join(self.constant.processed_dir, stored_folder)
            if not os.path.exists(check_folder_path):
                try:
                    os.mkdir(check_folder_path)
                    return True
                except Exception as ex:
                    return False
            return True

    def file_move(self, moving_folder, file_name, success=True):
        def get_destination_path(success):
            if success:
                return os.path.join(self.constant.processed_dir, moving_folder)
            else:
                return os.path.join(self.constant.failed_dir, moving_folder)
        d_final_file_path = get_destination_path(success)
        s_final_file_path = os.path.join(self.constant.processing_dir, file_name)
        shutil.move(s_final_file_path, d_final_file_path)



    def moving(self):
        print(len(os.listdir(self.constant.processing_dir)))
        for file_name in os.listdir(self.constant.processing_dir):
            s_file_path = os.path.join(self.constant.processing_dir, file_name)
            folder_exists = get_file_info(s_file_path, t_type='m')
            if folder_exists is not None:
                is_created = self.is_dir_not_exists_create(str(folder_exists))
                if is_created:
                    self.file_move(str(folder_exists), file_name,success=True)



