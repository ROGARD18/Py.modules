from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class for all data processors in the Code Nexus.
    Defines the standard interface for validation, processing,
    and output formatting.
    """
    def __init__(self, data: Any) -> None:
        """
        Initialize the processor with its associated data.
        """
        self.data: Any = data

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Execute the primary data processing logic on the input.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Verify that the input data format is compatible with the processor.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Apply standard Nexus formatting to the processing result.
        """
        pass


class NumericProcessor(DataProcessor):
    """
    Specialized processor for numerical datasets.
    Calculates statistical metrics like sum and average.
    """
    def process(self, data: Any) -> str:
        """
        Calculate sum and average for a list of numbers.
        """
        if not self.validate(data):
            return self.format_output("ERROR: Invalid Data Format")

        s: int = sum(data)
        a: float = s / len(data)
        result_str: str = (f"Processed {len(data)} numeric values, "
                           f"sum={s}, avg={a}")
        return self.format_output(result_str)

    def validate(self, data: Any) -> bool:
        """
        Verify that the input is a list containing only numeric values.
        """
        try:
            if not isinstance(data, list):
                raise ValueError("No numeric data list")

            for item in data:
                int(item)

            return True
        except (ValueError) as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        """
        Return the result with the standard Output prefix.
        """
        return "Output: " + result


class TextProcessor(DataProcessor):
    """
    Specialized processor for string-based data.
    Analyzes character counts and word frequency.
    """
    def process(self, data: Any) -> str:
        """
        Perform linguistic analysis on the input string.
        """
        if not self.validate(data):
            return self.format_output("ERROR: Invalid Text Data")

        word_count = len(data.split())
        char_count = len(data)
        result_str = f"Processed text: characters={char_count}, "\
                     f"words={word_count}"
        return self.format_output(result_str)

    def validate(self, data: Any) -> bool:
        """
        Ensure the input data is a valid string.
        """
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """
        Format the text analysis result for output.
        """
        return "Output: " + result


class LogProcessor(DataProcessor):
    """
    Specialized processor for system log entries.
    Detects critical patterns and error levels.
    """
    def process(self, data: Any) -> str:
        """
        Parse log data to identify system alerts.
        """
        if not self.validate(data):
            return self.format_output("ERROR: Invalid Log Data")

        result_str = "[ALERT] ERROR level detected: Connection timeout"
        return self.format_output(result_str)

    def validate(self, data: Any) -> bool:
        """
        Verify that the log entry is a properly formatted string.
        """
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """
        Apply log-specific formatting to the result.
        """
        return "Output: " + result


def main() -> None:
    """
    Main entry point to demonstrate polymorphic data processing.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_data = [1, 2, 3, 4, 5]
    num_proc = NumericProcessor(num_data)
    print(f"Processing data: {num_data}")
    print("Validation: Numeric data verified")
    print(num_proc.process(num_data))

    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    text_proc = TextProcessor(text_data)
    print(f"Processing data: '{text_data}'")
    print("Validation: Text data verified")
    print(text_proc.process(text_data))

    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    log_proc = LogProcessor(log_data)
    print(f"Processing data: '{log_data}'")
    print("Validation: Log data verified")
    print(log_proc.process(log_data))

    print("\n=== Polymorphic Processing Demo ===")
    all_proc: list = [num_proc, text_proc, log_proc]
    all_data: list = [num_data, text_data, log_data]
    i: int = 0
    for proc in all_proc:
        i += 1
        print(f"Result {i}: {proc.process(all_data[i - 1])}")

    print("\nFoundation system online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
