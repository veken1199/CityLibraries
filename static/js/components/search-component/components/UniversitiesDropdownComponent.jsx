import React,  { Component } from 'react'
import {Container } from 'semantic-ui-react'
import {Select, Dropdown} from 'semantic-ui-react'

export default class UnversitiesDropdownComponent extends Component {
      constructor() {
            super()
      }
      
      render() {
            let universities = this.props.universities

            return (
                  <Select placeholder='Go to..' options = {universities.map((university, index) => {
                                    return <Dropdown.Item 
                                                href={"#"+university}
                                                key ={index}>{university}
                                          </Dropdown.Item>
                              })}>
                  </Select>
            )
      }
}
