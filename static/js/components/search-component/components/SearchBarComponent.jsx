import React, {Component, useState} from 'react'
import {Input, Button, Container, Dropdown, Label} from 'semantic-ui-react'

export default class SearchBarComponent extends Component {
    constructor() {
        super()
        this.state = {
            cityInput: "",
            queryInput: ""
        }
    }

    render() {
        let queryHandlerCallback = this.props.queryHandler
        let cities = this.props.cities
        return (
            <Container textAlign={"left"} style={{width: "80%", float: "left"}}>
                <Input fluid
                       required
                       type='text'
                       maxLength="200"
                       placeholder='Insert the title of the book'
                       onChange={e => {
                           this.setState({queryInput: e.target.value})
                       }}
                >

                    <Dropdown
                        placeholder='Which city?'
                        selection
                        options={cities.map((city, index) => ({value: city, key: index, text: city}))}
                        onChange={e => {
                            this.setState({cityInput: e.target.textContent})
                        }}/>

                    <input />

                    <Button
                        type='submit'
                        icon='search'
                        onClick={e => queryHandlerCallback(this.state.queryInput, this.state.cityInput)}/>
                </Input >
            </Container>
        )
    }
}


