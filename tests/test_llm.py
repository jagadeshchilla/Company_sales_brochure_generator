from brochure.llm import generate_response

if __name__ == "__main__":
    # Example usage
    prompt = "What is the capital of France?"
    response = generate_response(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")