# pip python3 -m venv promptify-env
# source promptify-env/bin/activate
# pip install -r requirements.txt

from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# Load the T5 model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large") 
prompt_enhancement = "Please take the following input and enhance it by adding relevant details, context, and elaboration to make it suitable for a large language model. Ensure that the expanded prompt provides clear instructions and sufficient context for generating a comprehensive and accurate response. Here is the input: "

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['inputs']
    
    # Prepare the input and generate the response
    inputs = tokenizer.encode(prompt_enhancement + user_input, return_tensors='pt')
    outputs = outputs = model.generate(
        inputs,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,  # Adjust as needed
        top_k=50,         # Adjust as needed
        top_p=0.95        # Adjust as needed
    )

    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({'generated_text': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
