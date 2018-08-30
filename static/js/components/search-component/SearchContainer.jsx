import axios from 'axios'
import React,  { Component } from 'react'
import {Container }from 'semantic-ui-react'
import {Input, Segment, Button, Dimmer, Loader }from 'semantic-ui-react'
import SearchBarComponent from './components/SearchBarComponent'
import SearchResultsComponent from './components/SearchResultsComponent'


export default class SearchContainer extends Component {
      constructor() {
            super()
            this.state = {queryData: [], isLoadingQuery: false}
            this.queryHandler = this.queryHandler.bind(this)
      }         

      queryHandler(query:String){
            this.setState({isLoadingQuery: true})
            axios.get('http://localhost:8082')
            .then((response) => {
                  console.log(response)
                  this.setState({queryData: response.data})
            }).catch((error) => {
                  console.log(error);
            }).then(() => {
                  this.setState({isLoadingQuery: false})
            })
      }

      render() {
            return ( 
                  <Container >  
                        < SearchBarComponent 
                              queryHandler =  { this.queryHandler }
                              isLoadingQuery = { this.state.isLoadingQuery }>
                        </SearchBarComponent> 
                        < SearchResultsComponent queryData = { this.state.queryData } />
                  </Container > 
            )
      }
}
