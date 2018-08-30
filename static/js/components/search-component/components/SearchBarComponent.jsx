import React,  { Component } from 'react'
import {Container }from 'semantic-ui-react'
import {Input, Segment, Button }from 'semantic-ui-react'

export default class SearchBarComponent extends Component {
      constructor() {
            super()
            this.state = {}
      }

      submitSearchQuery(query:String) {
            console.log(query); 
      }
      
      render() {
            let queryHandlerFunc = this.props.queryHandler;
            let inputVal; 
            return (
                  < Segment >  
                        < Input fluid 
                              action =  {{color:'teal', icon:'search', onClick:e => queryHandlerFunc(inputVal)}}
                              placeholder = 'Insert the title of the book'
                              onChange =  {e => {inputVal = e.target.value}}/> 
                  </Segment >   
            )
      }
}


