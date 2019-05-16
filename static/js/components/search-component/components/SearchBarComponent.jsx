import React, {Component} from 'react'
import {Input, Button, Container} from 'semantic-ui-react'

export default class SearchBarComponent extends Component {
    constructor() {
        super()
        this.state = {}
    }

    render() {
        let queryHandlerCallback = this.props.queryHandler
        let inputVal

        return (
            <Container textAlign={"left"} style={{width:"80%", float: "left"}}>
                <Input fluid
                       placeholder='Insert the title of the book'
                       onChange={e => {
                           inputVal = e.target.value
                       }}>
                    <input />
                    <Button type='submit' icon='search' onClick={e => queryHandlerCallback(inputVal)}/>
                </Input >
            </Container>
        )
    }
}


