from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Store chat history
chat_history_ids = None

def ask_question(query):
    global chat_history_ids
    try:
        # Encode user input
        new_input_ids = tokenizer.encode(query + tokenizer.eos_token, return_tensors='pt')

        # Append chat history
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

        # Generate response
        chat_history_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=100,
            top_p=0.7,
            temperature=0.8
        )

        # Decode and return
        response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

    except Exception as e:
        return f"Error: {e}"
