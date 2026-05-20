from typing import Any, TypeAlias
from abc import ABC, abstractmethod

NumericData: TypeAlias = int | float | list[int | float]
TextData: TypeAlias = str | list[str]
LogEntry: TypeAlias = dict[str, str]
LogData: TypeAlias = LogEntry | list[LogEntry]
StoredItem: TypeAlias = tuple[int, str]


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[StoredItem] = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> StoredItem:
        return self._data.pop(0)
    
    def _store(self, value: str) -> None:
        self._data.append((self._rank, value))
        self._rank += 1

    def get_total_processed(self) -> int:
        return self._rank
    
    def get_remaining_count(self) -> int:
        return len(self._data)

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False    

    def ingest(self, data: NumericData) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False
    
    def ingest(self, data: TextData) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        
        if isinstance(data, list):
            for item in data:
                self._store(item)

        else:
            self._store(data)
    
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                isinstance(data.get("log_level"), str)
                and isinstance(data.get("log_message"), str)
            )

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not isinstance(item.get("log_level"), str):
                    return False
                if not isinstance(item.get("log_message"), str):
                    return False
            return True

        return False

    def ingest(self, data: LogData) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        
        if isinstance(data, list):
            for item in data:
                self._store(
                    f"{item['log_level']}: {item['log_message']}"
                )
        else:
            self._store(
                f"{data['log_level']}: {data['log_message']}"
            )

class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False

            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def _processor_name(self, processor: DataProcessor) -> str:
        name = processor.__class__.__name__
        return name.replace("Processor", " Processor")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{self._processor_name(processor)}: "
                f"total {processor.get_total_processed()} items processed, "
                f"remaining {processor.get_remaining_count()} on processor"
            )

if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    data_stream.register_processor(NumericProcessor())

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {stream}\n")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    print("Send the same batch again")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    # 登録順: Numeric, Text, Log
    numeric = data_stream._processors[0]
    text = data_stream._processors[1]
    log = data_stream._processors[2]

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    data_stream.print_processors_stats()
