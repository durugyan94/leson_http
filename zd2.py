from urllib import response
import requests
from pathlib import Path


TOKEN = ''

class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk'
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        files_metod = self.url + '/resources/files'
        response = requests.get(files_metod, headers=self.headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        """Метод получает ссылку на загрузку"""
        upload_url = self.url + '/resources/upload'
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=self.headers, params=params).json()
        href = response.get('href', False)
        if href:
            return href
        else:
            raise RuntimeError(f'Ошибка получения ссылки на загрузку {response}')

    def upload(self, local_files_path, disk_file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = self._get_upload_link(disk_file_path)
        with open(local_files_path, 'rb') as f:
            response = requests.put(upload_url, data=f)
            response.raise_for_status()
            if response.status_code == 201:
                print('Успешно!')



if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    local_files_path = Path('C:/Users/HOME/Desktop/Untitled-1.py')
    disk_file_path = local_files_path.name

    ya.upload(local_files_path, disk_file_path)
