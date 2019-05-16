import React from 'react'
import AppHeader from './app-header/AppHeader'
import SearchComponent from './search-component/SearchComponent'

export const App = (props) => (
    <div>
        <AppHeader state ={open=true}/>
        <SearchComponent />
    </div>
)
