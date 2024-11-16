import React from "react";

const BarcodeItem = ({name, date}) => {

    return(
        <div>
            <div>{name}</div>
            <div>Placed in Fridge: {date}</div>
        </div>
    )

}

export default BarcodeItem;