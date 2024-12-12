import os

HOME = os.getcwd()
# print('HOME', HOME)

DATASET_PATH = os.path.join(HOME, 'raw_animes_dataset')
# print('DATASET FOLDER', DATASET_PATH)

ANIME_DATASET_2023 = os.path.join(DATASET_PATH, 'anime-dataset-2023.csv')
# print('ANIME DATASET 2023', ANIME_DATASET_2023)

DATA_PREPROCESSING = os.path.join(HOME, 'Data Preprocessing')
# print('DATA PREPROCESSING', DATA_PREPROCESSING)