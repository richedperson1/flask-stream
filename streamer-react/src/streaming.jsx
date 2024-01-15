import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:5000'); // Replace with your server URL

const Streamer = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        socket.on('random_data', (data) => {
            setData(data.value);
        });
    }, []);

    return (
        <div>
            {data ? (
                <p>Received random data: {data}</p>
            ) : (
                <p>Waiting for data...</p>
            )}
        </div>
    );
};

export default Streamer;
