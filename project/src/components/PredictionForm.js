import React, { useState } from 'react';
import axios from 'axios';

function PredictionForm() {
    const [file, setFile] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [isPredicting, setIsPredicting] = useState(false);

    const handleChange = (event) => {
        setFile(event.target.files[0]);
    };

    console.log(file)

  

    const handleSubmit = async (event) => {
        event.preventDefault();

        setIsPredicting(true);
        setPrediction(null);

        let formData = new FormData();
        let text ="dfdfddgdg"
        formData.append('file', file );
        console.log(formData.get("file"))

        try {
            const response = await axios.post('http://localhost:8001/predict/',formData,{
                
                headers: {
                    'Content-Type': 'multipart/formdata'
                }
            });
            console.log(response)
            setPrediction(response.data.predicted_class);
        } catch (error) {
            console.error('Error predicting:', error);
        } finally {
            setIsPredicting(false);
        }
    };

    return (
        <div>
            <h1>Liver Disease Detection</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleChange} />
                <button type="submit">Predict</button>
            </form>
            {isPredicting && <p>Predicting...</p>}
{prediction && <p>Predicted Class: {prediction}</p>}
        </div>
    );
}

export default PredictionForm;