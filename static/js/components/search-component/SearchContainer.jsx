import React,  { Component }from 'react'
import {Container }from 'semantic-ui-react'
import {Input, Segment, Button }from 'semantic-ui-react'
import SearchBarComponent from './components/SearchBarComponent'
import SearchResultsComponent from './components/SearchResultsComponent'


export default class SearchContainer extends Component {
      constructor() {
        super()
        this.state =  {}
      }
      
      queryHandler(query:String) {
            console.log(query);
      }

      render() {
            return ( 
                  <Container >  
                        < SearchBarComponent queryHandler =  {this.queryHandler} > </SearchBarComponent> 
                        < SearchResultsComponent/>
                  </Container > 
            )
      }
}
