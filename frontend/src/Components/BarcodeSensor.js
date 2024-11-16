import React, { useEffect, useRef, useState } from 'react';
import { BrowserMultiFormatReader } from '@zxing/browser';
import Actions from './Actions';

const BarcodeSensor = () => {
    const videoRef = useRef(null);
    const [barcode, setBarcode] = useState('');

    useEffect(() => {
        const codeReader = new BrowserMultiFormatReader();
        
        // Start the camera and attach it to the video element
        codeReader
        .decodeFromVideoDevice(null, videoRef.current, (result, error) => {
            if (result) {
                console.log(result);
                setBarcode(result.getText());
            } else {
                console.log("Nothing");
            }
        })
        .catch(err => console.error('Camera access error:', err));

        return () => {
        // Stop the camera when component unmounts
            //codeReader.reset();
        };
    }, []);

    return (
        <div>
            {barcode ? <Actions barcode_id={barcode}/> : <video ref={videoRef} style={{ width: '100%', maxWidth: '400px' }} />}
        </div>
    );
};

export default BarcodeSensor;