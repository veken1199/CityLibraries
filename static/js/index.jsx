// index.jsx
import React from 'react';
import ReactDOM from 'react-dom';
import AppHeader from './components/AppHeader';

ReactDOM.render(
  <AppHeader state ={open=true}/>,
  document.getElementById('content')
);