// index.jsx
import React from 'react';
import ReactDOM from 'react-dom';
import AppHeader from './components/AppHeader';
import SearchContainer from './components/search-component/SearchContainer';

ReactDOM.render(
  <div>
    <AppHeader state ={open=true}/>
    <SearchContainer />
  </div>, document.getElementById('content'));

function handler(tsx) {
  console.log(tsx);
}

