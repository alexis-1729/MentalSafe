from unsloth import FastLanguageModel
from dotenv import load_dotenv
import os
load_dotenv()


class ModelLLM:

    def __init__(self) -> None:
        self.model = None
        self.tokenizer = None

    def load_model(self):
       self.model, self.tokenizer = FastLanguageModel.from_pretrained(
        model_name = os.getenv("MODELO_BASE"),     
        adapter_name = os.getenv("RUTA_ADAPTER"),   
        max_seq_length = os.getenv("MAX_SEQ_LENGTH"),
        load_in_4bit = True,          
        dtype = None,                  
        )
       
       self.model = FastLanguageModel.for_inference(self.model)

    def inference(self, 
                  messages,
                  max_new_tokens=512,
                  temperature=0.7,
                  top_p=0.9):
        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True, 
            return_tensors="pt"
        ).to("cuda")

        outputs = self.model.generate(
        input_ids=inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,              
        pad_token_id=self.tokenizer.eos_token_id,
        eos_token_id=self.tokenizer.eos_token_id,
        use_cache=True,              
        )
        
        respuesta = self.tokenizer.decode(
            outputs[0][len(inputs[0]):], 
            skip_special_tokens=True
        ).strip()

        return respuesta
    
    
