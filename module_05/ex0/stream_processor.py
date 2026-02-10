from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self, data: Any):
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("ERROR: Invalid Data Format")

        s = sum(data)
        a = s / len(data)
        result_str = f"Processed {len(data)} numeric values, sum={s}, avg={a}"
        return self.format_output(result_str)

    def validate(self, data: Any) -> bool:
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
        return "Output: " + result


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("ERROR: Invalid Text Data")

        word_count = len(data.split())
        char_count = len(data)
        result_str = f"Processed text: characters={char_count}"\
                     f"words={word_count}"
        return self.format_output(result_str)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return "Output: " + result


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("ERROR: Invalid Log Data")

        result_str = "[ALERT] ERROR level detected: Connection timeout"
        return self.format_output(result_str)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return "Output: " + result


def main() -> None:
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
