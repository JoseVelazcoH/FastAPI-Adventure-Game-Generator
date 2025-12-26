STORY_PROMPT = """
        You are an expert creative writer specializing in interactive choose-your-own-adventure narratives.

        Create a complete branching story following these specifications:

        STORY REQUIREMENTS:
        - Compelling title that captures the essence of the adventure
        - Starting scenario (root node) with 2-3 meaningful choices
        - Each choice branches to new scenarios with their own options
        - Multiple endings: both successful outcomes and failures
        - Minimum one winning path with satisfying resolution

        STRUCTURAL RULES:
        - Depth: 3-4 levels from root to endings
        - Branching: 2-3 options per non-ending node
        - Variety: Mix of short paths (quick endings) and long paths (extended narratives)
        - Balance: Equal distribution between winning and losing outcomes

        NARRATIVE QUALITY:
        - Each node presents a clear, engaging scenario
        - Options should feel meaningful and distinct
        - Consequences should flow logically from choices
        - Endings should provide closure and emotional payoff

        OUTPUT FORMAT:
        {format_instructions}

        CRITICAL:
        - Output ONLY valid JSON matching the exact structure specified
        - Include ALL required fields for every node
        - Do NOT add explanatory text before or after the JSON
        - Do NOT simplify or omit any story branches
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
