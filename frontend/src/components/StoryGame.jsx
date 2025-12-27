import {useState, useMemo} from 'react';

function StoryGame({story, onNewStory}) {
    const [currentNodeId, setCurrentNodeId] = useState(story?.root_node?.id || null);

    const currentNode = useMemo(() => {
        if (!currentNodeId || !story || !story.all_nodes) return null;
        return story.all_nodes[currentNodeId];
    }, [currentNodeId, story]);

    const isEnding = currentNode ? currentNode.is_ending : false;
    const isWinningEnding = currentNode ? currentNode.is_winning_endig : false;

    const options = useMemo(() => {
        if (!currentNode || currentNode.is_ending || !currentNode.options || currentNode.options.length === 0) {
            return [];
        }
        return currentNode.options;
    }, [currentNode]);

    const chooseOption = (optionId) => {
        setCurrentNodeId(optionId);
    };

    const restartStory = () => {
        if (story && story.root_node) {
            setCurrentNodeId(story.root_node.id);
        }
    };

    return <div className="story-game">
        <header className="story-header">
            <h2>{story?.title || ''}</h2>
        </header>

        <div className="story-content">
            {currentNode && <div className="story-node">
                <p>{currentNode.content}</p>

                {isEnding ?
                    <div className="story-ending">
                        <h3>{isWinningEnding ? "Congratulations" : "The End"}</h3>
                        <p>{isWinningEnding ? "You reached a winning ending" : "Your adventure has ended."}</p>
                    </div>
                    :
                    <div className="story-options">
                        <h3>What will you do?</h3>
                        <div className="options-list">
                            {options.map((option, index) => (
                                <button
                                    key={index}
                                    onClick={() => chooseOption(option.node_id)}
                                    className="option-btn"
                                >
                                    {option.text}
                                </button>
                            ))}
                        </div>
                    </div>
                }
            </div>}

            <div className="story-controls">
                <button onClick={restartStory} className="reset-btn">
                    Restart Story
                </button>
            </div>
        <div className="story-controls">
            {onNewStory && <button onClick={onNewStory} className="new-story-btn">
                New Story
            </button>}
         </div>
        </div>
    </div>
}

export default StoryGame
