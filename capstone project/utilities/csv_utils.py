import csv
from pathlib import Path
from typing import List, Dict, Tuple
from utilities.logger import CustomLogger

logger = CustomLogger.get_logger("CSVUtils")


class CSVUtils:
    """
    Utility class to read test data from CSV files.
    """
    @staticmethod
    def get_csv_as_dicts(file_name_or_path: str) -> List[Dict[str, str]]:
        """
        Reads CSV file and returns list of dictionaries where keys are column headers.
        """
        file_path = CSVUtils._resolve_path(file_name_or_path)
        data = []
        try:
            with open(file_path, mode="r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # Strip leading/trailing whitespaces from keys and values
                    cleaned_row = {k.strip(): v.strip() for k, v in row.items() if k is not None}
                    data.append(cleaned_row)
            logger.info(f"Loaded {len(data)} rows from CSV: {file_path.name}")
        except Exception as e:
            logger.error(f"Error reading CSV file at {file_path}: {str(e)}")
            raise
        return data

    @staticmethod
    def get_csv_as_tuples(file_name_or_path: str, columns: List[str] = None) -> List[Tuple]:
        """
        Reads CSV file and returns list of tuples matching the specified column order.
        Ideal for pytest.mark.parametrize.
        """
        dicts = CSVUtils.get_csv_as_dicts(file_name_or_path)
        if not dicts:
            return []

        if columns is None:
            columns = list(dicts[0].keys())

        result = []
        for row in dicts:
            row_tuple = tuple(row.get(col, "") for col in columns)
            result.append(row_tuple)
        return result

    @staticmethod
    def _resolve_path(file_name_or_path: str) -> Path:
        path = Path(file_name_or_path)
        if not path.is_absolute():
            base_dir = Path(__file__).resolve().parent.parent
            path = base_dir / "test_data" / file_name_or_path
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found at: {path}")
        return path
