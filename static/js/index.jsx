// index.jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { App } from './components/App'

ReactDOM.render(
  <div>
    <App />
  </div>, document.getElementById('root'));

function handler(tsx) {
  console.log(tsx);
}

