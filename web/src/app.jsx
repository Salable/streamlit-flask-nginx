import * as React from 'react';
import {createRoot} from 'react-dom/client';

import '../src/assets/style.css';

async function addSticky(url) {
  try {
    const response = await fetch('/api/url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    });

    if (!response.ok) {
      console.log(response)
      throw new Error('Network response was not ok');
    }

      const data = await response.json();
      console.dir(data)
      let stickyNote={}
      if (data.success && data.data) {
        const text = await miro.board.createText({
          content: data.data.keywords,
          style: {
            color: '#1a1a1a', // Default value: #1a1a1a (black)
            fillColor: 'transparent', // Default value: transparent (no fill)
            fillOpacity: 1, // Default value: 1 (solid color)
            fontFamily: 'arial', // Default font type for the text
            fontSize: 14, // Default font size
            textAlign: 'left', // Default alignment: left
          },
          x: 0,
          y: 0,
          width: 720,
          // 'height' is calculated automatically, based on 'width'
        });
        await miro.board.viewport.zoomTo(text);
      }
  } catch (error) {
    console.error('Error in addSticky:', error);
    // You can handle the error here, for example, by showing an error message to the user
  }
}
const App = () => {
  const [url, setUrl] = React.useState('');
  const [board, setBoard] = React.useState({})
  miro.board.getInfo().then(returnedBoard => {
    setBoard(returnedBoard)
  })
  const handleButtonClick = () => {
    addSticky(url);
  };

  return (
    <div className="grid wrapper">
      <div className="cs1 ce12">
        <h1>Open in Streamlit</h1>
        <p>You've just created your first Miro app!</p>
        <p>
          Jump over to Streamlit to check out some metrics.
        </p>
        <a href={"/?board="+board.id} target="_blank"> Open in Streamlit</a>
      </div>
      {/* <div className="cs1 ce12">
        <input 
          type="text" 
          value={url} 
          onChange={(e) => setUrl(e.target.value)} 
          placeholder="Enter URL" 
        />
        <button onClick={handleButtonClick} className="button primary">Add Sticky</button>
      </div> */}
    </div>
  );
};

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
