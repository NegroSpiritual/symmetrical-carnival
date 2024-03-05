import React, { useState } from 'react';
import axios from 'axios';

function PredictionForm() {
    const [file, setFile] = useState(null);
    const [prediction, setPrediction] = useState(null);

    const handleChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8001/predict/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setPrediction(response.data.predicted_class);
        } catch (error) {
            console.error('Error predicting:', error);
        }
    };

    return (
        <div>
            <h1>Simple Image Classifier</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleChange} />
                <button type="submit">Predict</button>
            </form>
            {prediction && <p>Predicted Class: {prediction}</p>}
        </div>
    );
}

export default PredictionForm;
