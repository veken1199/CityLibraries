import React,  { Component } from 'react'
import {Container }from 'semantic-ui-react'
import {Input, Segment, Button } from 'semantic-ui-react'
import UnversitiesDropdownComponent from './UniversitiesDropdownComponent'


export default class SearchBarComponent extends Component {
      constructor() {
            super()
            this.state = {}
      }

      render() {
            let queryHandlerFunc = this.props.queryHandler
            let isLoadingQuery = this.props.isLoadingQuery
            let queryData = this.props.queryData
            let inputVal
            
            return ( 
                  <Input fluid loading={isLoadingQuery}
                        placeholder = 'Insert the title of the book'
                        onChange =  {e => {inputVal = e.target.value}}
                        action>
                  <input />
                        <Button type='submit' icon='search' onClick = {e => queryHandlerFunc(inputVal)} />
                        <UnversitiesDropdownComponent universities = {queryData.map(obj=>obj.uni)} />
                  </Input >
            )
      }
}


