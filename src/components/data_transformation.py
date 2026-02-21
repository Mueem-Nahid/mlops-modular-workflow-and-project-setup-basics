import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts/data_transformation', 'preprocessor.pkl')
    feature_store_repo_path = "feature_repo"

