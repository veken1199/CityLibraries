import React from 'react'
import AppHeader from './app-header/AppHeader'
import SearchComponent from './search-component/SearchComponent'
import {DiscoveryComponent} from './discovery-component/DiscoveryComponent'

export const App = (props) => (
    <div>
        <AppHeader />
        <SearchComponent />
        <DiscoveryComponent />
    </div>
)