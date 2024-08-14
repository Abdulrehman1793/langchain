"""Interface for selecting examples to include in prompts."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from langchain_core.runnables import run_in_executor


class BaseExampleSelector(ABC):
    """Interface for selecting examples to include in prompts."""

    @abstractmethod
    def add_example(self, example: Dict[str, Any]) -> Any:
        """Add new example to store.

        Args:
            example: A dict that maps input and output variables to their example
                values.
        """

    async def aadd_example(self, example: Dict[str, Any]) -> Any:
        """Async add new example to store.

        Args:
            example: A dict that maps input and output variables to their example
                values.
        """

        return await run_in_executor(None, self.add_example, example)

    @abstractmethod
    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
        """Select which examples to use based on the inputs.

        Args:
            input_variables: A that maps input variables to their values.
        """

    async def aselect_examples(self, input_variables: Dict[str, str]) -> List[dict]:
        """Async select which examples to use based on the inputs.

        Args:
            input_variables: A that maps input variables to their values.
        """

        return await run_in_executor(None, self.select_examples, input_variables)
