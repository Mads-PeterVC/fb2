from importlib.resources import files
from pathlib import Path

def get_data_path() -> Path:
    """
    Returns the path to the data directory within the fb2 package.
    
    This function uses importlib.resources to locate the 'data' directory
    inside the fb2 package, ensuring compatibility with both local and
    installed versions of the package.
    
    Returns:
        Path: The path to the data directory.
    """
    return Path(files("fb2.data"))

def get_mm_dataset_path() -> Path:
    """
    Returns the path to the mm_dataset directory within the fb2.data package.
    
    This function uses importlib.resources to locate the 'mm_dataset' directory
    inside the fb2.data package, ensuring compatibility with both local and
    installed versions of the package.
    
    Returns:
    """
    path = get_data_path() / "mm_dataset.txt"
    return path

if __name__ == "__main__":
    # Example usage
    data_path = get_data_path()
    print(f"Data path: {data_path}")
    # You can now use data_path to access files in the fb2.data package

    mm_dataset_path = get_mm_dataset_path()
    print(f"MM Dataset path: {mm_dataset_path}")
    # You can now use mm_dataset_path to access the mm_dataset.txt file