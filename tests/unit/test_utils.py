import pytest
import os
from pathlib import Path
from box import ConfigBox
from deepClassifier.utils import read_yaml


yaml_files = [
    "configs/config.yaml",
    "configs/config.txt"
    
]


def test_read_yaml_return_type():
    response = read_yaml(Path(yaml_files[0]))
    assert isinstance(response, ConfigBox)
    
def test_read_yaml_extension():
    with pytest.raises(Exception):
        read_yaml(yaml_files[-1])
        
@pytest.mark.parametrize("path_to_yaml")
def test_read_yaml_empty_and_yaml_extension(path_to_yaml):
    pass