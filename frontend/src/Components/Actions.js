import React, { useState, useEffect } from "react";

const Actions = ({barcode_id}) => {

    const ENDPOINT = "192.168.4.1";
    const [barcode, setBarcode] = useState(barcode_id);
    const [barcodes, setBarcodes] = useState([]);
    const [name, setName] = useState("");
    const [date, setDate] = useState("");
    const [barcodeData, setBarcodeData] = useState(null);

    const fetchBarcode = async() => {

        try {
            const response = await fetch(`http://${ENDPOINT}/api/barcode/`);
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            //const data = await response.json();
            const data = [{"name":"Grapes","date":"11/16/2024","server":true}];
            setBarcodes(data);
        } catch (err) {
            
        }
    }

    const logItem = async() => {

    }

    const updateItem = async() => {

    }

    const removeItem = async() => {

    }

    useEffect(() => {
        const data = [{"name":"Grapes","date":"11/16/2024","server":true}];
        setName(data[0].name);
        setDate(data[0].date);
        setBarcodes(data);
    }, []);

    const handleNameChange = (event) => {
        setName(event.target.value);
    }
    const handleDateChange = (event) => {
        setDate(event.target.value);
    }

    const newBarcodeActions = () => {
        return(
            <div>
                <div>Barcode not logged in server</div>
                <div>Name: <input value={name} onChange={handleNameChange}/></div>
                <div>Put in fridge: <input value={date} onChange={handleDateChange}/></div>
                <div>
                    <button>Log</button>
                </div>
            </div>
        )
    }

    const oldBarcodeActions = () => {
        return(
            <div>
                <div>Barcode logged in server</div>
                <div>Name: <input value={name} onChange={handleNameChange}/></div>
                <div>Put in fridge: <input value={date} onChange={handleDateChange}/></div>
                <div>
                    <button>Remove</button>
                    <button>Update</button>
                </div>
            </div>
        )
    }

    const multipleBarcodeActions = () => {
        return(
            <div>

            </div>
        )
    }

    const getActions = () => {
        if (barcodes.length === 0) {

        } else if (barcodes.length === 1) {
            if (barcodes[0].server === true) {
                return oldBarcodeActions();
            } else {
                return newBarcodeActions();
            }
        } else {
            return multipleBarcodeActions();
        }
        
    }

    return(
        <div>
            {getActions()}

        </div>
    )
}

export default Actions;
