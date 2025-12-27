function LoadingStatus({theme}) {
    return <div className = "loading-container">
        <h2>Generating your {theme} story</h2>
        <div className="loading-animation">
            <div className="spinner"></div>
        </div>
        <p className="loading-info">
            This may take a few moments, we are generating an exciting adventure for you!
        </p>
    </div>
}

export default LoadingStatus;
