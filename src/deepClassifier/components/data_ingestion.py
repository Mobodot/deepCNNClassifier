import os
from zipfile import ZipFile
from typing import List
import urllib.request as request
from deepClassifier.entity.config_entity import DataIngestionConfig
from deepClassifier import logger
from tqdm import tqdm
from deepClassifier.utils import get_size
from deepClassifier.config import ConfigurationManager


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> None:
        logger.info(f"Trying to download data from: {self.config.source_url}")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info: \n {headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(self.config.local_data_file)}"
            )

    def _get_updated_list_of_files(self, list_of_files) -> List:
        return [f for f in list_of_files if f.endswith(".jpg")]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)

    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            logger.info("Preprocessing files...")
            updated_list_of_files = self._get_updated_list_of_files(
                list_of_files=list_of_files
            )
            logger.info("Extracting and unzipping files...")
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzipped_dir)
