STORY_PROMPT = """
You are a creative writer. Generate a choose-your-own-adventure story in the specified JSON format.

Constraints:
- Max 7 nodes total; max 3 levels deep (including root node).
- Each node content: 1-3 sentences.
- Non-ending nodes: exactly 2 options.
- Ending nodes: 0 options.
- Every option must have non-empty "text" and a valid "nextNode" identifier.
- Set "isEnding" and "isWinningEnding" booleans on every node.
- Include at least one winning ending and at least one losing ending.

Output:
- Follow this exact JSON structure: {format_instructions}
- Return ONLY the raw JSON object. No markdown, no intro/outro, no commentary.
"""

json_structure = """
        {
            "title": "Story Title",
            "rootNode": {
                "content": "The starting situation of the story",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Option 1 text",
                        "nextNode": {
                            "content": "What happens for option 1",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    // More options for root node
                ]
            }
        }
        """