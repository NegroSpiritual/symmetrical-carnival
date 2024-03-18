import React, { useState } from 'react';
import axios from 'axios';

function PredictionForm() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (event) => {
        const selectedFile = event.target.files[0];
        setFile(selectedFile);

        if (selectedFile) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setPreview(reader.result);
            };
            reader.readAsDataURL(selectedFile);
        } else {
            setPreview(null);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://127.0.0.1:8000/predict/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            if (response.data && response.data.predicted_class) {
                setPrediction(response.data.predicted_class);
            } else {
                setPrediction('Unknown');
            }
        } catch (error) {
            console.error('Error predicting:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="form-container">
            <h1>Liver Disease Classifier</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleChange} />
                {preview && <img src={preview} alt="Preview" style={{ maxWidth: '100%', maxHeight: '200px', margin: '10px 0' }} />}
                <button type="submit">Predict</button>
            </form>
            {loading && <p>Loading...</p>}
            {prediction && !loading && <p>Predicted Class: {prediction}</p>}
        </div>
    );
}

export default PredictionForm;
