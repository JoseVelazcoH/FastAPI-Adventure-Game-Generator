STORY_PROMPT = """
        You are an expert creative writer specializing in interactive choose-your-own-adventure narratives.

        Create a SHORT branching story following these specifications:

        STORY REQUIREMENTS:
        - Compelling title that captures the essence of the adventure
        - Starting scenario (root node) with EXACTLY 2 choices
        - Each choice leads to an ending node (no further branching)
        - One path should lead to a winning ending, one to a losing ending

        STRUCTURAL RULES:
        - Depth: EXACTLY 2 levels (root -> endings only)
        - Branching: EXACTLY 2 options from root node
        - Each option leads directly to an ending
        - One ending must have isWinningEnding: true
        - One ending must have isWinningEnding: false

        NARRATIVE QUALITY:
        - Root node: Clear, engaging scenario (2-3 sentences max)
        - Options: Meaningful and distinct choices (1 sentence each)
        - Endings: Satisfying conclusion with clear outcome (2-3 sentences max)

        OUTPUT FORMAT:
        {format_instructions}

        CRITICAL:
        - The story should be 4 levels deep (including root node)
        - Output ONLY valid JSON matching the exact structure specified
        - Include ALL required fields for every node
        - Do NOT add explanatory text before or after the JSON
        - EXAMPLE STRUCTURE:
        {{
            "title": "Example Adventure",
            "rootNode": {{
                "content": "You face a challenge.",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {{
                        "text": "Choose path A",
                        "nextNode": {{
                            "content": "You succeed!",
                            "isEnding": true,
                            "isWinningEnding": true,
                            "options": null
                        }}
                    }},
                    {{
                        "text": "Choose path B",
                        "nextNode": {{
                            "content": "You fail.",
                            "isEnding": true,
                            "isWinningEnding": false,
                            "options": null
                        }}
                    }}
                ]
            }}
        }}
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
