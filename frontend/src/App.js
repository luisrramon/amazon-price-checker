import React, { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const response = await fetch(`http://localhost:5000?url=${url}`);
    const data = await response.json();
    setData(data);
  };

  return (
    <div>
      <h1>Amazon Price Tracker</h1>
      <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="Amazon URL" />
      <button onClick={fetchData}>Check Price</button>
    
      {data && (
        <div>
          <h2>{data.title}</h2>
          <p>Price: ${data.price}</p>
        </div>
      )}
    </div>
  );
}

export default App;
