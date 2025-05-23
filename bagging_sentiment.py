def bagged_sentiment_classify(text, api_key, model_variants):
    predictions = []

    for model_name, prompt_style in model_variants:
        try:
            result = query_llm_sentiment(text, api_key, model_name, prompt_style)
            predictions.append(result)
        except Exception as e:
            print(f"Model {model_name} failed: {e}")

    if not predictions:
        raise Exception("All model calls failed.")

    # Majority vote
    vote = Counter(predictions)
    return vote.most_common(1)[0][0]

