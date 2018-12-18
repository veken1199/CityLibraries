import axios from 'axios'
import React,  { Component } from 'react'
import {Container, Sticky }from 'semantic-ui-react'
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
            axios.get('http://localhost:8082/query/' + query)
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
                  <Container>  
                        <SearchBarComponent 
                              queryData = { this.state.queryData }
                              queryHandler =  { this.queryHandler }
                              isLoadingQuery = { this.state.isLoadingQuery }>
                        </SearchBarComponent> 
                        <br/>
                        <Container fluid>
                              <Loader active = {this.state.isLoadingQuery}></Loader>
                        </Container>
                        
                        <Dimmer.Dimmable as={Segment} blurring dimmed={this.state.isLoadingQuery}>
                              <SearchResultsComponent queryData = { this.state.queryData } />
                        </Dimmer.Dimmable>
                  </Container> 
            )
      }
}
