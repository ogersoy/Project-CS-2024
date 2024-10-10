import logging
from langchain.llms.base import LLM
from langchain.embeddings.base import Embeddings
from typing import Any, Dict, List, Optional
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
from huggingface_hub import login
from pydantic import Field

logger = logging.getLogger(__name__)

class HuggingFaceLLM(LLM):
    model_name: str = Field(..., description="Name of the Hugging Face model to use")
    hf_token: str = Field(..., description="Hugging Face API token")
    system_message: str = Field("", description="System message to prepend to all prompts")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        login(token=self.hf_token)

        self._tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self._model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self._max_length = self._model.config.max_position_embeddings

        # Set pad_token_id to eos_token_id if not set
        if self._tokenizer.pad_token_id is None:
            self._tokenizer.pad_token_id = self._tokenizer.eos_token_id

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
        logger.debug(f"Calling HuggingFaceLLM with prompt: {prompt[:50]}...")

        full_prompt = f"{self.system_message}\nHuman: {prompt}\nAI:"
        inputs = self._tokenizer(full_prompt, return_tensors="pt", padding=True, truncation=True, max_length=self._max_length)
        logger.debug(f"Input sequence length: {inputs['input_ids'].shape[1]}")

        # Calculate max_new_tokens, ensuring it's at least 1
        max_new_tokens = max(1, min(1000, self._max_length - inputs['input_ids'].shape[1]))
        logger.debug(f"max_new_tokens: {max_new_tokens}")

        with torch.no_grad():
            output_sequences = self._model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True,
                pad_token_id=self._tokenizer.pad_token_id,
            )

        response = self._tokenizer.decode(output_sequences[0], skip_special_tokens=True)
        logger.debug(f"Generated response: {response[:50]}...")

        # Extract only the AI's response
        ai_response = response.split("AI:")[-1].strip()
        if not ai_response:
            logger.warning("No 'AI:' found in the response. Returning full response.")
            return response.strip()
        return ai_response

    @property
    def _llm_type(self) -> str:
        return "Hugging Face LLM"

class HuggingFaceEmbeddings(Embeddings):
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    hf_token: Optional[str] = None

    def __init__(self, **kwargs):
        super().__init__()
        self.model_name = kwargs.get("model_name", self.model_name)
        self.hf_token = kwargs.get("hf_token", self.hf_token)
        
        if self.hf_token:
            login(token=self.hf_token)
        
        self._model = AutoModel.from_pretrained(self.model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        inputs = self._tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = self._model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]